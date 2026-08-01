---
okf_version: 0.1
type: content_page
title: "CMSForNerd2 | The Static Modernisation Laboratory"
description: "A lightweight, database-free CMS modernised using Astro 7.1 Static Site Generator (SSG) with strict TypeScript standards."
schemaType: "WebApplication"
author: "Harisfazillah Jamel"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-home">
<header class="hero-section">
<h1>Welcome to CMSForNerd2: The Astro 7.1 Static Modernisation Laboratory</h1>
<div class="runtime-status">
<span class="badge astro-version">Astro 7.1</span>
<span class="badge status-strict">TypeScript: Strict</span>
<span class="badge status-check">Vite: v6/v8</span>
<span class="badge status-sec">PWA: Enabled</span>
</div>
</header>

<div class="intro-box">
<p>
<strong>CMSForNerd2</strong> is a state-of-the-art static modernisation of the legacy database-free PHP CMS.
By utilizing <strong>Astro 7.1 Static Site Generator (SSG)</strong>, this workspace compiles your content to purely static, high-performance HTML5, CSS3, and ES6+ JavaScript.
While frameworks often hide complexity, we expose it—teaching you to master modern static workflows, type-safe content collections, and zero-JS-by-default architecture.
</p>
<div class="quick-links">
<a href="/welcome-kit" class="btn welcome-btn">🚀 Welcome Kit</a>
<a href="/lab-manual" class="btn lab-btn">🎓 Lab Manual</a>
<a href="/template" class="btn guide-btn">🎨 Template Guide</a>
<a href="/ui-kit" class="btn audit-btn">🧪 UI Audit</a>
</div>
</div>

<section class="grid-features">
<div class="feature-card">
<h3>🛡️ Static Security Engineering</h3>
<ul>
<li><strong>No Server-Side Vulnerabilities:</strong> Absolute immunity to LFI, Directory Traversal, and SQL injection since there is no server execution.</li>
<li><strong>Static Content Security Policy:</strong> Build-time CSP header definitions and Subresource Integrity (SRI) to neutralize XSS.</li>
<li><strong>Immutable State:</strong> Type-safe data schema structures validated at compile-time by Zod.</li>
<li><strong>Hardened Container:</strong> Production-ready unprivileged NGINX server Alpine container.</li>
</ul>
</div>

<div class="feature-card">
<h3>🚀 Modern SSG Standards</h3>
<ul>
<li><strong>"Component Frontmatter" Architecture:</strong> Build-time JS/TS executing solely during compilation to render clean HTML.</li>
<li><strong>Type-Safe Content:</strong> Rigid frontmatter schemas checked by Astro's Content Collections compiler.</li>
<li><strong>SEO & AI Ready:</strong> Complete integration with RSS, XML Sitemaps, and Schema.org JSON-LD structured metadata.</li>
<li><strong>PWA Resiliency:</strong> Instant offline fallback loading via <code>@vite-pwa/astro</code> service worker integration.</li>
</ul>
</div>
</section>

<section class="lab-workflow">
<h3>The Astro 7.1 Secure Static Workflow</h3>
<div class="workflow-steps">
<div class="step">
<span class="step-num">1</span>
<h4>The Page</h4>
<p>Create or duplicate a <code>.md</code> page in <code>src/content/pages/</code>.</p>
</div>
<div class="step">
<span class="step-num">2</span>
<h4>The Frontmatter</h4>
<p>Configure metadata validating against Zod schemas in <code>src/content.config.ts</code>.</p>
</div>
<div class="step">
<span class="step-num">3</span>
<h4>The Build</h4>
<p>Compile static assets using <code>npm run build</code> and preview locally with <code>npm run preview</code>.</p>
</div>
</div>
</section>

<section class="stack-recommendation">
<h3>Optimised Learning Stack</h3>
<table class="stack-table">
<tr>
<td><strong>Runtime/Framework</strong></td>
<td>Astro 7.1 (using Node.js 20+ and static output)</td>
</tr>
<tr>
<td><strong>Standards</strong></td>
<td>Open Knowledge Format (OKF) v0.1, TypeScript, strict schema validation</td>
</tr>
<tr>
<td><strong>OS Support</strong></td>
<td>Cross-platform (Debian/Ubuntu Linux, Windows 11, macOS)</td>
</tr>
<tr>
<td><strong>Dev Tools</strong></td>
<td>npm, Astro CLI, Vite, VS Code, Playwright, Git</td>
</tr>
</table>
</section>
</article>

<style>
.lab-home { max-width: 1000px; margin: 0 auto; line-height: 1.6; font-family: var(--f-sans, sans-serif); }
.hero-section h1 { color: var(--lab-heading, #2c3e50); border-bottom: 4px solid var(--lab-purple, #8e44ad); padding-bottom: 10px; margin-bottom: 10px; }

.runtime-status { margin-bottom: 25px; }
.badge { display: inline-block; padding: 4px 12px; border-radius: 4px; font-size: 0.85rem; font-weight: bold; margin-right: 5px; }
.astro-version { background: #FF5D01; color: white; }
.status-strict { background: #27ae60; color: white; }
.status-check { background: #f39c12; color: white; }
.status-sec { background: #8e44ad; color: white; }

.intro-box { background: var(--lab-surface, #f4f7f6); border: 1px solid var(--lab-border, #e2e8f0); color: var(--lab-text); padding: 30px; border-radius: 12px; border-left: 6px solid var(--lab-purple, #8e44ad); margin-bottom: 40px; }
.quick-links { margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap; }

.btn { padding: 12px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; color: white; transition: all 0.2s ease; font-size: 0.9rem; }
.welcome-btn { background: #2980b9; }
.lab-btn { background: #c0392b; }
.guide-btn { background: #8e44ad; }
.audit-btn { background: #2c3e50; }
.btn:hover { filter: brightness(1.1); transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.1); }

.grid-features { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; margin-bottom: 40px; }
.feature-card { background: var(--lab-surface, white); border: 1px solid var(--lab-border, #e2e8f0); color: var(--lab-text); padding: 25px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
.feature-card h3 { color: var(--lab-heading, #2c3e50); margin-top: 0; border-bottom: 1px solid var(--lab-border, #eee); padding-bottom: 10px; }
.feature-card ul { padding-left: 20px; }
.feature-card li { margin-bottom: 8px; font-size: 0.95rem; }

.lab-workflow { background: #0f172a; color: white; padding: 30px; border-radius: 12px; margin-bottom: 40px; }
.workflow-steps { display: flex; justify-content: space-around; gap: 20px; margin-top: 20px; text-align: center; }
.step-num { background: #8e44ad; width: 40px; height: 40px; display: block; margin: 0 auto 10px; border-radius: 50%; line-height: 40px; font-weight: bold; font-size: 1.2rem; }
.step h4 { margin-bottom: 5px; color: #ecf0f1; }
.step p { font-size: 0.85rem; color: #bdc3c7; }

.stack-table { width: 100%; border-collapse: collapse; background: var(--lab-surface, white); border-radius: 8px; overflow: hidden; border: 1px solid var(--lab-border, #e2e8f0); color: var(--lab-text); }
.stack-table td { padding: 15px; border: 1px solid var(--lab-border, #eee); }
.stack-table tr td:first-child { background: var(--lab-bg, #f9f9f9); width: 30%; font-weight: bold; color: var(--lab-muted, #64748b); font-size: 0.9rem; }
</style>
