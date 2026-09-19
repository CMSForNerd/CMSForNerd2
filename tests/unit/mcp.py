"""Unit tests for FastMCP server tools, SSG route introspection, and WebSocket/SSE transports."""

from typing import Any

import pytest
from starlette.testclient import TestClient

from tools.mcp.server import (
    create_mcp_app,
    dispatch_wasm_component_tool,
    get_openwiki_concept,
    get_route_content,
    get_sitemap_routes,
    list_ssg_routes,
    run_server,
    search_ssg_routes,
    validate_diagram_schema,
    validate_wasm_cm_wit_interface,
)


def test_list_ssg_routes() -> None:
    """Verify that list_ssg_routes returns active SSG routes with required metadata fields."""
    routes: list[dict[str, Any]] = list_ssg_routes()
    assert isinstance(routes, list)
    assert len(routes) > 0

    route_slugs = [r["slug"] for r in routes]
    assert "index" in route_slugs
    assert "about" in route_slugs
    assert "lab-manual" in route_slugs

    for r in routes:
        assert "route" in r
        assert "title" in r
        assert "description" in r
        assert "source_file" in r


def test_get_route_content() -> None:
    """Verify fetching route content for both valid and invalid routes."""
    res_index: dict[str, Any] = get_route_content("index")
    assert res_index["found"] is True
    assert res_index["route"] == "/"
    assert isinstance(res_index["frontmatter"], dict)
    assert len(res_index["body"]) > 0

    res_about: dict[str, Any] = get_route_content("/about")
    assert res_about["found"] is True
    assert res_about["route"] == "/about"

    res_missing: dict[str, Any] = get_route_content("non-existent-route-12345")
    assert res_missing["found"] is False
    assert "error" in res_missing


def test_search_ssg_routes() -> None:
    """Verify keyword search across SSG routes."""
    results: list[dict[str, Any]] = search_ssg_routes("Astro")
    assert isinstance(results, list)
    assert len(results) > 0

    slugs = [r["slug"] for r in results]
    assert len(slugs) > 0

    empty_results: list[dict[str, Any]] = search_ssg_routes("xyz123nonexistentkeyword")
    assert len(empty_results) == 0


def test_get_sitemap_routes() -> None:
    """Verify parsing published URLs from sitemap.txt."""
    sitemap_urls: list[str] = get_sitemap_routes()
    assert isinstance(sitemap_urls, list)
    assert len(sitemap_urls) > 0
    assert any("cmsfornerd" in url.lower() for url in sitemap_urls)


def test_get_openwiki_concept() -> None:
    """Verify querying spatial memory concepts."""
    res: dict[str, Any] = get_openwiki_concept("DSOM")
    assert res["found"] is True
    assert res["matches_count"] > 0
    assert len(res["matches"]) > 0


def test_validate_wasm_cm_wit_interface() -> None:
    """Verify WebAssembly Component Model WIT interface specification validation."""
    wit_code = """package mcp:agent-tools@0.2.0;

interface search-engine {
  record search-query {
    query: string,
    limit: u32
  }
  func execute-search(req: search-query) -> string;
}"""
    res_valid: dict[str, Any] = validate_wasm_cm_wit_interface(wit_code)
    assert res_valid["valid"] is True
    assert res_valid["interface_name"] == "mcp:agent-tools@0.2.0"
    assert "execute-search" in res_valid["functions"]
    assert "search-query" in res_valid["types"]

    res_empty: dict[str, Any] = validate_wasm_cm_wit_interface("")
    assert res_empty["valid"] is False
    assert "error" in res_empty


def test_dispatch_wasm_component_tool() -> None:
    """Verify WebAssembly Component Model multi-language tool dispatching."""
    res_rust: dict[str, Any] = dispatch_wasm_component_tool(
        component_name="mcp:agent-tools/search",
        function_name="execute-search",
        args={"query": "Astro", "limit": 10},
        target_language="rust",
    )
    assert res_rust["dispatched"] is True
    assert res_rust["component"] == "mcp:agent-tools/search"
    assert res_rust["function"] == "execute-search"
    assert res_rust["target_language"] == "rust"
    assert res_rust["abi"] == "wasm-cm-canonical-v1"
    assert res_rust["output"]["status"] == "success"

    res_go: dict[str, Any] = dispatch_wasm_component_tool(
        component_name="mcp:agent-tools/vector",
        function_name="rank-docs",
        args={"query": "Wasm"},
        target_language="go",
    )
    assert res_go["target_language"] == "go"


def test_validate_diagram_schema() -> None:
    """Verify diagram schema validation for valid and invalid Mermaid code."""
    valid_flowchart = "graph TD\n  A[Start] --> B[End]"
    res_valid: dict[str, Any] = validate_diagram_schema(valid_flowchart)
    assert res_valid["valid"] is True
    assert res_valid["diagram_type"] == "graph"
    assert len(res_valid["warnings"]) == 0

    invalid_diagram = "invalidType TD\n  A --> B"
    res_invalid: dict[str, Any] = validate_diagram_schema(invalid_diagram)
    assert res_invalid["valid"] is False
    assert res_invalid["diagram_type"] == "unknown"


