---
okf_version: 0.1
type: "content_page"
title: "Lab Worksheet: Module 5 - CMSForNerd2"
description: "Module 5: Static Build QA and Service Worker Validation. Learn to audit the compiled dist directory and PWA offline fallback assets."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet">
<h1>📊 Student Lab Worksheet: Module 5</h1>
<p class="subtitle">Topic: Build Quality Assurance and PWA Service Worker Auditing</p>

<p class="intro">
In this final lab module, students learn to audit the compiled static assets generated in the output directory (<code>dist/</code>).
<strong>Build QA</strong> ensures that page clean URLs are correctly structured, sitemaps exist, and service worker manifests are optimized to support complete offline capabilities.
</p>

<div class="requirement-alert">
<strong>Requirement Level:</strong> Students <strong>MUST</strong> compile a zero-error production build and verify sitemap and service worker registration to pass the course.
</div>

<section class="objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li>Understand the difference between **Astro Source Files** and the **Compiled Static Output (dist/)**.</li>
<li>Analyze and validate the statically generated files.</li>
<li>Audit the **@vite-pwa/astro** service worker caching configuration.</li>
</ul>
</section>

<section class="step">
<h2>⚙️ Step 1: Source versus Compiled Assets</h2>
<p>Unlike dynamic systems, an Astro SSG compiles layout components, Markdown pages, and stylesheets into purely static files. We never edit files directly inside the <code>dist/</code> folder because they are regenerated on every build.</p>
<p><strong>Task:</strong> Compile the production-ready static assets. Run:</p>
<div class="terminal-block">
<code>npm run build</code>
</div>
<p>Look for the <code>dist/</code> directory. You will see a list of clean folders and compiled files ready to be served by unprivileged NGINX web servers.</p>
</section>

<section class="step">
<h2>🧪 Step 2: Auditing Clean URLs and AMP Outputs</h2>
<p>In our modernised layout, clean URLs are preserved without dynamic query strings (e.g., instead of <code>about.php?view=amp</code>, we statically build <code>about/index.html</code> and <code>about/amp/index.html</code>).</p>
<p><strong>Task:</strong> Verify the structure of generated files under <code>dist/</code>:</p>
<ol>
<li>Verify that <code>dist/index.html</code> has compiled successfully.</li>
<li>Ensure the directory structure contains the correct dual AMP pathways (e.g., <code>dist/about/amp/index.html</code>).</li>
<li>Observe that <code>dist/sitemap.xml</code> and <code>dist/offline/index.html</code> are created.</li>
</ol>
</section>

<section class="step">
<h2>🔍 Step 3: Auditing PWA Service Worker</h2>
<p>Progressive Web App features are managed via the <code>@vite-pwa/astro</code> integration inside <code>astro.config.mjs</code>. This registers a robust, offline-capable service worker.</p>
<div class="exercise">
<h3>Exercise:</h3>
<ol>
<li>Ensure that the service worker file <code>dist/sw.js</code> exists.</li>
<li>Open <code>dist/registerSW.js</code> and examine how the client browser is instructed to cache static page assets.</li>
<li><strong>The Offline Check:</strong> Launch the static preview server:
<div class="terminal-block"><code>npm run preview</code></div>
</li>
<li>Open the local URL in your browser and toggle the "Offline" checkbox in your DevTools Application tab. Confirm that the page continues loading correctly from cache!</li>
</ol>
</div>
</section>

<section class="step">
<h2>✅ Step 4: The Quality Assurance Audit</h2>
<p>A professional static site engineer verifies sitemaps and machine-readable data structures before pushing changes to git.</p>
<p><strong>Final Challenge:</strong> Access the sitemap file at <code>dist/sitemap.xml</code>. Confirm that all static routes (including dual AMP paths) exist in the sitemap output.</p>
</section>

<footer class="standards-summary">
<h2>🎓 Summary of Standards for Module 5</h2>
<ul>
<li><strong>MUST:</strong> Generate a production build successfully without any compilation errors before deployment.</li>
<li><strong>SHOULD:</strong> Cache all essential static resources (JS, CSS, HTML layouts) in the service worker's pre-cache manifest.</li>
<li><strong>MAY:</strong> Exclude temporary backup or test files from the final static publication folder.</li>
</ul>
<div class="question-box">
<p><strong>Question for the Student:</strong> Why does deploying static assets to an unprivileged NGINX server provide a safer production profile than dynamic PHP runtimes?</p>
<p class="hint">(Hint: Consider if a compromised asset can execute malicious backend shell commands in a static environment versus a server running dynamic PHP scripts).</p>
</div>
</footer>

<nav class="progress-nav">
<a href="/lab-module4" class="btn prev">&lt; Previous: Module 4 (Automated Testing)</a>
<a href="/final-exam" class="btn next">Next: Final Exam (Break-Fix Challenge) &gt;</a>
</nav>
</article>

<style>
.lab-worksheet h1 { color: #0275d8; margin-bottom: 0.1rem; }
.lab-worksheet .subtitle { font-size: 1.2rem; color: #777; margin-bottom: 2rem; }
.lab-worksheet .requirement-alert { background: #d9edf7; border: 1px solid #bce8f1; color: #31708f; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }
.lab-worksheet h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; margin-top: 2rem; }
.lab-worksheet .intro { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #0275d8; margin-bottom: 2rem; }
.lab-worksheet .terminal-block { background: #1a1a1a; color: #fff; padding: 1rem; font-family: 'Consolas', 'Monaco', monospace; border-radius: 4px; margin: 1rem 0; border-left: 5px solid #0275d8; }
.lab-worksheet .terminal-block code { color: #5bc0de; }
.lab-worksheet .exercise { background: #fcfcfc; padding: 1.5rem; border: 1px solid #e1e1e1; border-radius: 8px; margin: 1rem 0; }
.lab-worksheet .question-box { background: #fee7e7; border: 1px solid #fad2d2; color: #9a2020; padding: 1.5rem; border-radius: 8px; margin: 2rem 0; }
.lab-worksheet .standards-summary { margin-top: 3rem; background: #f8f9fa; padding: 1.5rem; border-radius: 8px; border: 1px solid #eee; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #0275d8; color: #fff; }
@media (max-width: 768px) { .progress-nav { flex-direction: column; gap: 1rem; } }
</style>