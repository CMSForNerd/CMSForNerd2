---
okf_version: 0.1
type: "content_page"
title: "Static CSP Implementation Guide | CMSForNerd2 Security"
description: "Comprehensive guide to implementing Content Security Policy (CSP) and Subresource Integrity on static Astro 7.1 sites."
schemaType: "TechArticle"
author: "CMSForNerd2 Security Team"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="csp-guide" itemscope itemtype="https://schema.org/TechArticle">
<header class="guide-header">
<h1 itemprop="headline">🛡️ Static CSP Implementation Guide</h1>
<p class="intro">
Enforcing a strict <strong>Content Security Policy (CSP)</strong> is the gold standard for stopping
<strong>Cross-Site Scripting (XSS)</strong>. On static architectures like Astro 7.1, we achieve this through server-level header definitions and static meta tags.
</p>
</header>

<section class="overview">
<h2>CSP on Static Architectures</h2>
<p>
Unlike dynamic PHP sites where a random <strong>nonce</strong> can be generated on every single page request, a static site compiles to pre-rendered HTML files. Thus, we utilize two primary mechanisms for secure asset verification:
</p>
<div class="highlight-box">
<p><strong>1. Strict Domain Restrictions:</strong> Directing the web server (e.g., NGINX) to append strict HTTP headers that permit script execution only from <code>'self'</code> and specific pre-authorized domains.</p>
<p><strong>2. Subresource Integrity (SRI):</strong> Generating hashes for external assets so the browser blocks execution if an asset is modified downstream.</p>
</div>
</section>

<section class="implementation">
<h2>Step 1: NGINX Headers Configuration</h2>
<p>In <strong>CMSForNerd2</strong>, our security policy is configured inside the static web server setup (<code>nginx/default.conf</code>).</p>

<div class="code-block">
<pre><code># Enforcing security headers directly from NGINX
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://challenges.cloudflare.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; frame-src 'self' https://challenges.cloudflare.com; object-src 'none'; base-uri 'self';" always;</code></pre>
</div>

<p>This meta directive instructs the browser to only evaluate inline scripts and resources that are hosted on the same origin (<code>'self'</code>) or Cloudflare's verified widgets.</p>
</section>

<section class="comparison-section">
<h2>XSS Protection in Action</h2>
<div class="comparison-grid">
<div class="card before">
<h3>❌ Legacy (Unsafe Inline)</h3>
<pre><code>&lt;script&gt;
  // Dynamic inline without server-level checks
  alert(document.cookie);
&lt;/script&gt;</code></pre>
<p class="danger">Browser executes untrusted scripts without restriction.</p>
</div>

<div class="card after">
<h3>✅ Statically Secure</h3>
<pre><code>&lt;script src="/assets/main.js"&gt;&lt;/script&gt;
&lt;!-- Pre-compiled static script file --&gt;</code></pre>
<p class="success">Only matched sources and pre-authorized paths are allowed.</p>
</div>
</div>
</section>

<section class="lab-challenge">
<div class="try-it">
<h3>🧪 Lab Challenge: Manual Injection</h3>
<p>Open your console (F12) and try to run a dynamic script from an external origin. Notice the <strong>CSP Refusal</strong> error. This is the "Green Bar" of static security testing.</p>
</div>
</section>

<nav class="footer-nav">
<a href="/lab-manual" class="btn btn-secondary">← Back to Lab</a>
<a href="/security-policy" class="btn btn-primary">View Security Policy →</a>
</nav>
</article>

<style>
:root { --csp-red: #c7254e; --csp-green: #5cb85c; --csp-blue: #0066cc; }
.csp-guide { max-width: 900px; margin: 0 auto; line-height: 1.6; }
.guide-header h1 { color: var(--csp-red); border-bottom: 3px solid var(--csp-red); }
.intro { background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 5px solid #ffc107; }
.code-block { background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 5px; font-family: monospace; margin: 15px 0; }
.comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0; }
.card { padding: 15px; border-radius: 8px; border: 1px solid #ddd; }
.before { border-top: 5px solid var(--csp-red); }
.after { border-top: 5px solid var(--csp-green); }
.danger { color: var(--csp-red); font-weight: bold; }
.success { color: var(--csp-green); font-weight: bold; }
.try-it { background: #f0f8ff; border: 2px dashed var(--csp-blue); padding: 20px; border-radius: 10px; }
.btn { padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block; font-weight: bold; }
.btn-primary { background: var(--csp-red); color: white; }
.btn-secondary { background: #eee; color: #333; }
@media (max-width: 600px) { .comparison-grid { grid-template-columns: 1fr; } }
</style>