---
okf_version: 0.1
type: "content_page"
title: "Final Exam: Break-Fix Challenge - CMSForNerd2"
description: "Final Certification Exam. Repair 5 deliberate static site and Astro 7.1 errors to prove mastery of SSG compilation and layout safety."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="final-exam">
<header class="exam-header">
<h1>🚩 The CMSForNerd2 Astro 7.1 Final Exam</h1>
<p class="mission">Mission: Repair the Static Build</p>
</header>

<div class="exam-intro">
<p>
This Final Exam is designed as a <strong>"Break-Fix" challenge</strong>. In the software industry, a developer's job
is frequently to debug build configurations and compile errors. To pass, you must understand how to resolve five deliberate static configuration errors that block successful compilation.
</p>
<div class="scenario-box">
<strong>Scenario:</strong> A developer has checked in a series of content and layout modifications that violated our Zod schema validation rules, triggering build-time compiler failures.
</div>
</div>

<section class="challenge">
<h2>❌ Challenge 1: Broken Content Collection Frontmatter (Module 1/2)</h2>
<p>The following page frontmatter was committed. It triggers a compilation crash because it is missing the mandatory <code>okf_version</code> field required by the Zod schema in <code>src/content.config.ts</code>.</p>
<p><strong>Task:</strong> Add the missing OKF version field to restore schema compliance.</p>
<div class="code-block broken">
<pre><code>---
# BROKEN FRONTMATTER - MISSING MANDATORY FIELD
type: content_page
title: "New Student Article"
description: "Short guide."
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation"]
---</code></pre>
</div>
</section>

<section class="challenge">
<h2>❌ Challenge 2: Broken Frontmatter Syntax (Module 2)</h2>
<p>This page frontmatter throws a YAML parsing error because the developer used tabs for indentation and syntax formatting.</p>
<p><strong>Task:</strong> Replace the incorrect tabs with spaces and ensure valid colon syntax.</p>
<div class="code-block broken">
<pre><code>---
okf_version: 0.1
type: content_page
title: "Windows Guides"
topics:
	- "modernisation" # BROKEN: Indented with a tab character!
	- "setup"
---</code></pre>
</div>
</section>

<section class="challenge">
<h2>❌ Challenge 3: Insecure Static CSP Header (Module 3)</h2>
<p>An insecure Content Security Policy was written in the server configuration, allowing external domains to run arbitrary scripts.</p>
<p><strong>Task:</strong> Restrict <code>script-src</code> to only allow <code>'self'</code> and trusted Cloudflare challenge endpoints.</p>
<div class="code-block broken">
<pre><code># BROKEN NGINX CSP CONFIGURATION
add_header Content-Security-Policy "default-src 'self'; script-src *;" always;</code></pre>
</div>
</section>

<section class="challenge">
<h2>❌ Challenge 4: Type Mismatch in Layout Props (Module 1/4)</h2>
<p>A TypeScript interface expects the page title to be a string, but the developer passed a numeric value, throwing a compilation error.</p>
<p><strong>Task:</strong> Wrap the title property in quotes to enforce strict type-safety.</p>
<div class="code-block broken">
<pre><code>&lt;!-- BROKEN CODE --&gt;
&lt;Layout title={2026}&gt;
  &lt;p&gt;Static page content.&lt;/p&gt;
&lt;/Layout&gt;</code></pre>
</div>
</section>

<section class="challenge">
<h2>❌ Challenge 5: Missing Offline Fallback Target (Module 5)</h2>
<p>The PWA configuration is missing the standard offline asset page, causing offline cached loading to throw a 404 error when disconnected.</p>
<p><strong>Task:</strong> Configure the PWA configuration to include the correct fallback route (<code>/offline/index.html</code>) in the pre-cache block.</p>
<div class="code-block broken">
<pre><code>// BROKEN PWA CACHE CONFIG
AstroPWA({
  workbox: {
    // Missing the offline fallback mapping!
    navigateFallback: null
  }
})</code></pre>
</div>
</section>

<footer class="exam-footer">
<h2>📝 Evaluation Criteria</h2>
<p>A student passes if they can successfully build the statically compiled assets with zero compiler errors:</p>
<div class="terminal-block">
<code>npm run build</code>
</div>
<div class="graduation-cta">
<h3>🎓 Ready to Submit?</h3>
<p>Once you have resolved all five build challenges and verified a clean compilation report, go to the Graduation page!</p>
<p><a href="/graduation" class="btn exam-btn">🏁 Go to Graduation</a></p>
</div>
</footer>

<nav class="progress-nav">
<a href="/lab-module5" class="btn prev">&lt; Previous: Module 5 (Coverage &amp; QA)</a>
<a href="/graduation" class="btn next">Go to Graduation &gt;</a>
</nav>
</article>

<style>
.final-exam h1 { color: #d9534f; border-bottom: 2px solid #d9534f; padding-bottom: 0.5rem; }
.final-exam .exam-header { text-align: center; margin-bottom: 3rem; }
.final-exam .mission { font-size: 1.5rem; font-weight: bold; color: #333; text-transform: uppercase; letter-spacing: 2px; }
.final-exam .exam-intro { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #d9534f; margin-bottom: 3rem; }
.final-exam .scenario-box { margin-top: 1rem; font-style: italic; color: #555; }
.final-exam h2 { color: #333; margin-top: 3rem; }
.final-exam .code-block { background: #1a1a1a; padding: 1.5rem; border-radius: 4px; margin: 1rem 0; box-shadow: inset 0 0 10px rgba(0,0,0,0.5); }
.final-exam .code-block pre { color: #f8f8f2; margin: 0; }
.final-exam .code-block.broken { border-left: 5px solid #d9534f; }
.final-exam .terminal-block { background: #000; color: #00ff00; padding: 1rem; font-family: 'Consolas', monospace; border-radius: 4px; margin: 1rem 0; }
.final-exam .graduation-cta { background: #fffbeb; border: 2px solid #fde68a; padding: 2rem; border-radius: 8px; text-align: center; margin-top: 4rem; }
.final-exam .exam-btn { background: #d9534f; color: #fff; text-decoration: none; padding: 1rem 2rem; border-radius: 4px; font-weight: bold; display: inline-block; }
.final-exam .exam-btn:hover { background: #c9302c; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #d9534f; color: #fff; }
@media (max-width: 768px) { .progress-nav { flex-direction: column; gap: 1rem; } }
</style>