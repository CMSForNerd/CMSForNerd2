---
okf_version: 0.1
type: "content_page"
title: "Official Answer Key: Final Exam | CMSForNerd2"
description: "Instructor grading rubric and official static build solutions for the CMSForNerd2 Final Exam."
schemaType: "EducationalOccupationalCredential"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="exam-answers">
<header class="answers-header">
<h1>✅ Official Answer Key: Final Exam</h1>
<p class="subtitle">CMSForNerd2 Static Modernisation Curriculum</p>
</header>

<div class="answers-intro">
<p>
Use this <strong>Official Answer Key</strong> to verify student submissions.
Solutions MUST resolve static compile-time conflicts, satisfy Zod metadata validation, and maintain
<strong>Strict Type Safety</strong>.
</p>
</div>

<section class="answer-section">
<h2>✅ Answer 1: Zod Schema Frontmatter Validation</h2>
<p><strong>Requirement:</strong> Add the missing mandatory <code>okf_version</code> to restore schema compliance.</p>
<div class="code-block fixed">
<pre><code>---
okf_version: "0.1" # Fixed: Added the missing mandatory OKF version
type: content_page
title: "New Student Article"
description: "Short guide."
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation"]
---</code></pre>
</div>
</section>

<section class="answer-section">
<h2>✅ Answer 2: YAML Compliant Indentation</h2>
<p><strong>Requirement:</strong> Replace illegal tab characters with standard YAML spaces.</p>
<div class="code-block fixed">
<pre><code>---
okf_version: 0.1
type: content_page
title: "Windows Guides"
topics:
  - "modernisation" # Fixed: Indented with 2 spaces instead of tabs
  - "setup"
---</code></pre>
</div>
</section>

<section class="answer-section">
<h2>✅ Answer 3: Enforcing Strict Content Security Policy</h2>
<p><strong>Requirement:</strong> Restrict script directives to avoid open script execution.</p>
<div class="code-block fixed">
<pre><code># Fixed NGINX Security Configuration
add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://challenges.cloudflare.com; style-src 'self' 'unsafe-inline';" always;</code></pre>
</div>
</section>

<section class="answer-section">
<h2>✅ Answer 4: TypeScript Props Typing</h2>
<p><strong>Requirement:</strong> Pass a string title instead of a number to comply with standard layout TS interfaces.</p>
<div class="code-block fixed">
<pre><code>&lt;Layout title="2026"&gt;
  &lt;p&gt;Static page content.&lt;/p&gt;
&lt;/Layout&gt;</code></pre>
</div>
</section>

<section class="answer-section">
<h2>✅ Answer 5: PWA Service Worker Route Falling</h2>
<p><strong>Requirement:</strong> Configure workbox navigation fallbacks to reference the compiled static offline path.</p>
<div class="code-block fixed">
<pre><code>AstroPWA({
  workbox: {
    navigateFallback: '/offline/index.html' # Fixed: Configured the correct offline target
  }
})</code></pre>
</div>
</section>

<footer class="grading-rubric">
<h2>🎓 Certification Rubric</h2>
<ul>
<li><strong>MUST:</strong> Pass compilation with zero errors under <code>npm run build</code>.</li>
<li><strong>MUST:</strong> Register a valid service worker with offline fallback support.</li>
<li><strong>SHOULD:</strong> Leverage OKF v0.1 compliant frontmatter on all newly authored pages.</li>
</ul>
</footer>
</article>

<style>
:root { --exam-green: #28a745; --exam-gold: #92400e; }
.exam-answers { max-width: 850px; margin: 0 auto; line-height: 1.8; }
.answers-header { text-align: center; border-bottom: 3px double var(--exam-green); padding-bottom: 20px; }
.answers-intro { background: #f0fdf4; border-left: 5px solid var(--exam-green); padding: 20px; border-radius: 8px; }
.answer-section { margin: 40px 0; }
.code-block { background: #1a1a1a; color: #f8f8f2; padding: 20px; border-radius: 6px; font-family: 'Courier New', monospace; border-left: 5px solid var(--exam-green); overflow-x: auto; }
.grading-rubric { background: #fffbeb; border: 2px solid #fde68a; padding: 30px; border-radius: 12px; margin-top: 50px; }
.grading-rubric h2 { color: var(--exam-gold); margin-top: 0; }
</style>