---
okf_version: 0.1
type: content_page
title: "Student Welcome Kit: Essential Cheat Sheet - CMSForNerd2"
description: "The one-stop reference guide for every student entering the CMSForNerd2 Astro 7.1 Laboratory."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="welcome-kit">
<header class="kit-header">
<h1>🚀 CMSForNerd2: Student Welcome Kit</h1>
<p class="quote">"Static modernisation without loss of simplicity."</p>
</header>

<div class="kit-intro">
<p>
Welcome to the laboratory. This document contains everything you need to manage your environment and pass your modules.
Keep this <strong>Cheat Sheet</strong> open as you work through the curriculum.
</p>
</div>

<section class="kit-section">
<h2>🛠️ The Essential Astro 7.1 "Nerd Stack"</h2>
<table class="stack-table">
<thead>
<tr>
<th>Tool</th>
<th>Purpose</th>
<th>Status Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Node.js & npm</strong></td>
<td>Astro 7.1 Runtime & Dependency Manager</td>
<td><code>node -v</code> (Must be 20.0+) / <code>npm -v</code></td>
</tr>
<tr>
<td><strong>Git</strong></td>
<td>Version Control & Cloning</td>
<td><code>git --version</code></td>
</tr>
<tr>
<td><strong>Astro 7.1 CLI</strong></td>
<td>Astro Local Dev & Compilation Engine</td>
<td><code>npx astro --version</code></td>
</tr>
<tr>
<td><strong>VS Code</strong></td>
<td>Code Editor / IDE</td>
<td><code>code .</code></td>
</tr>
</tbody>
</table>
</section>

<section class="kit-section">
<h2>📂 Quick Start Commands</h2>
<p>Run these inside your project workspace root folder:</p>
<div class="command-grid">
<div class="cmd-item">
<strong>Initialize Dependencies:</strong>
<code>npm install</code>
</div>
<div class="cmd-item">
<strong>Run Development Server:</strong>
<code>npm run dev</code>
</div>
<div class="cmd-item">
<strong>Compile Static Build:</strong>
<code>npm run build</code>
</div>
<div class="cmd-item">
<strong>Preview Production Build:</strong>
<code>npm run preview</code>
</div>
<div class="cmd-item">
<strong>Verify Type Safety:</strong>
<code>npx tsc --noEmit</code>
</div>
</div>
</section>

<section class="kit-section">
<h2>⚖️ Our RFC 2119 Standards</h2>
<p>As a student of this laboratory, your code must adhere to these requirement levels:</p>
<ul class="standard-list">
<li><span class="must">MUST:</span> Every page file carries OKF v0.1 YAML frontmatter with correct schema fields.</li>
<li><span class="must">MUST:</span> Compile with zero errors during <code>npm run build</code>.</li>
<li><span class="must-not">MUST NOT:</span> Hardcode page routes. Rely on Astro's Content Collections routing structure.</li>
<li><span class="should">SHOULD:</span> Customise your styles within Astro scoped layout styles.</li>
<li><span class="may">MAY:</span> Implement custom MDX elements for interactive laboratory exercises.</li>
</ul>
</section>

<section class="kit-section">
<h2>🛡️ Static Security Laws</h2>
<div class="security-grid">
<div class="law">
<h3>1. Validate Schema Metadata</h3>
<p>Verify that your page frontmatter strictly adheres to the schema defined in <code>src/content.config.ts</code>.</p>
</div>
<div class="law">
<h3>2. Escape Output</h3>
<p>Astro automatically escapes text variables rendered inside brackets, eliminating XSS injection by default.</p>
</div>
<div class="law">
<h3>3. Pure Static Execution</h3>
<p>There is zero server execution, making server-side paths completely immutable and safe from injection attacks.</p>
</div>
<div class="law rfc-law">
<h3>4. Be Reachable (RFC 9116)</h3>
<p>Maintain your <code>security.txt</code> and <a href="/security-policy">Security Policy</a> statically inside your <code>public/.well-known/</code> folder.</p>
</div>
</div>
</section>

