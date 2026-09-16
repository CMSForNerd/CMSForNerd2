"""FastMCP server exposing live Astro SSG routes, content, and spatial memory to AI agents.

This module implements a Model Context Protocol (MCP) server utilizing FastMCP to grant
AI agents (e.g., Claude Desktop, Cursor, Google Jules) direct introspection capabilities
over CMSForNerd2's static site routes, content collections, sitemaps, and spatial memory.
It supports stdio, Server-Sent Events (SSE), and WebSocket transport modes for real-time
AI pair-programming integration.
"""

import argparse
import json
import os
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any, Literal

import uvicorn
import yaml
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.websockets import WebSocket, WebSocketDisconnect

# Initialize FastMCP Server Gateway
mcp = FastMCP(
    name="CMSForNerd2 Live SSG Gateway",
    instructions="Model Context Protocol server for inspecting CMSForNerd2 SSG routes, content collections, and spatial memory.",
)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PAGES_DIR = REPO_ROOT / "src" / "content" / "pages"
SITEMAP_FILE = REPO_ROOT / "sitemap.txt"
KNOWLEDGE_FILE = REPO_ROOT / ".agents" / "brain" / "knowledge.md"


def _extract_frontmatter(file_path: Path) -> tuple[dict[str, Any], str]:
    """Extracts YAML frontmatter and body text from a Markdown file.

    Args:
        file_path: Path to the target Markdown file.

    Returns:
        A tuple containing the parsed YAML frontmatter dictionary and the body text string.
    """
    if not file_path.is_file():
        return {}, ""

    content = file_path.read_text(encoding="utf-8")
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, content.strip()


@mcp.tool()
def list_ssg_routes() -> list[dict[str, Any]]:
    """Lists all active Astro SSG routes with titles, descriptions, and file locations.

    Returns:
        List of dictionaries detailing route slugs, titles, descriptions, and source files.
    """
    routes: list[dict[str, Any]] = []
    if not PAGES_DIR.exists():
        return routes

    for page_file in sorted(PAGES_DIR.glob("*.md")):
        slug = page_file.stem
        route_path = "/" if slug == "index" else f"/{slug}"
        frontmatter, _ = _extract_frontmatter(page_file)

        routes.append(
            {
                "route": route_path,
                "slug": slug,
                "title": frontmatter.get("title", slug.replace("-", " ").title()),
                "description": frontmatter.get("description", ""),
                "topics": frontmatter.get("topics", []),
                "source_file": str(page_file.relative_to(REPO_ROOT)),
            }
        )
    return routes


@mcp.tool()
def get_route_content(route_slug: str) -> dict[str, Any]:
    """Retrieves frontmatter metadata and Markdown body content for a specific SSG route.

    Args:
        route_slug: The slug or route path (e.g., 'about', '/lab-manual', 'index').

    Returns:
        Dictionary containing metadata, body content, and route status.
    """
    clean_slug = route_slug.strip("/").strip()
    if not clean_slug:
        clean_slug = "index"

    target_file = PAGES_DIR / f"{clean_slug}.md"
    if not target_file.is_file():
        return {
            "found": False,
            "error": f"Route '{route_slug}' not found in content collection.",
            "route": route_slug,
        }

    frontmatter, body = _extract_frontmatter(target_file)
    return {
        "found": True,
        "route": "/" if clean_slug == "index" else f"/{clean_slug}",
        "slug": clean_slug,
        "frontmatter": frontmatter,
        "body": body,
        "source_file": str(target_file.relative_to(REPO_ROOT)),
    }


@mcp.tool()
def search_ssg_routes(query: str) -> list[dict[str, Any]]:
    """Searches case-insensitively across titles, descriptions, topics, and body content of all SSG pages.

    Args:
        query: Search string or keyword to look for.

    Returns:
        List of matching route metadata and snippet matches.
    """
    results: list[dict[str, Any]] = []
    query_lower = query.lower().strip()
    if not query_lower or not PAGES_DIR.exists():
        return results

    for page_file in sorted(PAGES_DIR.glob("*.md")):
        slug = page_file.stem
        route_path = "/" if slug == "index" else f"/{slug}"
        frontmatter, body = _extract_frontmatter(page_file)

        title = str(frontmatter.get("title", ""))
        desc = str(frontmatter.get("description", ""))
        raw_topics = frontmatter.get("topics") or []
        topics = " ".join(str(t) for t in raw_topics if t)

        body_lower = body.lower()
        searchable_text = f"{title} {desc} {topics} {body_lower}"
        if query_lower in searchable_text:
            snippet = ""
            pos = body_lower.find(query_lower)
            if pos >= 0:
                start = max(0, pos - 40)
                end = min(len(body), pos + 100)
                snippet = body[start:end].replace("\n", " ").strip()
            elif desc:
                snippet = desc

            results.append(
                {
                    "route": route_path,
                    "slug": slug,
                    "title": frontmatter.get("title", slug),
                    "description": desc,
                    "snippet": f"...{snippet}..." if snippet else "",
                    "source_file": str(page_file.relative_to(REPO_ROOT)),
                }
            )

    return results


