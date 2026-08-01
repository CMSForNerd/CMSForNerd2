---
okf_version: 0.1
type: content_page
title: "Windows 11 Setup Guide: Node.js & Astro 7.1 | CMSForNerd2"
description: "Step-by-step guide to setting up Node.js, Git, and VS Code for Astro 7.1 development on Windows 11."
schemaType: "HowTo"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="setup-guide">
<header class="guide-header">
<h1>🚀 The "Future-Proof" Setup Guide: CMSForNerd2</h1>
<p class="subtitle">Prepared for Node.js & Astro 7.1 Static Modernisation</p>
</header>

<div class="guide-intro">
<p>
This guide will walk you through setting up a professional development environment on <strong>Windows 11</strong>.
We are building this to support the latest static-site features in <strong>Astro 7.1</strong> and ensure compatibility with
modern TypeScript and unprivileged container standards. By focusing on static optimization and build-time safety, this setup is "future-proof."
</p>
</div>

<section class="phase">
<h2>🛠️ Phase 1: Installing the Professional Toolchain</h2>

<div class="tool-card">
<h3>1. Node.js (The Static Compilation Engine)</h3>
<p>Node.js is the preferred runtime environment because it executes the Astro compiler locally to render pages.</p>
<ul>
<li><strong>Download:</strong> Visit <a href="https://nodejs.org" target="_blank">nodejs.org</a> and download the v20 LTS installer.</li>
<li><strong>Version Selection:</strong> During setup, ensure you select the standard LTS package.</li>
<li><strong>npm integration:</strong> The installer automatically bundles <code>npm</code>, our package and integration manager.</li>
</ul>
</div>

<div class="tool-card">
<h3>2. Git for Windows (The Code Mover)</h3>
<ul>
<li><strong>Download:</strong> <a href="https://git-scm.com" target="_blank">git-scm.com</a>.</li>
<li><strong>Configuration:</strong> Select standard default options during installation.</li>
</ul>
</div>

<div class="tool-card">
<h3>3. VS Code (The Recommended Editor)</h3>
<p><strong>Why:</strong> Standard text editors struggle with Markdown, frontmatter, and TypeScript formatting. VS Code provides high-speed type hints, autocompletion, and integrated terminal controls.</p>
</div>
</section>

<section class="phase">
<h2>📂 Phase 2: Cloning the Repository</h2>
<ol>
<li>Open your terminal (PowerShell or Git Bash).</li>
<li>Navigate to your projects directory:
<div class="terminal-block"><code>cd ~\Projects</code></div>
</li>
<li>Clone the project:
<div class="terminal-block"><code>git clone https://github.com/CMSForNerd/CMSForNerd2.git</code></div>
</li>
<li>Enter the directory:
<div class="terminal-block"><code>cd CMSForNerd2</code></div>
</li>
</ol>
</section>

<section class="phase">
<h2>⚙️ Phase 3: Initializing for Astro 7.1</h2>
<p>To make the CMS run locally, we must install the dependencies.</p>
<ol>
<li>Run npm install:
<div class="terminal-block"><code>npm install --legacy-peer-deps</code></div>
<p><em>*This downloads Astro 7.1, Vite, and other supporting plugins required for static compilation.*</em></p>
</li>
<li>Verify Node Version:
<div class="terminal-block"><code>node -v</code></div>
<p>Ensure it says <strong>v20.x.x</strong> or higher.</p>
</li>
</ol>
</section>

<section class="phase">
<h2>🧪 Phase 4: Running the Compile Audit</h2>
<p>To confirm your installation is perfect and complies with the RFC 2119 "MUST" requirements:</p>
<div class="terminal-block"><code>npm run build</code></div>
<h3>What this checks:</h3>
<ul>
<li><strong>YAML Frontmatter:</strong> Are all Markdown page metadata tags valid?</li>
<li><strong>Astro Compiler:</strong> Can layouts, scoped CSS styles, and component slots build with zero errors?</li>
<li><strong>Sitemaps & PWA SW:</strong> Are XML sitemaps and Workbox service workers registered successfully?</li>
</ul>
</section>

<section class="phase reasoning">
<h2>💡 Important: Why Astro 7.1 Matters</h2>
<ul>
<li><strong>Absolute Security:</strong> Static sites have no runtime database or server-side script engine. There is zero vulnerability surface for hackers to attack!</li>
<li><strong>Type Safety:</strong> Zod and TypeScript schemas catch formatting mistakes before they leave your machine.</li>
<li><strong>Performance:</strong> Pre-compiled static assets load 10x faster than traditional dynamic databases.</li>
</ul>
</section>

<footer class="guide-footer">
<h3>Next Step for Students</h3>
<p>Once your terminal shows a successful build report, you are ready to open the project in your editor and start the <a href="/lab-manual">Lab Manual</a>!</p>
</footer>
</article>

<style>
.setup-guide h1 { color: #007bff; border-bottom: 2px solid #007bff; padding-bottom: 0.5rem; }
.setup-guide .guide-header { text-align: center; margin-bottom: 3rem; }
.setup-guide .subtitle { font-size: 1.2rem; color: #666; font-weight: bold; }
.setup-guide .guide-intro { background: #e7f3ff; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #007bff; margin-bottom: 3rem; }
.setup-guide h2 { color: #333; margin-top: 3rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; }
.setup-guide .tool-card { background: #fff; border: 1px solid #ddd; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
.setup-guide .tool-card h3 { margin-top: 0; color: #0056b3; }
.setup-guide .terminal-block { background: #1a1a1a; color: #00ff00; padding: 1rem; font-family: 'Consolas', monospace; border-radius: 4px; margin: 1rem 0; overflow-x: auto; max-width: 100%; box-sizing: border-box; white-space: pre-wrap; word-break: break-all; }
.setup-guide .phase.reasoning { background: #fffbea; padding: 1.5rem; border-radius: 8px; border: 1px solid #fde68a; }
.setup-guide .phase.reasoning h2 { border-bottom-color: #fde68a; }
.setup-guide .guide-footer { background: #f8f9fa; padding: 2rem; border-radius: 8px; text-align: center; margin-top: 4rem; }
</style>