<section class="kit-section troubleshooting">
<h2>🆘 Troubleshooting</h2>
<dl>
<dt>Astro Build Failure?</dt>
<dd>Ensure that your newly added page has correct YAML formatting in the frontmatter blocks.</dd>

<dt>Node.js Version Error?</dt>
<dd>Verify that your Node environment is on version 20 or higher. Run <code>node -v</code> to verify.</dd>

<dt>Port Already In Use?</dt>
<dd>If port 4321 is blocked, kill the existing process: <code>kill $(lsof -t -i :4321) 2>/dev/null || true</code>.</dd>
</dl>
</section>

<footer class="path-to-cert">
<h2>🎓 Path to Certification</h2>
<div class="roadmap">
<div class="step"><strong>1. Setup:</strong> Install tools & run <code>npm install</code>.</div>
<div class="step"><strong>2. Modules 1-3:</strong> Astro Architecture, Standards, and Static Security.</div>
<div class="step"><strong>3. Modules 4-5:</strong> Write automated checks and build QA verification.</div>
<div class="step"><strong>4. Final Exam:</strong> Fix the "Broken Build" configuration.</div>
<div class="step"><strong>5. Certification:</strong> Claim your Astro Modernisation Certificate!</div>
</div>
<div class="cta">
<a href="/lab-manual" class="btn welcome-btn">🚀 Start Laboratory Module 1</a>
</div>
</footer>
</article>

<style>
.welcome-kit h1 { color: #004085; border-bottom: 2px solid #004085; padding-bottom: 0.5rem; margin-top: 0; }
.welcome-kit .kit-header { text-align: center; margin-bottom: 2rem; }
.welcome-kit .quote { font-style: italic; color: #666; font-size: 1.1rem; }
.welcome-kit .kit-intro { background: #e2f3f5; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #004085; margin-bottom: 2rem; }
.welcome-kit h2 { color: #333; margin-top: 2rem; border-bottom: 1px solid #eee; padding-bottom: 0.3rem; }
.welcome-kit .stack-table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
.welcome-kit .stack-table th, .welcome-kit .stack-table td { text-align: left; padding: 0.75rem; border: 1px solid #dee2e6; }
.welcome-kit .stack-table th { background: #f8f9fa; }
.welcome-kit .command-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.welcome-kit .cmd-item { background: #fff; border: 1px solid #ddd; padding: 1rem; border-radius: 4px; }
.welcome-kit .cmd-item code { display: block; margin-top: 0.5rem; background: #212529; color: #f8f9fa; padding: 0.5rem; border-radius: 4px; white-space: pre-wrap; word-break: break-all; }
.welcome-kit .standard-list { list-style: none; padding: 0; }
.welcome-kit .standard-list li { margin-bottom: 0.75rem; }
.welcome-kit .must { color: #d9534f; font-weight: bold; }
.welcome-kit .must-not { color: #d9534f; font-weight: bold; text-decoration: underline; }
.welcome-kit .should { color: #f0ad4e; font-weight: bold; }
.welcome-kit .may { color: #5bc0de; font-weight: bold; }
.welcome-kit .security-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.welcome-kit .law { background: #fff9f9; border: 1px solid #ffeeba; padding: 1rem; border-radius: 4px; }
.welcome-kit .law h3 { margin-top: 0; font-size: 1rem; color: #856404; }
.welcome-kit .troubleshooting dl { margin: 1rem 0; }
.welcome-kit .troubleshooting dt { font-weight: bold; color: #c82333; margin-top: 1rem; }
.welcome-kit .path-to-cert { background: #f8f9fa; padding: 2rem; border-radius: 8px; margin-top: 3rem; text-align: center; }
.welcome-kit .roadmap { display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 2rem; text-align: left; max-width: 400px; margin-left: auto; margin-right: auto; }
.welcome-kit .step { border-left: 3px solid #004085; padding-left: 1rem; }
.welcome-kit .welcome-btn { background: #004085; color: #fff; padding: 1rem 2rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.welcome-kit .welcome-btn:hover { background: #002752; }
</style>