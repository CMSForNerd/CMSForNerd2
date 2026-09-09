---
type: "content_page"
title: "Module 10 Worksheet | CMSForNerd2 Wasm Vector Search & FastMCP ADR Validation"
description: "Interactive lab worksheet exploring client-side Wasm vector search micro-frontends and FastMCP server tools for real-time Architectural Decision Record (ADR) validation."
schemaType: "TechArticle"
author: "CMSForNerd2 Architecture & AI Education Team"
topics: ["wasm", "vector-search", "fastmcp", "adr", "ai", "mcp", "architecture"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: lab-module10.md
  url: src/content/pages/lab-module10.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-08-01T09:00:00Z'
tags: ["wasm", "vector-search", "fastmcp", "adr", "ai", "mcp", "architecture"]
---

<article class="lab-module-page" itemscope itemtype="https://schema.org/TechArticle">
<header class="module-header">
<h1 itemprop="headline">🚀 Laboratory Module 10: Wasm Vector Search & FastMCP ADR Validation</h1>
<p class="intro">
Welcome to <strong>Laboratory Module 10</strong>. In this advanced module, students explore next-generation static web technologies: running <strong>client-side WebAssembly (Wasm) vector search embeddings</strong> for semantic page discovery, and utilizing <strong>FastMCP (Model Context Protocol) gateway tools</strong> for real-time Architectural Decision Record (ADR) validation.
</p>
</header>

<section class="learning-objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li><strong>Client-Side Wasm Vector Search Micro-Frontends:</strong> Understand how lightweight ONNX / Wasm embedding models enable client-side semantic search without server costs or API key exposure.</li>
<li><strong>Model Context Protocol (MCP) Server Architecture:</strong> Explore how Python FastMCP gateways (`tools/mcp/server.py`) expose routes, spatial memory, and validation tools directly to AI coding agents.</li>
<li><strong>Architectural Decision Record (ADR) Validation:</strong> Use automated schema checkers to ensure ADRs match strict structural, temporal, and governance criteria.</li>
<li><strong>Privacy-Preserving Edge Intelligence:</strong> Deliver local AI functionality directly inside browser WebAssembly runtimes.</li>
</ul>
</section>

<section class="exercise-box">
<h2>📝 Exercise 10.1: Client-Side Wasm Vector Search Micro-Frontends</h2>
<p>
Traditional search indexes rely on exact keyword matching. Modern WebAssembly micro-frontends allow lightweight vector embedding models (such as `all-MiniLM-L6-v2` compiled to Wasm) to run directly inside the user's browser, calculating cosine similarity over static page vector indices.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Exploring Wasm Vector Search Architecture</h3>
<p>
Examine how client-side vector search initializes inside a Web Worker thread:
</p>
<pre><code>// Initialize Wasm Vector Search Worker
const worker = new Worker('/wasm/vector-search-worker.js');

// Query semantic embeddings client-side
worker.postMessage({
  type: 'SEMANTIC_SEARCH',
  query: 'How do I configure Nginx Content Security Policy hashes?'
});

worker.onmessage = (event) => {
  const { results } = event.data;
  console.log('Top Semantic Match:', results[0].title, 'Score:', results[0].score);
};</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 10.2: FastMCP Gateway Architecture</h2>
<p>
The repository implements a Python FastMCP (Model Context Protocol) server gateway located at <code>tools/mcp/server.py</code>. This allows AI developer tools and agent systems to query Astro routes, search SSG pages, inspect OpenWiki concepts, and validate system schemas programmatically.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Inspecting FastMCP Tools</h3>
<p>
Inspect the FastMCP tool registration in <code>tools/mcp/server.py</code>:
</p>
<pre><code>@mcp.tool()
def search_ssg_routes(query: str) -> list[dict[str, str]]:
    """Performs full-text search across all compiled Astro SSG routes."""
    # Queries compiled page content and returns formatted matching routes
    ...

@mcp.tool()
def validate_diagram_schema(mermaid_code: str) -> dict[str, str]:
    """Validates Mermaid diagram blocks against standard visual guidelines."""
    ...</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 10.3: Architectural Decision Record (ADR) Real-Time Validation</h2>
<p>
Architectural Decision Records (ADRs) document key system choices (e.g. adopting Astro 7.1 SSG, using Wasm Pagefind search, implementing FastMCP). Using FastMCP tools, AI agents and developers can validate ADR formatting, status fields, and linked references in real-time.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Validating ADR Compliance</h3>
<p>
Execute unit tests in <code>tests/unit/mcp.py</code> to verify MCP tool execution and ADR schema assertions:
</p>
<pre><code># Run FastMCP unit test suite
python3 -m pytest tests/unit/mcp.py

# Expected Output:
# tests/unit/mcp.py :: test_fastmcp_route_listing PASSED
# tests/unit/mcp.py :: test_fastmcp_adr_validation PASSED</code></pre>
</div>
</section>

<nav class="footer-nav">
<a href="/lab-module9" class="btn btn-secondary">← Back to Module 9</a>
<a href="/graduation" class="btn btn-primary">Proceed to Graduation →</a>
</nav>
</article>

<style>
.lab-module-page { max-width: 900px; margin: 0 auto; line-height: 1.7; color: #1e293b; }
.module-header h1 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 8px; }
.intro { background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 5px solid #22c55e; margin: 20px 0; }
.learning-objectives { background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
.exercise-box { margin-bottom: 40px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
.exercise-box h2 { color: #059669; border-bottom: 2px solid #d1fae5; padding-bottom: 6px; margin-top: 0; }
.try-it-box { background: #fafafa; border-left: 4px solid #059669; padding: 15px; border-radius: 4px; margin-top: 15px; }
.try-it-box pre { background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 6px; overflow-x: auto; font-family: 'SF Mono', monospace; font-size: 0.9rem; }
.btn { display: inline-block; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 10px; }
.btn-primary { background: #0d6efd; color: white; }
.btn-secondary { background: #e2e8f0; color: #333; }
.footer-nav { display: flex; justify-content: space-between; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 30px; }
</style>