def test_create_mcp_app_and_websocket_transport() -> None:
    """Verify creating Starlette app and executing JSON-RPC tool calls over WebSocket transport."""
    app = create_mcp_app(transport="websocket")
    client = TestClient(app)

    with client.websocket_connect("/ws") as websocket:
        # 1. Handshake initialize
        websocket.send_json({"jsonrpc": "2.0", "method": "initialize", "id": 1})
        init_res = websocket.receive_json()
        assert init_res["id"] == 1
        assert "serverInfo" in init_res["result"]

        # 2. Ping check
        websocket.send_json({"jsonrpc": "2.0", "method": "ping", "id": 2})
        ping_res = websocket.receive_json()
        assert ping_res["id"] == 2

        # 3. List FastMCP tools
        websocket.send_json({"jsonrpc": "2.0", "method": "tools/list", "id": 3})
        tools_res = websocket.receive_json()
        assert tools_res["id"] == 3
        tools = tools_res["result"]["tools"]
        assert len(tools) >= 6
        tool_names = [t["name"] for t in tools]
        assert "list_ssg_routes" in tool_names
        assert "validate_diagram_schema" in tool_names

        # 4. Invoke FastMCP tool over WebSocket
        websocket.send_json(
            {
                "jsonrpc": "2.0",
                "method": "tools/call",
                "id": 4,
                "params": {
                    "name": "validate_diagram_schema",
                    "arguments": {"diagram_code": "graph TD\n  A --> B"},
                },
            }
        )
        call_res = websocket.receive_json()
        assert call_res["id"] == 4
        assert "content" in call_res["result"]
        text_content = call_res["result"]["content"][0]["text"]
        assert "valid" in text_content


def test_websocket_reconnect_failure_mode() -> None:
    """Verify WebSocket reconnect failure modes, malformed JSON error recovery, and session restoration."""
    app = create_mcp_app(transport="websocket")
    client = TestClient(app)

    # 1. Connect and send malformed JSON
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("MALFORMED_JSON_STRING")
        err_res = websocket.receive_json()
        assert err_res["error"]["code"] == -32700
        assert err_res["error"]["message"] == "Parse error"

        # Verify server remains functional after parse error
        websocket.send_json({"jsonrpc": "2.0", "method": "ping", "id": 10})
        ping_res = websocket.receive_json()
        assert ping_res["id"] == 10

    # 2. Simulate connection drop and reconnect recovery
    with client.websocket_connect("/ws") as reconnected_ws:
        reconnected_ws.send_json({"jsonrpc": "2.0", "method": "initialize", "id": 11})
        init_res = reconnected_ws.receive_json()
        assert init_res["id"] == 11
        assert "serverInfo" in init_res["result"]


def test_mcp_webtransport_datagram_handler() -> None:
    """Verify HTTP/3 WebTransport datagram packet ingestion and spatial memory mesh status."""
    app = create_mcp_app(transport="websocket")
    client = TestClient(app)

    payload = {
        "node_id": "wt-agent-alpha-1",
        "transport": "WebTransport-Datagram",
        "concepts": ["WebGPU INT4 Speculative KV-Cache", "WebTransport P2P Datagrams"],
    }
    response = client.post("/webtransport/datagrams", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "datagram_received"
    assert data["transport"] == "WebTransport-Datagram"
    assert data["node_id"] == "wt-agent-alpha-1"
    assert len(data["synced_concepts"]) == 2
    assert "latency_ms" in data


def test_mcp_webrtc_p2p_mesh_transport() -> None:
    """Verify FastMCP WebRTC P2P agent mesh signaling, ICE candidate registration, and spatial memory sync."""
    app = create_mcp_app(transport="websocket")
    client = TestClient(app)

    with client.websocket_connect("/ws/webrtc") as websocket:
        # 1. Test SDP Offer & Answer Exchange
        websocket.send_json(
            {
                "type": "webrtc_offer",
                "node_id": "agent-alpha",
                "sdp": "v=0\r\no=- 12345 IN IP4 127.0.0.1",
            }
        )
        answer_res = websocket.receive_json()
        assert answer_res["type"] == "webrtc_answer"
        assert answer_res["status"] == "signaling_established"

        # 2. Test ICE Candidate Registration
        websocket.send_json(
            {
                "type": "ice_candidate",
                "node_id": "agent-alpha",
                "candidate": {"candidate": "candidate:1 1 UDP 2013266431 127.0.0.1 5000 typ host"},
            }
        )
        ice_res = websocket.receive_json()
        assert ice_res["type"] == "ice_candidate_ack"
        assert ice_res["status"] == "candidate_registered"

        # 3. Test Spatial Memory P2P Mesh Concept Broadcast Sync
        websocket.send_json(
            {
                "type": "mesh_sync",
                "node_id": "agent-alpha",
                "concepts": ["FastMCP P2P", "WebGPU PagedAttention", "WebNN Graph"],
            }
        )
        sync_res = websocket.receive_json()
        assert sync_res["type"] == "mesh_sync_ack"
        assert sync_res["synced_concepts_count"] == 3
        assert sync_res["status"] == "spatial_memory_updated"


def test_run_server_invalid_transport() -> None:
    """Verify that run_server raises ValueError for unsupported transport modes."""
    with pytest.raises(ValueError, match="Unsupported transport mode"):
        run_server(transport="invalid-transport-mode")
