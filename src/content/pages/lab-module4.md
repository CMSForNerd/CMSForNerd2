---
okf_version: 0.1
type: "content_page"
title: "Lab Worksheet: Module 4 - CMSForNerd2"
description: "Student Lab Worksheet for Module 4: Automated Testing with Playwright. Learn to test static Astro 7.1 layouts and components."
schemaType: "WebPage"
author: "CMSForNerd Team & Google Gemini"
timestamp: "2026-07-30T12:00:00Z"
topics: ["modernisation", "astro", "static", "architecture"]
---

<article class="lab-worksheet">
<h1>Student Lab Worksheet: Module 4</h1>
<p class="subtitle">Topic: Automated End-to-End Testing with Playwright</p>

<div class="requirement-alert">
<strong>Requirement Level:</strong> Students <strong>MUST</strong> pass all static visual assertions to achieve "Certified Developer" status.
</div>

<section class="objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li>Understand the **Arrange-Act-Assert (AAA)** pattern in front-end browser testing.</li>
<li>Write a Playwright browser test to verify static page integrity.</li>
<li>Master terminal-based testing for static web applications.</li>
</ul>
</section>

<section class="step">
<h2>📂 Step 1: The Test Anatomy</h2>
<p>For statically built sites, unit tests on individual functions are often replaced by integration and End-to-End (E2E) tests. We verify that pages render correctly in real browsers.</p>

<h3>The AAA Pattern in E2E Testing:</h3>
<ul>
<li><strong>Arrange:</strong> Start the local preview server and set up the browser viewport.</li>
<li><strong>Act:</strong> Navigate the browser to the target static URL (e.g., <code>/about</code>).</li>
<li><strong>Assert:</strong> Check if elements, classes, and styles render as expected.</li>
</ul>
</section>

<section class="step">
<h2>🛠️ Step 2: Writing Your First Browser Test</h2>
<p>You will write a test to ensure that the layout, navigation menu, and CSS classes render correctly without broken styles.</p>
<p><strong>Task:</strong> Create a standard browser test file (e.g., <code>tests/layout.test.ts</code>):</p>
<div class="code-block modern">
<pre><code>import { test, expect } from '@playwright/test';

test.describe('CMSForNerd2 Layout Integrity', () => {
  test('should load the home page and render hero section correctly', async ({ page }) => {
    // 1. Arrange & Act - Navigate to local preview
    await page.goto('http://localhost:4321/');

    // 2. Assert - Validate that the main elements render
    const heading = page.locator('h1');
    await expect(heading).toContainText('Welcome to CMSForNerd2');

    // Confirm that the CSS grid and runtime badges exist
    const badge = page.locator('.badge.astro-version');
    await expect(badge).toBeVisible();
  });
});</code></pre>
</div>
</section>

<section class="step">
<h2>🚀 Step 3: Running the Test Suite</h2>
<p>Ensure that your local preview server is running, and launch the headless browser tests:</p>
<div class="terminal-block">
<code>npx playwright test</code>
</div>
<p><strong>What to look for:</strong></p>
<ul>
<li><strong>Success message:</strong> Playwright will show "all tests passed" with a green checkmark.</li>
<li><strong>Errors/Failures:</strong> If an assertion fails, Playwright will capture a screenshot and trace report showing the exact layout mismatch.</li>
</ul>
</section>

<section class="step">
<h2>🧪 Step 4: The "Breaking" Exercise</h2>
<p>To truly understand testing, you must see a failure.</p>
<ol>
<li>Open <code>src/content/pages/index.md</code>.</li>
<li>Temporarily change the main heading to something else, or remove the <code>astro-version</code> class from the badge.</li>
<li>Run the test again.</li>
<li><strong>Observe:</strong> Watch how the browser test identifies the broken selector instantly, preventing deployment of incorrect pages!</li>
</ol>

<div class="question-box">
<p><strong>Question for the Student:</strong> Why are E2E browser tests particularly valuable for static sites generated via Markdown/MDX collections?</p>
</div>
</section>

<footer class="standards-summary">
<h2>🎓 Summary of Standards for Module 4</h2>
<ul>
<li><strong>MUST:</strong> Assert that critical SEO meta elements (title, description) exist on every page.</li>
<li><strong>MUST:</strong> Test responsive designs by executing assertions against both desktop and mobile viewports.</li>
<li><strong>SHOULD:</strong> Assert that PWA service workers and offline fallback targets are discoverable.</li>
</ul>
</footer>

<nav class="progress-nav">
<a href="/lab-module3" class="btn prev">&lt; Previous: Module 3 (Defensive Engineering)</a>
<a href="/lab-module5" class="btn next">Next: Module 5 (Coverage &amp; QA) &gt;</a>
</nav>
</article>

<style>
.lab-worksheet h1 { color: #d9534f; margin-bottom: 0.1rem; }
.lab-worksheet .subtitle { font-size: 1.2rem; color: #777; margin-bottom: 2rem; }
.lab-worksheet .requirement-alert { background: #fcf8e3; border: 1px solid #faebcc; color: #8a6d3b; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }
.lab-worksheet h2 { color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; margin-top: 2rem; }
.lab-worksheet .code-block { background: #2d2d2d; color: #ccc; padding: 1rem; border-radius: 4px; overflow-x: auto; margin: 1rem 0; }
.lab-worksheet .code-block.modern { border-left: 5px solid #5cb85c; }
.lab-worksheet .terminal-block { background: #000; color: #00ff00; padding: 1rem; font-family: 'Courier New', Courier, monospace; border-radius: 4px; margin: 1rem 0; }
.lab-worksheet .question-box { background: #d9edf7; border: 1px solid #bce8f1; color: #31708f; padding: 1rem; border-radius: 4px; margin: 2rem 0; }
.lab-worksheet .standards-summary { margin-top: 3rem; background: #f5f5f5; padding: 1.5rem; border-radius: 8px; }
.progress-nav { display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #eee; }
.progress-nav .btn { padding: 1rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; }
.progress-nav .prev { background: #6c757d; color: #fff; }
.progress-nav .next { background: #5cb85c; color: #fff; }
@media (max-width: 768px) { .progress-nav { flex-direction: column; gap: 1rem; } }
</style>