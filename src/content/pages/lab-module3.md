---
okf_version: 0.1
type: "content_page"
title: "Lab Worksheet: Module 3 - CMSForNerd2"
description: "Module 3: Defensive Engineering in Static Architectures. Learn how Astro 7.1 and unprivileged containers eliminate runtime security risks."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet">
<h1>Student Lab Worksheet: Module 3</h1>
<p class="subtitle">Topic: Defensive Static Engineering & Container Security</p>

<div class="requirement-alert">
<strong>Requirement Level:</strong> Students <strong>MUST</strong> verify NGINX header configurations and secure static page outputs to achieve a secure "Green-Light" status.
</div>

<section class="objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li>Understand how **Static-Site Generation (SSG)** completely eliminates server-side vulnerabilities.</li>
<li>Implement strict **Content Security Policies (CSP)** for statically compiled resources.</li>
<li>Understand the secure design of **Unprivileged NGINX Containers** running on non-root ports.</li>
</ul>
</section>

<section class="step">
<h2>🧱 Step 1: The "Static Immunity" Concept</h2>
<p>In traditional PHP applications, every request executes code on the server, opening up possibilities for <strong>Path Traversal (../)</strong>, <strong>Local File Inclusion (LFI)</strong>, and <strong>SQL Injection</strong>.</p>

<div class="comparison-grid">
<div class="vulnerable-code" style="border-left-color: #dc3545;">
<h4>❌ Legacy Dynamic Controller (PHP)</h4>
<pre><code>// VULNERABLE TO PATH TRAVERSAL
$page = $_GET['page'];
include "contents/" . $page . ".php";</code></pre>
<p class="danger">Attacker can load system files by passing "?page=../../etc/passwd"!</p>
</div>

<div class="secure-code" style="border-left-color: #28a745;">
<h4>✅ Astro 7.1 Static Modernisation</h4>
<pre><code>// Pre-compiled statically at build time
// No runtime URL routing logic is executed on the host
// Built file: dist/about/index.html</code></pre>
<p class="success">Absolute security! The server only hosts static HTML files. No backend code execution!</p>
</div>
</div>
</section>

<section class="step">
<h2>🛡️ Step 2: Content Security Policy on Static Sites</h2>
<p>For a static site, security relies heavily on the web server headers. We configure our strict Content Security Policy directly within the web server configuration file.</p>

<div class="concept-box">
<h3>Why Static CSP Headers?</h3>
<p>A static web server like NGINX can append HTTP headers to every served file. By enforcing a strict CSP, we tell the visitor's browser exactly which domains are trusted to load script, font, and style assets.</p>
</div>

<h3>📋 Task 2.1: Review the NGINX Security configuration</h3>
<p>Open <code>nginx/default.conf</code> and locate the security headers section. Notice how we restrict script and style domains to maintain standard compliance:</p>
<div class="code-block modern">
<pre><code># Enforcing security headers directly from NGINX
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://challenges.cloudflare.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; frame-src 'self' https://challenges.cloudflare.com; object-src 'none'; base-uri 'self';" always;
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;</code></pre>
</div>
</section>

<section class="step">
<h2>🐳 Step 3: Hardened Containerisation</h2>
<p>For deployment on Render.com, we package CMSForNerd2 using a multi-stage unprivileged Docker build.</p>
<div class="file-study">
<h4>Multi-stage Containerfile/Dockerfile Configuration</h4>
<p>Notice how our build process compiling Astro 7.1 separates the build tools from the final NGINX container:</p>
<div class="code-block modern">
<pre><code># Stage 1: Build the static files
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

# Stage 2: Serve using hardened unprivileged NGINX
FROM nginx:alpine-slim
COPY --from=builder /app/dist /usr/share/nginx/html
# Run NGINX on non-root port 8080 as unprivileged user
...</code></pre>
</div>
<p><strong>Question:</strong> Why do we run the container on port <code>8080</code> instead of port <code>80</code>?</p>
<p class="answer-hint">💡 Click to reveal: Standard ports like 80 require root privileges, whereas port 8080 allows the web server to execute as a secure, unprivileged user, mitigating potential container breakout risks.</p>
</div>
</section>

<section class="step">
<h2>✅ Step 4: Verification (The "Security" Audit)</h2>
<p>Run a preview of your static compiled container and audit your NGINX headers using curl:</p>
<div class="terminal-block">
<code>curl -I http://localhost:8080/healthz</code>
</div>
<p><strong>Expected Outcome:</strong> The response must return an HTTP status of <code>200 OK</code> along with your strict Content-Security-Policy and X-Frame-Options security headers.</p>
</section>

<footer class="standards-summary">
<h2>🎓 Summary of Standards for Module 3</h2>
<ul>
<li><strong>MUST:</strong> Deliver all files over HTTPS or secure local network pathways.</li>
<li><strong>MUST:</strong> Enforce strict Content Security Policies via static server headers.</li>
<li><strong>MUST NOT:</strong> Run web server serving processes as the root system user.</li>
</ul>
</footer>

<nav class="progress-nav">
<a href="/lab-module2" class="btn prev">&lt; Previous: Module 2 (Standards)</a>
<a href="/lab-module4" class="btn next">Next: Module 4 (Automated Testing) &gt;</a>
</nav>
</article>

<style>
.lab-worksheet h1 { color: #d9534f; margin-bottom: 0.1rem; }
.lab-worksheet .subtitle { font-size: 1.2rem; color: #777; margin-bottom: 2rem; }
.lab-worksheet .requirement-alert { background: #fcf8e3; border: 1px solid #faebcc; color: #8a6d3b; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }
.lab-worksheet h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; margin-top: 2rem; }
.lab-worksheet .code-block { background: #2d2d2d; color: #ccc; padding: 1rem; border-radius: 4px; overflow-x: auto; margin: 1rem 0; }
.lab-worksheet .code-block.legacy { border-left: 5px solid #d9534f; }
.lab-worksheet .code-block.modern { border-left: 5px solid #5cb85c; }
.lab-worksheet .terminal-block { background: #000; color: #00ff00; padding: 1rem; font-family: 'Courier New', Courier, monospace; border-radius: 4px; margin: 1rem 0; }
.lab-worksheet .question-box { background: #d9edf7; border: 1px solid #bce8f1; color: #31708f; padding: 1rem; border-radius: 4px; margin: 2rem 0; }
.lab-worksheet .standards-summary { margin-top: 3rem; background: #f5f5f5; padding: 1.5rem; border-radius: 8px; }
.lab-worksheet .concept-box { background: #e7f3ff; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #0066cc; margin: 1.5rem 0; }
.lab-worksheet .file-study { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; border: 1px solid #dee2e6; }
.lab-worksheet .file-study h4 { color: #495057; margin-top: 0; }
.lab-worksheet .comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0; }
.lab-worksheet .vulnerable-code { background: #fff; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #dc3545; }
.lab-worksheet .secure-code { background: #fff; padding: 1.5rem; border-radius: 8px; border-left: 5px solid #28a745; }
.lab-worksheet .danger { color: #dc3545; font-weight: bold; }
.lab-worksheet .success { color: #28a745; font-weight: bold; }
.lab-worksheet .console-output { background: #2d2d2d; color: #f8f8f2; padding: 1rem; border-radius: 4px; margin: 0.5rem 0; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #d9534f; color: #fff; }
@media (max-width: 768px) {
.progress-nav { flex-direction: column; gap: 1rem; }
.lab-worksheet .comparison-grid { grid-template-columns: 1fr; }
}
</style>