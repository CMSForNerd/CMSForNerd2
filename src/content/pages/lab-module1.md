---
okf_version: 0.1
type: "content_page"
title: "Lab Worksheet: Module 1 - CMSForNerd2"
description: "Module 1: Master Astro 7.1 Component Frontmatter, Layouts, and strict TypeScript compilation."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet">
<h1>Student Lab Worksheet: Module 1</h1>
<p class="subtitle">Topic: Astro 7.1 Component Architecture & Type-Safety</p>

<div class="requirement-alert">
<strong>Requirement Level:</strong> Students <strong>MUST</strong> implement strict component frontmatter properties and validate them against strict TypeScript definitions to pass the "Code Elegance" audit.
</div>

<section class="objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li>Eliminate runtime processing using **Build-Time Component Frontmatter** (code fences).</li>
<li>Master **Astro Layouts** and static slot injection to maintain clean, modular templates.</li>
<li>Understand **Strict TypeScript Type-Safety** for frontmatter parameters.</li>
</ul>
</section>

<section class="step">
<h2>🛠️ Step 1: Component Frontmatter (Code Fences)</h2>
<p>In legacy PHP, variables had to be declared and initialized during every page load. In Astro 7.1, we define a code fence (<code>---</code>) containing JS/TS that runs <strong>exclusively at build-time</strong> to compile static pages.</p>
<p><strong>Task:</strong> Refactor a metadata assignment. Observe how Astro executes this logic at compilation time, generating pure, static HTML with zero client-side overhead.</p>
<div class="code-compare">
<div class="old">
<h3>Legacy PHP Controller</h3>
<pre><code>&lt;?php
declare(strict_types=1);
$pageTitle = "About Us";
$theme = "dark";
include "themes/header.php";
?&gt;</code></pre>
</div>
<div class="new">
<h3>Astro 7.1 Frontmatter</h3>
<pre><code>---
// src/pages/about.astro
import Layout from '../layouts/Layout.astro';
const pageTitle = "About Us";
const theme = "dark";
---
&lt;Layout title={pageTitle} theme={theme}&gt;
  &lt;p&gt;Static content rendered directly.&lt;/p&gt;
&lt;/Layout&gt;</code></pre>
</div>
</div>
</section>

<section class="step">
<h2>🧪 Step 2: Astro Layouts and Slot Injection</h2>
<p>Astro separates top-level templates from content pages using Layout components and the special <code>&lt;slot /&gt;</code> element.</p>
<div class="exercise">
<h3>Exercise 1.1: Standard Layout Integration</h3>
<p>Inspect <code>src/layouts/Layout.astro</code> and notice how page elements are rendered around the slot placeholder:</p>
<div class="code-block modern">
<pre><code>---
// src/layouts/Layout.astro
interface Props {
  title: string;
}
const { title } = Astro.props;
---
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;{title}&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt;Header&lt;/header&gt;
    &lt;main&gt;
      &lt;slot /&gt; &lt;!-- Page content is injected here --&gt;
    &lt;/main&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
</div>
</section>

<section class="step">
<h2>🔐 Step 3: TypeScript and Schema Validation</h2>
<p>This is a major upgrade for static reliability. In Astro 7.1, page schemas are defined using **Zod validation schemas** inside <code>src/content.config.ts</code>.</p>
<div class="exercise">
<h3>Exercise 1.2: Content Collections Schema Challenge</h3>
<ul>
<li>Explore your content schema definition. It mandates that every page have a <code>title</code>, <code>description</code>, <code>timestamp</code>, and <code>topics</code>.</li>
<li><strong>The Test:</strong> Try deleting a required property from a page's frontmatter and run the compiler. It will block compilation, safeguarding against broken structures!</li>
</ul>
<div class="code-block modern">
<pre><code>// src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pages = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/pages" }),
  schema: z.object({
    okf_version: z.string(),
    type: z.string(),
    title: z.string(),
    description: z.string(),
    timestamp: z.string(),
    topics: z.array(z.string())
  })
});</code></pre>
</div>
</div>
</section>

<section class="step">
<h2>✅ Step 4: Verification (The Static Compiler Audit)</h2>
<p>Run the Astro static build check to confirm type-safety across all compiled files:</p>
<div class="terminal-block">
<code>npm run build</code>
</div>
<div class="question-box">
<p><strong>Question for the Student:</strong> Why does build-time schema validation provide a safer environment than legacy run-time checks?</p>
<p class="hint">(Hint: Think about when a schema mistake is caught by developers versus when it affects an active website visitor).</p>
</div>
</section>

<footer class="standards-summary">
<h2>🎓 Summary of RFC 2119 Standards for Module 1</h2>
<ul>
<li><strong>MUST:</strong> Every page Markdown file carried in content collections **MUST** match the Zod schema configuration.</li>
<li><strong>SHOULD:</strong> Define explicit interface properties (<code>Props</code>) for all Astro layout files.</li>
<li><strong>MAY:</strong> Utilise custom TS types to support advanced helper components.</li>
</ul>
</footer>

<nav class="progress-nav">
<a href="/welcome-kit" class="btn prev">&lt; Back to Welcome Kit</a>
<a href="/lab-module2" class="btn next">Next: Module 2 (Standards) &gt;</a>
</nav>
</article>

<style>
.lab-worksheet h1 { color: #007bff; margin-bottom: 0.1rem; }
.lab-worksheet .subtitle { font-size: 1.2rem; color: #777; margin-bottom: 2rem; }
.lab-worksheet .requirement-alert { background: #dff0d8; border: 1px solid #d6e9c6; color: #3c763d; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }
.lab-worksheet h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; margin-top: 2rem; }
.lab-worksheet .code-compare { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0; }
.lab-worksheet .code-compare .old, .lab-worksheet .code-compare .new { background: #f8f9fa; padding: 1rem; border-radius: 4px; border: 1px solid #ddd; }
.lab-worksheet .code-compare pre { margin: 0; font-size: 0.85rem; }
.lab-worksheet .exercise { background: #f9f9f9; padding: 1rem; border-radius: 4px; border: 1px solid #ddd; margin: 1rem 0; }
.lab-worksheet .code-block { background: #2d2d2d; color: #ccc; padding: 1rem; border-radius: 4px; overflow-x: auto; margin: 1rem 0; }
.lab-worksheet .code-block.modern { border-left: 5px solid #007bff; }
.lab-worksheet .terminal-block { background: #000; color: #00ff00; padding: 1rem; font-family: 'Courier New', Courier, monospace; border-radius: 4px; margin: 1rem 0; }
.lab-worksheet .question-box { background: #fff3cd; border: 1px solid #ffeeba; color: #856404; padding: 1rem; border-radius: 4px; margin: 2rem 0; }
.lab-worksheet .standards-summary { margin-top: 3rem; background: #f5f5f5; padding: 1.5rem; border-radius: 8px; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #007bff; color: #fff; }
@media (max-width: 768px) { .lab-worksheet .code-compare { grid-template-columns: 1fr; } .progress-nav { flex-direction: column; gap: 1rem; } }
</style>