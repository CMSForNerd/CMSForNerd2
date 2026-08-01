---
okf_version: 0.1
type: content_page
title: "Graduation: Astro 7.1 Static Modernisation Mastery - CMSForNerd2"
description: "Official Certificate of Completion for the CMSForNerd2 Static Modernisation Curriculum."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="graduation-page">
<header class="graduation-header no-print">
<h1>🏁 Curriculum Complete</h1>
<p class="congrats">
You have successfully transformed a dynamic legacy application into a high-performance,
standards-compliant Astro 7.1 static site with complete offline capabilities.
</p>
</header>

<div class="certificate-container">
<div class="certificate">
<div class="cert-border-outer">
<div class="cert-border-inner">
<div class="cert-content">
<span class="cert-seal">🎓</span>
<h2 class="cert-title">Certificate of Completion</h2>
<h3 class="cert-subtitle">Astro 7.1 Static Modernisation Mastery</h3>

<div class="cert-award">
<p>This certifies that</p>
<div class="student-name">
<span id="cert-student-name">[Your Name Here]</span>
</div>
</div>

<p class="cert-text">
Has demonstrated professional proficiency in <strong>Astro 7.1 Architecture</strong>,
<strong>Defensive Static Engineering</strong>, and <strong>Automated Build Verification</strong>
within the CMSForNerd2 Static Modernisation Lab environment.
</p>

<table class="competency-table">
<thead>
<tr>
<th>Core Competency</th>
<th>Standard Achieved</th>
</tr>
</thead>
<tbody>
<tr><td>Static Architecture</td><td>Astro 7.1 Frontmatter & Layout Components</td></tr>
<tr><td>Defensive Engineering</td><td>Unprivileged NGINX Hosting & Pure Static CSP</td></tr>
<tr><td>Build Quality Assurance</td><td>Playwright E2E Integration & PWA Caching</td></tr>
</tbody>
</table>

<div class="signatures">
<div class="signature">
<div class="sig-line"></div>
<p>Harisfazillah Jamel</p>
<span>Lead Developer, CMSForNerd2</span>
</div>
<div class="signature">
<div class="sig-line"></div>
<p>Gemini AI</p>
<span>Thought Partner & Auditor</span>
</div>
</div>

<div class="footer-meta">
<p>Verification Date: <span id="cert-verification-date">July 30, 2026</span></p>
<p class="digital-sig">SHA-256 ID: <span id="cert-digital-sig">SHA256 signature loading...</span></p>
</div>
</div>
</div>
</div>
</div>
</div>

<section class="next-steps no-print">
<h2>🛠️ Teacher's Instructions</h2>
<div class="instruction-box">
<ul>
<li><strong>To Issue:</strong> Send students the link: <code>graduation/index.html?student=Full+Name</code></li>
<li><strong>To Print:</strong> Press <kbd>Ctrl + P</kbd>. The layout is optimised to hide UI elements and print only the certificate.</li>
</ul>
</div>
</section>
</article>

<script is:inline>
  document.addEventListener('DOMContentLoaded', () => {
const params = new URLSearchParams(window.location.search);
const student = params.get('student') || '[Your Name Here]';

// Set student name
const elName = document.getElementById('cert-student-name');
if (elName) elName.textContent = student;

// Set current date
const options = { year: 'numeric', month: 'long', day: 'numeric' };
const todayStr = new Date().toLocaleDateString('en-GB', options);
const elDate = document.getElementById('cert-verification-date');
if (elDate) elDate.textContent = todayStr;

// Generate simple deterministic SHA256 signature
const dateStamp = new Date().toISOString().split('T')[0];
const signaturePlain = student + dateStamp;

// Use Web Crypto API if available, else a mock SHA256-like hash
if (window.crypto && window.crypto.subtle) {
const encoder = new TextEncoder();
const data = encoder.encode(signaturePlain);
window.crypto.subtle.digest('SHA-256', data).then(hashBuffer => {
const hashArray = Array.from(new Uint8Array(hashBuffer));
const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
const elSig = document.getElementById('cert-digital-sig');
if (elSig) elSig.textContent = "SHA-256 ID: " + hashHex;
});
} else {
let hash = 0;
for (let i = 0; i < signaturePlain.length; i++) {
hash = (hash << 5) - hash + signaturePlain.charCodeAt(i);
hash |= 0;
}
const elSig = document.getElementById('cert-digital-sig');
if (elSig) elSig.textContent = "SHA-256 ID: mock_" + Math.abs(hash).toString(16);
}
});
</script>