---
okf_version: 0.1
type: "content_page"
title: "Lab Worksheet: Module 2 - CMSForNerd2"
description: "Module 2: Code Standards and Frontmatter Compliance. Learn to use Prettier, TypeScript validation, and OKF format rules."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet">
<h1>🎨 Student Lab Worksheet: Module 2</h1>
<p class="subtitle">Topic: Frontmatter Compliance & Code Formatting Standards</p>

<div class="requirement-alert">
<strong>Requirement Level:</strong> Students <strong>MUST</strong> pass a zero-error static compilation and structure validation audit to achieve compliant status.
</div>

<section class="objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li>Recognize clean page frontmatter structures and TypeScript standards.</li>
<li>Automate code formatting using <strong>Prettier</strong>.</li>
<li>Integrate YAML metadata verification into your developer workflow.</li>
</ul>
</section>

<section class="step">
<h2>🛠️ Step 1: The "Frontmatter Layout" Test</h2>
<p>Before using tools, students must understand the structure of a clean Markdown/MDX layout in Astro. In CMSForNerd2, every content page requires structured frontmatter at the top of the file.</p>
<p><strong>Common Violations to spot:</strong></p>
<ul>
<li>Missing or incorrectly formatted code fences (<code>---</code>).</li>
<li>Using tabs instead of 4 spaces in YAML metadata blocks.</li>
<li>Leaving out mandatory metadata properties, such as the <code>okf_version</code> string.</li>
</ul>
</section>

<section class="step">
<h2>🧪 Step 2: The Automated Type Check</h2>
<p>Rather than manually inspecting every page, we use the <strong>TypeScript compiler (tsc)</strong> coupled with Astro's content schema loader to validate all documents.</p>
<p><strong>Task:</strong> Run a content collection compilation check on your current workspace.</p>
<div class="terminal-block">
<code>npm run build</code>
</div>
<p><strong>Observation:</strong> If any page has a mismatching property, the build script will immediately emit descriptive validation warnings or errors, pinpointing the file and line number.</p>
</section>

<section class="step">
<h2>🪄 Step 3: The Automated Formatter (Prettier)</h2>
<p>Professional front-end engineers do not adjust margins or formatting manually. We use <strong>Prettier</strong> to format standard files (<code>.json</code>, <code>.md</code>, <code>.astro</code>).</p>
<p><strong>Task:</strong> Format your source files instantly.</p>
<div class="terminal-block">
<code>npx prettier --write "src/**/*.{astro,md,json}"</code>
</div>
<p><strong>Observation:</strong> This command automatically reformats trailing commas, margins, indentation, and spacings to ensure total stylistic consistency across all pages.</p>
</section>

<section class="step">
<h2>🧩 Step 4: Open Knowledge Format (OKF) Compliance</h2>
<p>All pages in our CMS must carry an Open Knowledge Format (OKF) v0.1 compliant frontmatter block.</p>
<p><strong>Exercise:</strong> Ensure every Markdown file in your <code>src/content/pages/</code> folder carries this exact structural sequence:</p>
<ol>
<li>An opening <code>---</code> code fence.</li>
<li><code>okf_version: 0.1</code> declaration.</li>
<li><code>type: content_page</code> (or other appropriate OKF doc type).</li>
<li><code>title</code>, <code>description</code>, and <code>timestamp</code> properties.</li>
<li>A list of <code>topics: [...]</code> defining keywords.</li>
<li>A closing <code>---</code> code fence.</li>
</ol>
</section>

<footer class="standards-summary">
<h2>🎓 Summary of Standards for Module 2</h2>
<ul>
<li><strong>MUST:</strong> Strictly utilize 2 spaces or 4 spaces consistently for indentation in YAML. Never mix them.</li>
<li><strong>MUST:</strong> Complete all required Zod schema properties defined in <code>src/content.config.ts</code>.</li>
<li><strong>SHOULD:</strong> Keep paragraphs concise and structured within semantic HTML elements.</li>
</ul>
<div class="question-box">
<p><strong>Question for the Student:</strong> Why does separating frontmatter metadata from the page layout body help with automation and content parsing?</p>
<p class="hint">(Hint: Think about how easy it is for an automated parser to read structured JSON/YAML versus parsing raw paragraphs of text).</p>
</div>
</footer>

<nav class="progress-nav">
<a href="/lab-module1" class="btn prev">&lt; Previous: Module 1 (Architecture)</a>
<a href="/lab-module3" class="btn next">Next: Module 3 (Defensive Engineering) &gt;</a>
</nav>
</article>

<style>
.lab-worksheet h1 { color: #6f42c1; margin-bottom: 0.1rem; }
.lab-worksheet .subtitle { font-size: 1.2rem; color: #777; margin-bottom: 2rem; }
.lab-worksheet .requirement-alert { background: #f3e5f5; border: 1px solid #d1c4e9; color: #4527a0; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }
.lab-worksheet h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; margin-top: 2rem; }
.lab-worksheet .terminal-block { background: #1e1e1e; color: #d4d4d4; padding: 1rem; font-family: 'Consolas', 'Monaco', monospace; border-radius: 4px; margin: 1rem 0; border-left: 5px solid #6f42c1; }
.lab-worksheet .terminal-block code { color: #00ff00; }
.lab-worksheet .question-box { background: #e8f5e9; border: 1px solid #c8e6c9; color: #2e7d32; padding: 1rem; border-radius: 4px; margin: 2rem 0; }
.lab-worksheet .standards-summary { margin-top: 3rem; background: #f5f5f5; padding: 1.5rem; border-radius: 8px; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #6f42c1; color: #fff; }
@media (max-width: 768px) { .progress-nav { flex-direction: column; gap: 1rem; } }
</style>