@mcp.tool()
def get_sitemap_routes() -> list[str]:
    """Parses and returns all published site URLs from sitemap.txt.

    Returns:
        List of published sitemap URLs.
    """
    if not SITEMAP_FILE.is_file():
        return []

    lines = SITEMAP_FILE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


@mcp.tool()
def get_openwiki_concept(concept_name: str) -> dict[str, Any]:
    """Queries knowledge points and concept records from spatial memory knowledge base.

    Args:
        concept_name: The concept or keyword to query in spatial memory (e.g., 'FastMCP', 'DSOM', 'Astro').

    Returns:
        Matching knowledge records and concepts.
    """
    if not KNOWLEDGE_FILE.is_file():
        return {"found": False, "error": "Knowledge base file missing."}

    content = KNOWLEDGE_FILE.read_text(encoding="utf-8")
    query_lower = concept_name.lower().strip()

    matches: list[str] = []
    paragraphs = re.split(r"\n\n+", content)
    for p in paragraphs:
        if query_lower in p.lower():
            matches.append(p.strip())

    return {
        "found": len(matches) > 0,
        "query": concept_name,
        "matches_count": len(matches),
        "matches": matches,
    }


@mcp.tool()
def validate_diagram_schema(diagram_code: str) -> dict[str, Any]:
    """Validates Mermaid or architecture diagram syntax according to repository diagram standards.

    Args:
        diagram_code: Mermaid definition block or raw diagram content string.

    Returns:
        Validation results containing status, diagram type, line count, and warnings.
    """
    code = diagram_code.strip()
    if not code:
        return {"valid": False, "error": "Diagram code string is empty."}

    valid_types = [
        "graph",
        "flowchart",
        "sequenceDiagram",
        "classDiagram",
        "stateDiagram",
        "erDiagram",
        "gantt",
        "pie",
        "gitGraph",
        "architecture",
    ]

    lines = [line.strip() for line in code.splitlines() if line.strip()]
    first_line = lines[0] if lines else ""

    detected_type = "unknown"
    for dtype in valid_types:
        if first_line.startswith(dtype):
            detected_type = dtype
            break

    is_valid = detected_type != "unknown"
    warnings: list[str] = []

    if not is_valid:
        warnings.append(
            f"First non-empty line '{first_line}' does not match known Mermaid types ({', '.join(valid_types[:5])}...)."
        )

    if "-->" not in code and "-.->" not in code and "==>" not in code and detected_type in ["graph", "flowchart"]:
        warnings.append("Flowchart diagram contains no connector arrows (e.g. '-->').")

    return {
        "valid": is_valid,
        "diagram_type": detected_type,
        "line_count": len(lines),
        "warnings": warnings,
    }


