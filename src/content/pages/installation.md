---
okf_version: 0.1
type: "content_page"
title: "Installation Guide | CMSForNerd2"
description: "Official installation steps for CMSForNerd2. Learn how to configure the Astro 7.1 environment, run the dev server, and compile static builds."
schemaType: "HowTo"
author: "CMSForNerd Team & Gemini AI"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<h1>Introduction</h1>
<p>
<strong>CMSForNerd2</strong> is a lightweight, database-free static modernization of the legacy dynamic PHP CMS.
By leveraging <strong>Astro 7.1 Static Site Generator (SSG)</strong>, the workspace compiles layout components, Markdown documents, and stylesheets into purely static files.
This makes the compiled output incredibly fast, zero-cost to scale, and completely secure—just deploy the static <code>dist/</code> directory!
</p>
<p>
We designed this framework to teach users modern web standards, including <strong>HTML5, CSS3, TypeScript, and Astro 7.1 Content Collections</strong>.
The modernization ensures full cross-platform compatibility across Windows, Linux, and macOS development environments.
</p>

<h3>Requirements</h3>
<ul>
<li><strong>Runtime Environment:</strong> Node.js v20+ (LTS recommended).</li>
<li><strong>Dependency Manager:</strong> npm (v10+).</li>
<li><strong>Version Control:</strong> Git.</li>
<li><strong>No Database or PHP runtime required at all!</strong></li>
</ul>

<h3>Installation</h3>
<ol>
<li>Clone the latest repository from GitHub.</li>
<li>Open your terminal inside the root workspace folder.</li>
<li>Run <code>npm install</code> to initialize all packages and dependencies.</li>
<li>Start the local development server: <code>npm run dev</code>.</li>
</ol>

<h3>Step 1: Dependency Management (npm)</h3>
<p>
CMSForNerd2 manages its build integrations and support packages using <code>package.json</code> and standard npm packages:
</p>
<div class="code-box" style="background: #1e1e1e; color: #dcdcdc; padding: 1rem; border-radius: 8px;">
<pre><code># Install modern Astro 7.1 support packages
npm install

# Resolve potential peer-dependency conflicts with legacy integrations
npm install --legacy-peer-deps</code></pre>
</div>

<h3>Step 2: Compile Static Builds</h3>
<p>
Before shipping your site, run the Astro compiler to compile all layouts, markdown pages, and stylesheets into static files under the <code>dist/</code> directory:
</p>
<div class="code-box" style="background: #1e1e1e; color: #dcdcdc; padding: 1rem; border-radius: 8px;">
<pre><code># Compile the static assets
npm run build</code></pre>
</div>
<p><em>Note: A successful, safe build will output <strong>Complete!</strong> and report the list of generated routes.</em></p>

<h3>How to Create Pages</h3>
<p>
CMSForNerd2 utilizes Astro Content Collections. To author a page, navigate to <code>src/content/pages/</code> and create a new Markdown (<code>.md</code>) or MDX (<code>.mdx</code>) file carrying standard OKF YAML frontmatter.
</p>

<h3>Recommended Tools</h3>
<ul>
<li><strong>Code Editor:</strong> <a href="https://code.visualstudio.com/" target="_blank">VS Code</a> with the Astro and MDX extensions.</li>
<li><strong>Static Hosting:</strong> Render.com, Cloudflare Pages, Netlify, or unprivileged NGINX Alpine containers.</li>
<li><strong>Browsers:</strong> Google Chrome or Firefox Developer Tools for checking static CSS Grid layouts and service worker pre-caches.</li>
</ul>

<div class="next-steps" style="background: #fff3cd; border: 2px solid #ffeeba; padding: 2rem; border-radius: 8px; margin-top: 3rem; text-align: center;">
<h3>✅ Installation Complete?</h3>
<p>Your NEXT STEP is to open the <strong>Student Welcome Kit</strong> to get your "Nerd Stack" ready for the laboratory.</p>
<p><a href="/welcome-kit" class="btn" style="background: #856404; color: #fff; padding: 0.8rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-block;">🚀 Open Student Welcome Kit</a></p>
</div>

<p style="text-align: center; margin-top: 2rem; font-style: italic; color: #666;">
Your project workspace is fully modernized to Astro 7.1!
</p>

<style>
.code-box pre { margin: 0; overflow-x: auto; }
.code-box code { font-family: 'Consolas', 'Monaco', monospace; }
h3 { border-bottom: 2px solid #eee; padding-bottom: 5px; margin-top: 2rem; color: #2c3e50; }
li { margin-bottom: 10px; }
.btn:hover { filter: brightness(1.2); }
</style>