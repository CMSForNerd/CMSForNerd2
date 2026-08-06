---
okf_version: 0.1
type: "content_page"
title: "SOP: Ethical AI Integration | CMSForNerd2 Laboratory"
description: "Standard Operating Procedure for responsible AI usage in the CMSForNerd2 developer workspace."
schemaType: "CreativeWork"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="ai-sop" itemscope itemtype="https://schema.org/CreativeWork">
<header class="sop-header">
<h1 itemprop="name">📜 SOP: Responsible AI Usage in the Lab</h1>
<div class="sop-meta">
<p><strong>Standard Operating Procedure #2026-01</strong></p>
<p><strong>Effective Date:</strong> <time itemprop="datePublished" datetime="2026-07-30">30 July 2026</time></p>
</div>
</header>

<section class="objective">
<h2>🎯 Objective</h2>
<p itemprop="abstract">
To leverage AI (such as Google Jules) to accelerate learning while maintaining
individual coding integrity and standard schema compliance within the Astro 7.1 static environment.
</p>
</section>

<section class="rule">
<h2>1. The "Think First" Rule</h2>
<div class="rule-box">
<p><strong>MUST:</strong> Students <strong>MUST</strong> attempt to analyze errors or structure problems for 10 minutes using the official workspace documentation before prompting an AI agent.</p>
</div>
</section>

<section class="rule">
<h2>2. Verification & Auditing (Trust but Verify)</h2>
<p>AI-generated code <strong>MUST NOT</strong> be merged until it passes the compilation and schema check suite.</p>

<div class="workflow">
<h3>The Mandatory Verification Loop:</h3>
<ol>
<li>Review AI code modifications in your local workspace environment.</li>
<li>Validate sitemap and layout props with zero warnings.</li>
<li>Run <code>npm run build</code> (Content collections schema and TypeScript logic check).</li>
<li>Run <code>npm run preview</code> to verify standard rendering visual status.</li>
</ol>
</div>

<div class="warning-box">
<p>⚠️ <strong>WARNING:</strong> Bypassing the static build compliance check is considered <strong>academic dishonesty</strong>.</p>
</div>
</section>

<section class="instructor-note">
<h2>🎓 Learning Outcome</h2>
<p>
Students who master this SOP will enter the industry as <strong>effective AI partners</strong>,
capable of directing intelligent agents while maintaining strict web standards.
</p>
</section>

<nav class="footer-nav">
<a href="/ai-dev" class="btn btn-secondary">🤖 AI Development Guide</a>
<a href="/lab-manual" class="btn btn-primary">Return to Lab Manual</a>
</nav>
</article>

<style>
:root { --sop-blue: #0066cc; --sop-gold: #ff9800; --sop-green: #4caf50; }
.ai-sop { max-width: 850px; margin: 0 auto; line-height: 1.7; }
.sop-header { background: #e7f3ff; padding: 20px; border-radius: 8px; border-left: 5px solid var(--sop-blue); margin-bottom: 30px; }
.rule-box { background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 5px solid var(--sop-gold); margin: 15px 0; }
.workflow { background: #f0f8ff; padding: 20px; border-radius: 8px; border: 1px solid #d0e4f5; }
.warning-box { background: #fff3e0; padding: 15px; border-radius: 8px; border: 2px solid #ff6f00; text-align: center; font-weight: bold; }
.instructor-note { background: #e8f5e9; padding: 25px; border-radius: 8px; border-left: 5px solid var(--sop-green); margin-top: 40px; }
.footer-nav { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
.btn { padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; display: inline-block; margin: 5px; }
.btn-primary { background: var(--sop-blue); color: white; }
.btn-secondary { background: #eee; color: #333; }
</style>