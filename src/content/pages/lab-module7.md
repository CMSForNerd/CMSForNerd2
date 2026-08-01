---
okf_version: 0.1
type: content_page
title: "Module 7 Worksheet | CMSForNerd2 Static Security & Performance"
description: "Interactive lab worksheet for configuring Content Security Policy whitelists, unprivileged server headers, and static performance caching."
schemaType: "TechArticle"
author: "CMSForNerd2 Security Education Team"
timestamp: "2026-08-01T09:00:00Z"
topics: ["security", "owasp", "performance", "optimisation", "nginx", "astro"]
---

<article class="lab-module-page" itemscope itemtype="https://schema.org/TechArticle">
<header class="module-header">
<h1 itemprop="headline">🛡️ Laboratory Module 7: Static Security Whitelisting & Performance Hardening</h1>
<p class="intro">
Welcome to <strong>Laboratory Module 7</strong>. In this module, we explore how static site architectures (Astro 7.1) can be hardened using <strong>OWASP Web Security Principles</strong> and advanced <strong>Static Performance Optimisation</strong> configurations.
</p>
</header>

<section class="learning-objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li><strong>Mitigate Cross-Site Scripting (XSS):</strong> Learn how extracting inline scripts into bundled files enables browser-level caching and supports a strict Same-Origin CSP.</li>
<li><strong>Configure Whitelisted CSP:</strong> Configure whitelists for cryptographic SHA-256 script hashes inside unprivileged Nginx header directives.</li>
<li><strong>Implement Defensive Headers:</strong> Enforce standard web headers including HSTS and Permissions-Policies on static reverse proxies.</li>
<li><strong>Establish Standard Disclosure:</strong> Publish an RFC 9116 machine-readable contact file to facilitate responsible vulnerability reporting.</li>
</ul>
</section>

<section class="exercise-box">
<h2>📝 Exercise 7.1: Compile-Time Script Bundling</h2>
<p>
In dynamic PHP platforms, inline script blocks are often generated dynamically. In modern Astro SSG architectures, we achieve maximum performance and security by extracting scripts into compiled bundles.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Inspecting Bundle Extraction</h3>
<p>
Examine how removing the <code>is:inline</code> attribute from the main theme-switching script in <code>src/layouts/Layout.astro</code> allows Astro's compiler to minify, bundle, and generate a same-origin deferred JavaScript file.
</p>
<pre><code><!-- Before: Inline and unsafe from CSP perspective -->
<script is:inline>
  function setLaboratoryTheme(theme) { ... }
</script>

<!-- After: Bundled, minified, and secure same-origin script -->
<script>
  function setLaboratoryTheme(theme) { ... }
</script></code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 7.2: Nginx Whitelisted CSP & Cryptographic Hashes</h2>
<p>
To prevent hostile script injections (XSS), browsers enforce a <strong>Content Security Policy (CSP)</strong>. For essential scripts that must run inline (such as early dark-theme initialization to prevent visual flashes), we authorize them securely using their exact SHA-256 hashes.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Evaluating SHA-256 Hashes</h3>
<p>
Inspect the custom Nginx server header definition (<code>nginx/nginx.conf</code>). Observe how the <code>Content-Security-Policy</code> restricts <code>script-src</code> strictly to whitelisted hashes:
</p>
<pre><code>add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'sha256-qge7luCI8jS7m2s+VEmXWHFZUbELa0eR9DgWdJVskJE=' 'sha256-rZ4y4zV03XgNKcEZvPkmcm2nIQLwmv/cK+37mD6GD3U=' 'sha256-xFRTI6+2g5BLlrJacnGZmJcRlIRJZQZhw0gXxjbq9yQ=' https://cdn.ampproject.org; style-src 'self' 'unsafe-inline'; ...";</code></pre>
<p>
This ensures that even if an attacker manages to inject a malicious script block, the browser will refuse to execute it because its SHA-256 hash does not match the authorized Nginx whitelist!
</p>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 7.3: Responsible Disclosure (RFC 9116)</h2>
<p>
According to OWASP guidelines, establishing a secure path for reporting vulnerabilities is a core pillar of standard-grade web security.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Verifying the disclosure endpoint</h3>
<p>
Examine the standardised machine-readable vulnerability policy file at <code>public/.well-known/security.txt</code>. This informs security researchers of the secure coordinates to submit bug disclosures.
</p>
<pre><code>Contact: mailto:security@cmsfornerd2.test
Expires: 2027-08-01T12:00:00Z
Acknowledgements: https://cmsfornerd2.netlify.app/hall-of-fame/
Policy: https://cmsfornerd2.netlify.app/security-policy/</code></pre>
</div>
</section>

<nav class="footer-nav">
<a href="/lab-manual" class="btn btn-secondary">← Back to Lab Manual</a>
<a href="/graduation" class="btn btn-primary">Proceed to Graduation →</a>
</nav>
</article>

<style>
.lab-module-page { max-width: 900px; margin: 0 auto; line-height: 1.7; color: #1e293b; }
.module-header h1 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 8px; }
.intro { background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 5px solid #22c55e; margin: 20px 0; }
.learning-objectives { background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
.exercise-box { margin-bottom: 40px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
.exercise-box h2 { color: #d9534f; border-bottom: 2px solid #fee2e2; padding-bottom: 6px; margin-top: 0; }
.try-it-box { background: #fafafa; border-left: 4px solid #d9534f; padding: 15px; border-radius: 4px; margin-top: 15px; }
.try-it-box pre { background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 6px; overflow-x: auto; font-family: 'SF Mono', monospace; font-size: 0.9rem; }
.btn { display: inline-block; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 10px; }
.btn-primary { background: #0d6efd; color: white; }
.btn-secondary { background: #e2e8f0; color: #333; }
.footer-nav { display: flex; justify-content: space-between; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 30px; }
</style>
