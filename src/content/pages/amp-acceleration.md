---
okf_version: 0.1
type: "content_page"
title: "AMP Acceleration | CMSForNerd2"
description: "Technical guide on how CMSForNerd2 leverages Accelerated Mobile Pages (AMP) for mobile-first performance via Astro 7.1 build-time generation."
schemaType: "TechArticle"
author: "CMSForNerd Team"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="amp-lab">
<header class="lab-header">
<h1>⚡ AMP Acceleration Engineering</h1>
<p class="lead">Understanding the dual-view static architecture and mobile performance optimisation in CMSForNerd2.</p>
</header>

<section class="ui-section">
<h2>🚀 The Mission: Instant Mobile Load</h2>
<p>CMSForNerd2 leverages Google's <strong>Accelerated Mobile Pages (AMP)</strong> framework to provide a near-instant loading experience on mobile devices. Our implementation focuses on three pillars:</p>
<ol>
<li><strong>HTML Restriction</strong>: Stripping away heavy JavaScript in favor of AMP components.</li>
<li><strong>CSS Efficiency</strong>: Enforcing a strict 75KB inline style limit.</li>
<li><strong>Pre-rendering</strong>: Allowing search engines to safely cache and pre-render the entire page.</li>
</ol>
</section>

<section class="ui-section">
<h2>🛠️ Dual-View Static Logic</h2>
<p>Instead of server-side dynamic detection (like legacy <code>index.php?view=amp</code>), Astro 7.1 generates dual outputs statically. Standard pages are compiled to <code>[...slug]/index.html</code>, and AMP pages are pre-compiled to <code>[...slug]/amp/index.html</code>.</p>
<div class="code-compare" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
<div style="background: var(--lab-border, #f1f5f9); padding: 15px; border-radius: 8px;">
<strong>Standard View</strong>
<p style="font-size: 0.8rem;">Loads PWA features, Service Workers, and full CSS (<code>global.css</code>). Output: <code>dist/[page]/index.html</code>.</p>
</div>
<div style="background: var(--lab-border, #f1f5f9); padding: 15px; border-radius: 8px;">
<strong>⚡ AMP View</strong>
<p style="font-size: 0.8rem;">Loads <code>amp.css</code>, AMP components, and enforces strict validation. Output: <code>dist/[page]/amp/index.html</code>.</p>
</div>
</div>
</section>

<section class="ui-section">
<h2>📐 Managing the CSS Byte-Budget</h2>
<p>AMP requires all CSS to be inline and under 75KB. CMSForNerd2 automates this by:</p>
<ul>
<li><strong>Variable Synchronisation</strong>: Using the same CSS variables (<code>--lab-purple</code>, etc.) in both <code>global.css</code> and <code>amp.css</code>.</li>
<li><strong>Component Stripping</strong>: Removing desktop-only styles (like complex interactions) from the AMP stylesheet.</li>
<li><strong>Inline Injection</strong>: The Astro build engine automatically reads <code>src/styles/amp.css</code> and injects the optimised CSS directly into the <code>&lt;style amp-custom&gt;</code> tag of the AMP layout.</li>
</ul>
</section>

<section class="ui-section">
<h2>📱 Interactive Components</h2>
<p>Even though AMP limits custom JavaScript, we maintain interactivity using AMP-specific components:</p>
<table class="stack-table">
<thead>
<tr>
<th>Component</th>
<th>Role in Laboratory</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>amp-sidebar</code></td>
<td>Handles mobile navigation without blocking the main thread.</td>
</tr>
<tr>
<td><code>amp-img</code></td>
<td>Ensures layout stability (Cumulative Layout Shift) by requiring strict aspect ratios.</td>
</tr>
</tbody>
</table>
</section>

<footer class="audit-footer">
<p>View this page in AMP mode: <a href="amp/">⚡ Switch to AMP</a></p>
</footer>
</article>

<style>
.amp-lab { max-width: 900px; margin: 0 auto; line-height: 1.6; }
.ui-section { margin-bottom: 3rem; padding-bottom: 2rem; border-bottom: 1px solid var(--lab-border); }
.code-compare strong { color: var(--lab-highlight, #8e44ad); display: block; margin-bottom: 5px; }
.stack-table { width: 100%; border-collapse: collapse; margin: 20px 0; }
.stack-table th, .stack-table td { text-align: left; padding: 12px; border-bottom: 1px solid var(--lab-border); }
.audit-footer { text-align: center; font-style: italic; margin-top: 2rem; }
</style>