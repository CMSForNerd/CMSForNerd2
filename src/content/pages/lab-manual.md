---
okf_version: 0.1
type: content_page
title: "The Lab Manual: Astro 7.1 Static Modernisation - CMSForNerd2"
description: "Welcome to the CMSForNerd2 educational suite. A transparent laboratory for learning modern Astro 7.1 static site architectures."
schemaType: "WebPage"
author: "Harisfazillah Jamel & Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-manual">
<h1>🎓 CMSForNerd2: The Developer’s Lab Manual</h1>
<p class="intro">
Welcome to the CMSForNerd2 educational suite. This workspace is designed to be a <strong>transparent laboratory</strong>.
Every file is fully accessible, every static choice is documented, and every security/PWA feature
is an interactive lesson in professional web standards using Astro 7.1.
</p>

<section class="module">
<h2>📚 Laboratory Module 1: Astro 7.1 Architecture & TypeScript</h2>
<p>In this module, students explore the transition from server-side PHP to modern Astro Static Site Generator (SSG) patterns, optimised for Astro 7.1 with strict TypeScript and code-fence structures.</p>
<div class="exercise">
<h3>Exercise 1.1: Component Frontmatter</h3>
<p>Observe how Astro's code fence (<code>---</code>) executes strictly at build-time to establish variables, query content collections, and pass metadata to layout wrappers.</p>
<p><a href="/lab-module1" class="btn">📝 Open Student Worksheet: Module 1</a></p>
</div>
<div class="exercise">
<h3>Exercise 1.2: Astro Layouts</h3>
<p>See how standard layouts (<code>src/layouts/Layout.astro</code>) handle top-level page structures and styles, using the <code>&lt;slot /&gt;</code> tag as the injection target for pages.</p>
</div>
<div class="exercise">
<h3>Exercise 1.3: Content Collections & Zod</h3>
<p>Learn to use strict TypeScript schemas via Zod to validate and structure page metadata, eliminating runtime database and data retrieval overhead.</p>
</div>
</section>

<section class="module">
<h2>⚖️ Laboratory Module 2: Standards & Compliance</h2>
<p>Students learn that high-quality static code is defined by its adherence to global schema standards and formatting specifications.</p>
<p><a href="/lab-module2" class="btn">📝 Open Student Worksheet: Module 2</a></p>
<ul>
<li><strong>Requirement Level (RFC 2119):</strong> We use <em>MUST</em>, <em>SHOULD</em>, and <em>MAY</em> to define project boundaries.
<ul>
<li>Rule: All generated pages <strong>MUST</strong> be HTML5 compliant.</li>
<li>Rule: Page frontmatter metadata <strong>MUST</strong> pass Zod schema validation.</li>
</ul>
</li>
<li><strong>Prettier & Linter:</strong> Use the integrated linter and type check tools to maintain a zero-error development workspace.</li>
</ul>
<div class="exercise">
<h3>Exercise 2.3: Semantic Metadata & Sitemaps</h3>
<p>Understand how <strong>JSON-LD</strong> and XML Sitemaps help AI agents and crawlers parse your static contents.</p>
<ul>
<li>Examine layout tags to see dynamic JSON-LD generation based on schema.org specifications.</li>
<li>Observe the statically compiled <code>dist/sitemap.xml</code> file.</li>
<li><strong>Verification:</strong> Validate JSON-LD structures using <a href="https://validator.schema.org/" target="_blank">Google's Structured Data Testing Tool</a>.</li>
</ul>
</div>
</section>

<section class="module">
<h2>🛡️ Laboratory Module 3: Defensive Static Engineering</h2>
<p>Security is a key pillar of CMSForNerd2. Learn how static-site compilation provides absolute defense-in-depth against legacy web vulnerabilities.</p>
<div class="lab-box">
<h3>Lab: Elimination of Server Vulnerabilities</h3>
<p>Students examine how static site generation completely eliminates runtime injection types like LFI, Directory Traversal, and SQL injection.</p>
<p><a href="/lab-module3" class="btn">📝 Open Student Worksheet: Module 3</a></p>
</div>
<div class="lab-box">
<h3>Lab 3.2: Content Security Policy (CSP) & SRI</h3>
<p>Learn to configure NGINX headers and static meta elements to enforce strict Content Security Policies and Subresource Integrity (SRI) on your compiled assets.</p>
<ul>
<li><strong>Concept:</strong> CSP instructs browsers on exactly which scripts, styles, and assets are permitted to execute.</li>
<li><strong>Exercise:</strong> Inspect the static NGINX server configuration (<code>nginx/default.conf</code>) to see how clean URL redirects and CSP directives are enforced.</li>
</ul>
</div>
<div class="lab-box security-disclosure">
<h3>Module 3.5: Responsible Disclosure (RFC 9116)</h3>
<p>Understand how to communicate with security researchers using the <code>security.txt</code> standard on static sites.</p>
<ul>
<li><strong>Objective:</strong> Learn to establish a secure, machine-readable protocol for reporting bugs.</li>
<li><strong>Exercise:</strong> Access the statically compiled <code>/.well-known/security.txt</code> file in your browser to verify configuration.</li>
</ul>
</div>
</section>

