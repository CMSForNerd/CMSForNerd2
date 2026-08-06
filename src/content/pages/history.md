---
okf_version: 0.1
type: "content_page"
title: "Modernisation History | CMSForNerd2 Evolution"
description: "Tracking the journey of CmsForNerd from a 2005 dynamic core to a 2026 Astro 7.1 static powerhouse."
schemaType: "ArchiveComponent"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="modernization-history">
<header class="history-header">
<h1>Modernisation History: From dynamic PHP to Astro 7.1</h1>
<p class="intro">
Starting in 2025, CmsForNerd underwent a radical transformation. This timeline tracks the shift from a 20-year-old dynamic flat-file PHP core to a modern, type-safe, static-first Astro 7.1 architecture (CMSForNerd2).
</p>
</header>

<div class="timeline">
<section class="version-block v20">
<div class="version-tag">v2.0.0</div>
<h2>Astro 7.1 Static Modernisation (Current)</h2>
<p><strong>Focus:</strong> Astro 7.1 SSG, Content Collections, and offline-first Progressive Web App capabilities.</p>
<ul>
<li><strong>Static Site Generation (SSG):</strong> Compiled layouts, markdown collections, and styles directly into optimized HTML5/CSS3 assets.</li>
<li><strong>Type-Safe Content:</strong> Enforced Zod schemas for page metadata validation inside <code>src/content.config.ts</code>.</li>
<li><strong>PWA Resiliency:</strong> Configured <code>@vite-pwa/astro</code> for automatic service worker caching and offline fallbacks.</li>
<li><strong>Hardened Hosting:</strong> Configured dual-view AMP paths statically and packaged the workspace in unprivileged NGINX Alpine containers.</li>
</ul>
</section>

<section class="version-block v35">
<div class="version-tag">v1.5.0</div>
<h2>Legacy PHP 8.4 Engine</h2>
<p><strong>Focus:</strong> Property Hooks, strict typing, and defensive routing in PHP.</p>
<ul>
<li><strong>Object-Oriented Core:</strong> Replaced dynamic global states with strict <code>CmsContext</code> models.</li>
<li><strong>Property Hooks:</strong> Utilized PHP 8.4 hooks for data formatting and sanitization.</li>
<li><strong>Standards & QA:</strong> Enforced PSR-12 and strict PHPUnit unit testing, reaching over 90% code coverage.</li>
</ul>
</section>
</div>

<footer class="history-footer">
<p><em>"Refining the past to secure the future."</em> — LinuxMalaysia & Google Gemini, 2026.</p>
</footer>
</article>

<style>
:root { --v20-color: #007bff; --v35-color: #e67e22; --bg-gray: #f9f9f9; }
.modernization-history { max-width: 900px; margin: 0 auto; line-height: 1.8; }
.history-header { text-align: center; margin-bottom: 50px; }
.history-header h1 { color: #2c3e50; font-size: 2.4rem; border-bottom: 3px solid var(--v20-color); display: inline-block; }
.intro { background: var(--bg-gray); padding: 20px; border-left: 5px solid #ccc; font-style: italic; }

.timeline { position: relative; padding: 20px 0; }
.version-block { margin-bottom: 40px; padding: 25px; border-radius: 12px; background: #fff; border: 1px solid #eee; position: relative; }
.version-tag { position: absolute; top: -15px; right: 20px; padding: 5px 15px; border-radius: 20px; color: white; font-weight: bold; font-size: 0.9rem; }

.v20 { border-left: 6px solid var(--v20-color); } .v20 .version-tag { background: var(--v20-color); }
.v35 { border-left: 6px solid var(--v35-color); } .v35 .version-tag { background: var(--v35-color); }

.version-block h2 { margin-top: 0; color: #2c3e50; }
.version-block ul { padding-left: 1.5rem; }
.version-block li { margin-bottom: 8px; }

.history-footer { text-align: center; margin-top: 60px; color: #7f8c8d; font-size: 0.95rem; border-top: 1px solid #eee; padding-top: 20px; }
</style>