---
type: "content_page"
title: "Module 8 Worksheet | CMSForNerd2 Wasm SRI & Brotli Performance"
description: "Interactive lab worksheet for whitelisting WebAssembly binaries with build-time SRI hashes and configuring pre-rendered Brotli sub-10ms TTFB assets."
schemaType: "TechArticle"
author: "CMSForNerd2 Security & Performance Education Team"
topics: ["security", "wasm", "sri", "brotli", "performance", "nginx", "pagefind"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: lab-module8.md
  url: src/content/pages/lab-module8.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-08-01T09:00:00Z'
tags: ["security", "wasm", "sri", "brotli", "performance", "nginx", "pagefind"]
---

<article class="lab-module-page" itemscope itemtype="https://schema.org/TechArticle">
<header class="module-header">
<h1 itemprop="headline">⚡ Laboratory Module 8: WebAssembly SRI Whitelisting & Pre-rendered Brotli Performance</h1>
<p class="intro">
Welcome to <strong>Laboratory Module 8</strong>. In this module, we explore how WebAssembly (Wasm) search binaries in static sites (such as Pagefind under <code>dist/pagefind/</code>) can be secured with <strong>Build-Time Subresource Integrity (SRI) Hashes</strong> and accelerated for <strong>sub-10ms Time-To-First-Byte (TTFB)</strong> using pre-rendered Brotli asset compression.
</p>
</header>

<section class="learning-objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li><strong>WebAssembly Cryptographic Integrity:</strong> Learn how to calculate build-time Subresource Integrity (SRI) hashes for WebAssembly (<code>.wasm</code>) binaries.</li>
<li><strong>Configure Nginx CSP & Static Whitelists:</strong> Incorporate Wasm integrity hashes into Nginx Content-Security-Policy (CSP) and HTTP response headers.</li>
<li><strong>Pre-rendered Brotli Static Compression:</strong> Understand how pre-compiling static assets into <code>.br</code> and <code>.gz</code> archives bypasses dynamic CPU compression bottlenecks at runtime, delivering sub-10ms TTFB responses.</li>
<li><strong>Immutable Asset Caching Policies:</strong> Configure <code>Cache-Control: public, max-age=31536000, immutable</code> rules for versioned static search indices.</li>
</ul>
</section>

<section class="exercise-box">
<h2>📝 Exercise 8.1: Build-Time SRI Hashes for Wasm Binaries</h2>
<p>
WebAssembly modules run compiled binary code in browser sandboxes. To guarantee that Pagefind Wasm search binaries (<code>dist/pagefind/*.wasm</code>) have not been tampered with in transit or on storage, we generate cryptographic SHA-384 or SHA-256 SRI hashes during the build process.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Generating Cryptographic SRI Hashes</h3>
<p>
Execute the build pipeline and generate the SRI hash for the compiled Pagefind Wasm binary using <code>openssl</code> or <code>shasum</code>:
</p>
<pre><code># Calculate base64-encoded SHA-384 hash of Pagefind Wasm module
openssl dgst -sha384 -binary dist/pagefind/pagefind_web_bg.wasm | openssl base64 -A

# Expected Output Format:
# sha384-K1R+4Z6X... (whitelisted in script-src / wasm-src header)</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 8.2: Sub-10ms TTFB Pre-rendered Brotli Assets</h2>
<p>
Dynamic HTTP compression on web servers adds runtime CPU latency to every incoming request. Modern static site deployments eliminate this overhead by pre-compressing static build artifacts during CI/CD using Brotli level 11 compression.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Verifying Pre-rendered Brotli Compression</h3>
<p>
Inspect the Nginx server configuration (<code>nginx/nginx.conf</code>). Notice how <code>brotli_static on;</code> and <code>gzip_static on;</code> instruct the server to serve pre-rendered <code>.br</code> files directly from disk without runtime processing:
</p>
<pre><code># Pre-rendering assets with Brotli in CI build script
brotli --best --keep dist/*.html dist/pagefind/*.wasm dist/pagefind/*.js

# Nginx static delivery directive
location /pagefind/ {
    brotli_static on;
    gzip_static on;
    add_header Cache-Control "public, max-age=31536000, immutable";
}</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 8.3: Nginx Defensive Headers for Wasm</h2>
<p>
To prevent cross-site side-channel attacks and enforce strict browser isolation when executing WebAssembly, we configure Cross-Origin Opener Policy (COOP) and Cross-Origin Embedder Policy (COEP) headers.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Inspecting Isolation Headers</h3>
<p>
Verify that response headers for <code>/pagefind/</code> include site isolation directives:
</p>
<pre><code>Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
Content-Type: application/wasm</code></pre>
</div>
</section>

<nav class="footer-nav">
<a href="/lab-module7" class="btn btn-secondary">← Back to Module 7</a>
<a href="/lab-module9" class="btn btn-primary">Proceed to Module 9 →</a>
</nav>
</article>

<style>
.lab-module-page { max-width: 900px; margin: 0 auto; line-height: 1.7; color: #1e293b; }
.module-header h1 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 8px; }
.intro { background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 5px solid #22c55e; margin: 20px 0; }
.learning-objectives { background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
.exercise-box { margin-bottom: 40px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
.exercise-box h2 { color: #0284c7; border-bottom: 2px solid #e0f2fe; padding-bottom: 6px; margin-top: 0; }
.try-it-box { background: #fafafa; border-left: 4px solid #0284c7; padding: 15px; border-radius: 4px; margin-top: 15px; }
.try-it-box pre { background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 6px; overflow-x: auto; font-family: 'SF Mono', monospace; font-size: 0.9rem; }
.btn { display: inline-block; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 10px; }
.btn-primary { background: #0d6efd; color: white; }
.btn-secondary { background: #e2e8f0; color: #333; }
.footer-nav { display: flex; justify-content: space-between; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 30px; }
</style>
