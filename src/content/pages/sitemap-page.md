---
okf_version: 0.1
type: content_page
title: "Sitemap For CMSForNerd2"
description: "HTML Sitemap for CMSForNerd2 - A lightweight static content management system modernised in Astro 7.1."
schemaType: "WebPage"
author: "Harisfazillah Jamel"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---


<div class="sitemap-list" style="padding: 20px;">
<h2>Laboratory Sitemap</h2>
<ul style="line-height: 2;" id="sitemap-list-ul">
<!-- Will be populated dynamically or statically at runtime -->
</ul>

<hr style="margin: 30px 0; border: 0; border-top: 1px solid #eee;">
<p>
<a href="/sitemap.xml">
<img src="https://upload.wikimedia.org/wikipedia/commons/4/43/Feed-icon.svg" width="16" height="16" alt="RSS">
View XML Version
</a>
</p>
</div>

<script is:inline>
  document.addEventListener('DOMContentLoaded', () => {
const listUl = document.getElementById('sitemap-list-ul');
if (listUl) {
// Fetch dynamic pages from footer and list them
const footerLinks = document.querySelectorAll('.lab-footer-wrap nav div a');
footerLinks.forEach(link => {
const li = document.createElement('li');
const a = document.createElement('a');
a.href = link.href;
a.textContent = link.textContent;
a.style.fontWeight = 'bold';
a.style.color = '#8e44ad';
li.appendChild(a);

const span = document.createElement('span');
span.style.color = '#999';
span.style.fontSize = '0.8rem';
span.textContent = ' (Statically Modernised)';
li.appendChild(span);

listUl.appendChild(li);
});
}
});
</script>