<section class="module">
<h2>🧪 Laboratory Module 4: Automated Testing & Verification</h2>
<p>Master automated verification of your static Astro pages using <strong>Playwright</strong> visual verification and headless integration tests.</p>
<div class="exercise">
<h3>Exercise: Visual Regressions</h3>
<p>Run end-to-end integration assertions to verify that all pages render correctly and layout grids are perfectly preserved across viewports.</p>
<p><a href="/lab-module4" class="btn">📝 Open Student Worksheet: Module 4</a></p>
</div>
<p><strong>Concept: "Automated Peace of Mind"</strong>—if the build or integration assertions fail, the code is not ready for deployment.</p>
</section>

<section class="module">
<h2>📊 Laboratory Module 5: Test Coverage and Build QA</h2>
<p>Learn to validate the compiled output directory (<code>dist/</code>) and verify Progressive Web App (PWA) cache readiness.</p>
<div class="exercise">
<h3>Exercise: PWA Offline Auditing</h3>
<p>Verify that your `@vite-pwa/astro` integration generates a proper service worker and offline fallback assets.</p>
<p><a href="/lab-module5" class="btn">📝 Open Student Worksheet: Module 5</a></p>
</div>
</section>

<section class="module ai-module">
<h2>🤖 Laboratory Module 6: AI-Assisted Static Workflows</h2>
<p>Learn to guide an AI agent (such as Google Jules) as your development partner. Master prompt-to-product static engineering.</p>
<div class="exercise">
<h3>Exercise 6.1: The Agentic Challenge</h3>
<p>Instruct an AI agent to build a new page. Review its implementation plan, verify compiled output, and run static compliance checks.</p>
<p><a href="/ai-dev" class="btn">🚀 Open AI Dev Guide</a></p>
</div>
<div class="exercise">
<h3>Exercise 6.2: AI Ethics & Responsible Usage</h3>
<p>Study the standard operating procedures for ethical AI development within static workspaces.</p>
<ul>
<li>Read the <a href="/ai-sop">📜 AI Ethics SOP</a> to understand cognitive rules and the "Trust but Verify" paradigm.</li>
<li><strong>Verification Loop:</strong> Always run a static compiler check (<code>npm run build</code>) on any AI-generated adjustments before merging.</li>
</ul>
</div>
</section>

<section class="module exam-module">
<h2>🚩 The Final Exam: Break-Fix Challenge</h2>
<p>The ultimate test of a static front-end engineer. Repair a broken configuration or schema mapping to pass the compilation test.</p>
<div class="exercise">
<h3>Challenge: Repair the Static Build</h3>
<p>You must fix schema violations and layout configurations to allow the static site to compile successfully.</p>
<p><a href="/final-exam" class="btn">🚀 Start the Final Exam</a></p>
</div>
</section>

<hr>

<section class="case-study">
<h2>📝 The History of CMSForNerd2: A Modernisation Case Study</h2>
<p>CMSForNerd2 represents a complete <strong>Modernisation Journey</strong>.</p>
<ol>
<li><strong>Phase 1:</strong> Transitioned the 2005 database-free procedural PHP codebase into an Astro Static Site Generator (SSG) framework.</li>
<li><strong>Phase 2:</strong> Ported the layout files into clean, scoped <code>Layout.astro</code> components utilizing modern CSS Grid and custom variables.</li>
<li><strong>Phase 3:</strong> Modernised flat-file content fragments into type-safe Markdown/MDX Content Collections under Zod schema rules.</li>
<li><strong>Phase 4:</strong> Replaced the legacy dynamic AJAX PHP router with client-side routing and PWA caching via `@vite-pwa/astro`.</li>
<li><strong>Phase 5:</strong> Enforced static containerisation and unprivileged NGINX serving configurations.</li>
</ol>
<div class="graduation-cta">
<h3>🎓 Ready to Graduate?</h3>
<p>If you have completed all modules and passed the static compilation and QA audits, you are ready to claim your certificate.</p>
<p><a href="/graduation" class="btn graduation-btn">🏁 Claim Your Certificate of Completion</a></p>
</div>
<p class="motto"><strong>Educational Motto:</strong> "Static modernisation without loss of simplicity." — Harisfazillah Jamel & Gemini, 2026.</p>
</section>
</article>

<style>
.graduation-cta { background: #fffbeb; border: 2px solid #fde68a; padding: 2rem; border-radius: 8px; text-align: center; margin: 2rem 0; }
.graduation-cta h3 { color: #92400e; margin-top: 0; }
.graduation-btn { background: #10b981; color: #fff; font-size: 1.2rem; padding: 1rem 2rem; }
.graduation-btn:hover { background: #059669; }
</style>

<style>
.lab-manual h1 { color: #004d00; border-bottom: 2px solid #004d00; padding-bottom: 0.5rem; }
.lab-manual h2 { color: #006600; margin-top: 2rem; border-left: 5px solid #006600; padding-left: 10px; }
.lab-manual section { margin-bottom: 3rem; background: #fff; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
.lab-manual .intro { font-size: 1.1rem; color: #333; line-height: 1.6; background: #e6f7ff; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #007bff; }
.lab-manual .exercise, .lab-manual .lab-box { background: #f9f9f9; padding: 1rem; border-radius: 4px; border: 1px solid #ddd; margin: 1rem 0; }
.lab-manual .exercise h3, .lab-manual .lab-box h3 { margin-top: 0; color: #d9534f; }
.lab-manual .motto { text-align: center; font-style: italic; font-size: 1.2rem; color: #555; margin-top: 2rem; }
.lab-manual hr { border: 0; border-top: 2px dashed #ccc; margin: 3rem 0; }
</style>