async def _mcp_websocket_handler(websocket: WebSocket) -> None:
    """Handles real-time WebSocket connections and JSON-RPC 2.0 messages for live AI pair programming.

    Args:
        websocket: The Starlette WebSocket connection instance.
    """
    await websocket.accept()
    tool_map: dict[str, Callable[..., Any]] = {
        "list_ssg_routes": list_ssg_routes,
        "get_route_content": get_route_content,
        "search_ssg_routes": search_ssg_routes,
        "get_sitemap_routes": get_sitemap_routes,
        "get_openwiki_concept": get_openwiki_concept,
        "validate_diagram_schema": validate_diagram_schema,
    }

    try:
        while True:
            raw_msg = await websocket.receive_text()
            try:
                data: dict[str, Any] = json.loads(raw_msg)
            except json.JSONDecodeError:
                await websocket.send_json(
                    {
                        "jsonrpc": "2.0",
                        "error": {"code": -32700, "message": "Parse error"},
                        "id": None,
                    }
                )
                continue

            method = data.get("method")
            msg_id = data.get("id")

            if method == "initialize":
                await websocket.send_json(
                    {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {"tools": {"listChanged": True}},
                            "serverInfo": {
                                "name": "CMSForNerd2 Live SSG Gateway",
                                "version": "2.0.0",
                            },
                        },
                    }
                )
            elif method == "notifications/initialized":
                pass
            elif method == "ping":
                await websocket.send_json({"jsonrpc": "2.0", "id": msg_id, "result": {}})
            elif method in ("tools/list", "list_tools"):
                tools_list = [
                    {
                        "name": "list_ssg_routes",
                        "description": "Lists all active Astro SSG routes with metadata.",
                    },
                    {
                        "name": "get_route_content",
                        "description": "Retrieves metadata and body for an SSG route.",
                    },
                    {
                        "name": "search_ssg_routes",
                        "description": "Searches titles, descriptions, and body content of SSG pages.",
                    },
                    {
                        "name": "get_sitemap_routes",
                        "description": "Parses and returns published site URLs.",
                    },
                    {
                        "name": "get_openwiki_concept",
                        "description": "Queries spatial memory knowledge base.",
                    },
                    {
                        "name": "validate_diagram_schema",
                        "description": "Validates Mermaid diagram syntax.",
                    },
                ]
                await websocket.send_json({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": tools_list}})
            elif method in ("tools/call", "call_tool"):
                params: dict[str, Any] = data.get("params") or {}
                name = str(params.get("name") or data.get("name") or "")
                raw_args = params.get("arguments") or data.get("arguments")
                arguments: dict[str, Any] = raw_args if isinstance(raw_args, dict) else {}

                if name in tool_map:
                    try:
                        func = tool_map[name]
                        res = func(**arguments) if arguments else func()
                        await websocket.send_json(
                            {
                                "jsonrpc": "2.0",
                                "id": msg_id,
                                "result": {
                                    "content": [
                                        {"type": "text", "text": json.dumps(res, default=str)}
                                    ]
                                },
                            }
                        )
                    except (TypeError, ValueError, KeyError) as err:
                        await websocket.send_json(
                            {
                                "jsonrpc": "2.0",
                                "id": msg_id,
                                "error": {"code": -32603, "message": str(err)},
                            }
                        )
                else:
                    await websocket.send_json(
                        {
                            "jsonrpc": "2.0",
                            "id": msg_id,
                            "error": {"code": -32601, "message": f"Tool '{name}' not found"},
                        }
                    )
            else:
                if msg_id is not None:
                    await websocket.send_json(
                        {
                            "jsonrpc": "2.0",
                            "id": msg_id,
                            "error": {"code": -32601, "message": f"Method '{method}' not implemented"},
                        }
                    )
    except WebSocketDisconnect:
        pass


def create_mcp_app(transport: str = "sse") -> Starlette:
    """Creates a Starlette ASGI application with SSE and WebSocket real-time gateway endpoints.

    Args:
        transport: Transport protocol mode ('sse', 'http', or 'websocket').

    Returns:
        Configured Starlette application supporting live AI pair programming integration.
    """
    selected_transport: Literal["sse", "http"] = (
        "sse" if transport in ("sse", "websocket", "ws") else "http"
    )
    app = mcp.http_app(transport=selected_transport)
    app.router.add_websocket_route("/ws", _mcp_websocket_handler)
    app.router.add_websocket_route("/ws/mcp", _mcp_websocket_handler)
    return app


def run_server(transport: str = "stdio", host: str = "127.0.0.1", port: int = 8000) -> None:
    """Runs the FastMCP gateway server using the requested transport mode.

    Args:
        transport: Transport protocol ('stdio', 'sse', 'websocket', or 'http').
        host: Host IP address to bind server endpoints to.
        port: Port number for HTTP/SSE/WebSocket server modes.
    """
    transport_mode = transport.lower().strip()
    if transport_mode == "stdio":
        mcp.run(transport="stdio")
    elif transport_mode in ("websocket", "ws"):
        app = create_mcp_app(transport="websocket")
        uvicorn.run(app, host=host, port=port)
    elif transport_mode in ("sse", "http", "streamable-http"):
        valid_mode: Literal["stdio", "http", "sse", "streamable-http"] = (
            "sse" if transport_mode == "sse"
            else "http" if transport_mode == "http"
            else "streamable-http"
        )
        mcp.run(transport=valid_mode, host=host, port=port)
    else:
        raise ValueError(f"Unsupported transport mode: '{transport}'")


def main() -> None:
    """Parses command-line arguments and environment variables to start the FastMCP Gateway."""
    parser = argparse.ArgumentParser(
        description="CMSForNerd2 FastMCP Gateway Server with stdio, SSE, and WebSocket transport support."
    )
    parser.add_argument(
        "--transport",
        type=str,
        default=os.getenv("MCP_TRANSPORT", "stdio"),
        choices=["stdio", "sse", "websocket", "ws", "http"],
        help="Transport mode for AI agent integration (default: stdio or MCP_TRANSPORT).",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.getenv("MCP_HOST", "127.0.0.1"),
        help="Host IP address for HTTP/SSE/WebSocket server modes (default: 127.0.0.1 or MCP_HOST).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("MCP_PORT", "8000")),
        help="Port number for HTTP/SSE/WebSocket server modes (default: 8000 or MCP_PORT).",
    )

    args = parser.parse_args()
    run_server(transport=args.transport, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
