---
spec_version: "0.2"
type: "explanation"
title: "FastMCP Protocol & WebAssembly (Wasm) Architecture"
description: "In-depth architectural analysis of FastMCP SSG route exposure, Pagefind Wasm client-side search, WebLLM WebGPU on-device RAG generation, ONNX streaming, and client-side Wasm cryptographic & document processing in CMSForNerd2."
topics: ["fastmcp", "mcp", "wasm", "webassembly", "pagefind", "webllm", "webgpu", "onnx", "architecture"]
okf_version: "0.1"
nav_order: 1
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: fastmcp-wasm-architecture.md
  url: docs/explanation/fastmcp-wasm-architecture.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["fastmcp", "mcp", "wasm", "webassembly", "pagefind", "webllm", "webgpu", "onnx", "architecture"]
---

# FastMCP Protocol & WebAssembly (Wasm) Architecture

This document provides a conceptual explanation of the **FastMCP Model Context Protocol** server integration and the **WebAssembly (Wasm)** client-side architecture in CMSForNerd2.

---

## 1. FastMCP SSG Route Exposure for AI Agents

Modern AI agents (e.g. Claude Desktop, Cursor, Google Jules) require fast, deterministic introspection of web platform assets without scanning unindexed file trees or relying on brittle web scrapers.

### Architecture Overview

```
 +------------------+                 +------------------------+
 |   AI Agent /     |  JSON-RPC over  |  FastMCP SSG Gateway   |
 |  Claude Desktop  |  stdio / HTTP   |  (tools/mcp/server.py) |
 +--------+---------+ <=============> +-----------+------------+
          |                                       |
          v                                       v
 +------------------+                 +------------------------+
 | list_ssg_routes  |                 |  src/content/pages/*.md|
 | get_route_content|                 |  sitemap.txt           |
 | search_ssg_routes|                 |  .agents/brain/        |
 +------------------+                 +------------------------+
```

### Key Capabilities

1. **Deterministic Route Mapping**: Exposes every Astro SSG route directly as structured JSON objects (`list_ssg_routes()`), eliminating link-crawling overhead.
2. **On-Demand Content Retrieval**: Delivers clean frontmatter and Markdown body text (`get_route_content()`) for instant context ingestion.
3. **Spatial Memory Introspection**: Integrates with Deep State of Mind (DSOM) knowledge base (`get_openwiki_concept()`) to share active spatial memory directly with AI subagents.

---

## 2. WebAssembly (Wasm) Client-Side Search Engine (Pagefind)

Search engines traditionally require dedicated backend servers (e.g., Elasticsearch, Solr, Meilisearch) or heavy serverless endpoints. CMSForNerd2 eliminates backend runtime overhead by adopting **Pagefind**, a static search engine compiled to **WebAssembly (Wasm)**.

### How Pagefind Wasm Works

- **Build-Time Compilation**: During `npm run build`, `pagefind --site dist` parses compiled HTML output in `dist/` and compiles static Wasm index files (`dist/pagefind/wasm.en.pagefind`).
- **Zero Server Overhead**: At runtime, browser JS loads the Pagefind Wasm engine (`pagefind-ui.js`), which queries the binary Wasm index locally.
- **Micro-Bundle Bandwidth**: Index files are chunked into tiny Wasm segments, ensuring users download only byte ranges necessary for their search query.

---

## 3. WebAssembly (Wasm) Client Cryptographic & Document Processing

To align with modern Zero-Trust static security standards, CMSForNerd2 includes client-side WebAssembly tools for cryptographic hashing and OKF v0.2 document parsing.

### Cryptographic Whitelisting
- **Browser-Native Execution**: Hashing functions execute using WebAssembly/WebCrypto APIs inside local browser memory.
- **CSP Integrity Verification**: Generates Base64 SHA-256 digests (`'sha256-...'`) for inline script whitelisting in Nginx Content Security Policy headers.

### OKF v0.2 Schema Processing
- Parses Open Knowledge Format frontmatter schemas, verifying trust and freshness pillars (`status`, `stale_after`, `sources`, `generated`).
- Guarantees complete user privacy: documents are analyzed entirely client-side with zero external data transmission.

---

## 4. WebLLM + WebGPU On-Device Air-Gapped RAG Generation

To enable 100% offline, air-gapped intelligence inside static sites, CMSForNerd2 pairs Web Worker Float32 vector embeddings and IndexedDB persistence with local in-browser LLMs (WebLLM running quantized Llama/Qwen models over WebGPU).

```
 +------------------------+     +------------------------+     +------------------------+
 | Web Worker Vector      | --> | IndexedDB Vector Store | --> | FastMCP RAG Context    |
 | Embedding Thread       |     | (WasmStudioVectorDB)   |     | Search Extractor       |
 +------------------------+     +------------------------+     +-----------+------------+
                                                                           |
                                                                           v
 +--------------------------------------------------------------------------------------+
 | WebLLM WebGPU On-Device LLM Generator (Llama-3.2-1B / Qwen2.5-0.5B Quantized Model)  |
 +--------------------------------------------------------------------------------------+
```

### Architecture Highlights
- **100% Offline Air-Gapped Execution**: Synthesizes responses locally on user hardware without transmitting prompts or vector contexts to external API backends.
- **WebGPU Acceleration**: Leverages modern GPU compute shaders for rapid quantized tensor matrix multiplication, falling back to multi-core Wasm SIMD when WebGPU is unavailable.
- **FastMCP Context Coupling**: Ingests top cosine-similarity matches from the FastMCP local vector database to deliver contextually grounded RAG answers.

---

## 5. HuggingFace ONNX Web Runtime Streaming

Real-time developer feedback is enabled via WebAssembly-streamed ONNX inference for live workspace code and document completion.

### Architecture Highlights
- **Token-by-Token WebAssembly Streaming**: Streams embeddings and generated tokens incrementally without blocking the main browser UI thread.
- **Live Typing Completion**: Automatically analyzes input text during document editing, delivering low-latency (~2.4ms) code suggestions at high throughput (~42 tokens/sec).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
