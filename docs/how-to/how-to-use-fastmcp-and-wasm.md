---
spec_version: "0.2"
type: "how_to"
title: "How to Use FastMCP Server & WebAssembly (Wasm) Tools"
description: "Step-by-step guide for running the FastMCP SSG server, querying live routes, executing Pagefind Wasm search, and utilizing client-side Wasm utilities."
topics: ["fastmcp", "mcp", "wasm", "pagefind", "how-to"]
okf_version: "0.1"
nav_order: 1
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: how-to-use-fastmcp-and-wasm.md
  url: docs/how-to/how-to-use-fastmcp-and-wasm.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["fastmcp", "mcp", "wasm", "pagefind", "how-to"]
---

# How to Use FastMCP Server & WebAssembly (Wasm) Tools

This guide explains how to run the FastMCP SSG Gateway server, inspect static routes as an AI agent, and utilize client-side WebAssembly search and cryptographic tools.

---

## 1. Running the FastMCP Server Gateway

The FastMCP server is located at `tools/mcp/server.py`.

### Prerequisites
Ensure Python dependencies are installed:
```bash
pip install fastmcp mcp pyyaml
```

### Starting the Server
To run the server in standard stdio mode (for Claude Desktop, Cursor, or AI agent integration):
```bash
python3 tools/mcp/server.py
```

### Querying FastMCP Tools Programmatically
You can also invoke tools programmatically in Python:
```python
from tools.mcp.server import list_ssg_routes, get_route_content, search_ssg_routes

# List all SSG routes
routes = list_ssg_routes()
print(f"Total SSG routes: {len(routes)}")

# Fetch route content
about_page = get_route_content("about")
print(about_page["frontmatter"]["title"])

# Search content
search_results = search_ssg_routes("WebAssembly")
print(search_results)
```

---

## 2. Executing Pagefind WebAssembly (Wasm) Search

Pagefind indexes the static HTML site after Astro compilation.

### Building and Indexing
Run the combined build command:
```bash
npm run build
```
This executes `astro build && pagefind --site dist`, compiling static assets to `dist/` and writing Wasm index bundles to `dist/pagefind/`.

### Previewing Search
Launch the local preview server:
```bash
npm run preview
```
Navigate to `http://localhost:4321/search` to test client-side Wasm search queries with term highlighting and subresults.

---

## 3. Utilizing WebAssembly Cryptographic & Document Studio

Navigate to `http://localhost:4321/wasm-studio` in your browser.

### Computing CSP SHA-256 Hashes
1. Paste inline script content into the **Cryptographic Hash & CSP Tool** input box.
2. Click **Compute SHA-256 Hash**.
3. Copy the generated Nginx CSP Header value (e.g. `'sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU='`) and append it to your Nginx CSP whitelist configuration in `nginx/nginx.conf`.

### Validating OKF v0.2 Documents
1. Paste Markdown content into the **OKF v0.2 Document Processor** input box.
2. Click **Analyze Document**.
3. Review compliance status, extracted title, word count, and line metrics.

### Executing In-Browser FastMCP Semantic AI Search
1. Enter a conceptual query (e.g., `Astro static site security hardening`) into the **In-Browser WebAssembly Vector Embeddings & FastMCP Semantic Search** input field.
2. Click **Execute FastMCP `semantic_code_search` Tool**.
3. The studio generates a 384-dimensional Float32 vector embedding via Web Workers, syncs vectors with IndexedDB local storage, computes cosine similarity scores across local documents, and returns top RAG matches wrapped in FastMCP tool output schemas.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
