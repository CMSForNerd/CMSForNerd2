---
okf_version: 0.1
type: "content_page"
title: "New Page Creation Guide | CMSForNerd2"
description: "A step-by-step guide to authoring new content pages using Markdown/MDX and Astro 7.1 Content Collections."
schemaType: "WebPage"
author: "Harisfazillah Jamel"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="template-guide">
<h1>🎨 CMSForNerd2 Page Creation Guide</h1>
<p class="subtitle">Mastering Content Collections & Frontmatter Validation</p>

<div class="intro-box">
<p>
In CMSForNerd2, page creation is completely declarative. Instead of managing complex controller files or PHP scripts, you simply write **Markdown (.md) or MDX (.mdx) files** inside our content collection folder. Astro's compiler reads your frontmatter metadata and renders pages statically through a unified layout wrapper.
</p>
</div>

<section class="guide-step">
<h2>📂 Step 1: Locate the Folders</h2>
<p>Focus on these key areas in the Astro development environment:</p>
<ul>
<li><strong>Content Collection:</strong> <code>src/content/pages/</code> — Place all page files here.</li>
<li><strong>Page Routing:</strong> <code>src/pages/[...slug].astro</code> — Astro's routing loader that automatically discovers your markdown files.</li>
<li><strong>Zod Config:</strong> <code>src/content.config.ts</code> — Configures the schema schemas that validate your frontmatter.</li>
</ul>
</section>

<section class="guide-step">
<h2>📝 Step 2: Create Your Content (.md or .mdx file)</h2>
<p>Write your page content using semantic HTML or Markdown elements.</p>
<ol>
<li>Create a new file inside <code>src/content/pages/</code> (e.g., <code>contact.md</code>).</li>
<li><strong>Naming Rule:</strong> Filenames should be lowercase and hyphen-separated (e.g., <code>contact-us.md</code>).</li>
<li>Write your content using standard Markdown syntax, semantic headings, tables, or inline blocks.</li>
</ol>
<div class="code-example">
<h3>Example: <code>src/content/pages/contact.md</code></h3>
<pre><code>---
okf_version: 0.1
type: content_page
title: "Contact Us | CMSForNerd2"
description: "Reach out to the Astro modernisation laboratory admins."
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "contact"]
---

&lt;section class="contact-page"&gt;
# Contact Us
Send a message to our static development team.
&lt;/section&gt;</code></pre>
</div>
</section>

<section class="guide-step">
<h2>🚀 Step 3: Frontmatter Schema Properties</h2>
<p>In CMSForNerd2, the compiler validates frontmatter variables at build time to prevent broken pages or missing SEO attributes.</p>

<div class="instruction-box">
<p><strong>Required YAML Fields:</strong></p>
<ul>
<li><code>okf_version</code>: Open Knowledge Format specification (MUST be <code>"0.1"</code> or <code>0.1</code>).</li>
<li><code>type</code>: Document class type (e.g., <code>content_page</code>).</li>
<li><code>title</code>: SEO-friendly title string.</li>
<li><code>description</code>: Meta description tag for search engines.</li>
<li><code>timestamp</code>: Iso Date String (e.g., <code>"2026-07-30T12:00:00Z"</code>).</li>
<li><code>topics</code>: Array list of keywords (e.g., <code>["modernisation", "setup"]</code>).</li>
</ul>
</div>
</section>

<section class="guide-step security-check">
<h2>🛡️ Step 4: Verify Safety & Compliance</h2>
<p>Before submitting your new page, perform these three static compilation checks:</p>
<div class="check-grid">
<div class="check-item">
<h3>1. Type Check</h3>
<p>Run <code>npx tsc --noEmit</code>. Ensure TypeScript throws zero type warnings or property errors.</p>
</div>
<div class="check-item">
<h3>2. Compiles Clean</h3>
<p>Execute <code>npm run build</code>. Check that your new route compiles successfully to static files under <code>dist/</code>.</p>
</div>
<div class="check-item">
<h3>3. Local Preview</h3>
<p>Run <code>npm run preview</code> and visit the generated page in your local browser to confirm layout correctness.</p>
</div>
</div>
</section>

<section class="standards-box">
<h2>⚖️ Laboratory Standards</h2>
<ul>
<li><strong>MUST:</strong> Author YAML blocks using strict spacing; avoid using tab characters.</li>
<li><strong>MUST NOT:</strong> Include raw dynamic runtime server scripts. Keep elements static.</li>
<li><strong>REQUIRED:</strong> Align frontmatter structures exactly with <code>src/content.config.ts</code> Zod validations.</li>
</ul>
</section>
</article>

<style>
.template-guide h1 { color: #8e44ad; border-bottom: 2px solid #8e44ad; padding-bottom: 0.5rem; }
.template-guide .subtitle { font-size: 1.2rem; color: #666; font-weight: bold; margin-bottom: 2rem; }
.template-guide .intro-box { background: #f3e5f5; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #8e44ad; margin-bottom: 2rem; }
.template-guide .instruction-box { background: #fff; padding: 1rem; border: 1px dashed #8e44ad; border-radius: 8px; margin-bottom: 1rem; }
.template-guide .guide-step { margin-bottom: 3rem; }
.template-guide h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; }
.template-guide .code-example { background: #1a1a1a; color: #fff; padding: 1rem; border-radius: 8px; margin: 1rem 0; }
.template-guide .code-example h3 { color: #e1bee7; margin-top: 0; font-size: 0.9rem; text-transform: uppercase; }
.template-guide .code-example pre { margin: 0; white-space: pre-wrap; word-break: break-all; }
.template-guide .code-example code { font-family: 'Consolas', monospace; color: #f0f0f0; }
.template-guide .security-check { background: #fff3e0; padding: 1.5rem; border-radius: 8px; border: 1px solid #ffe0b2; }
.template-guide .check-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem; }
.check-item { background: white; padding: 1rem; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
.check-item h3 { font-size: 1rem; color: #e65100; margin-top: 0; }
.template-guide .standards-box { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; border: 1px solid #ddd; margin-top: 2rem; }
</style>