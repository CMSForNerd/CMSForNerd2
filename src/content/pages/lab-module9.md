---
type: "content_page"
title: "Module 9 Worksheet | CMSForNerd2 Advanced E2E & Boundary Testing"
description: "Interactive lab worksheet for Playwright E2E scenarios covering dynamic role permissions, cookie expiration boundaries, and state validation in SSG/PWA applications."
schemaType: "TechArticle"
author: "CMSForNerd2 Quality Assurance Education Team"
topics: ["testing", "playwright", "e2e", "roles", "cookies", "pwa", "astro"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: lab-module9.md
  url: src/content/pages/lab-module9.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-08-01T09:00:00Z'
tags: ["testing", "playwright", "e2e", "roles", "cookies", "pwa", "astro"]
---

<article class="lab-module-page" itemscope itemtype="https://schema.org/TechArticle">
<header class="module-header">
<h1 itemprop="headline">🧪 Laboratory Module 9: Playwright E2E Testing - Dynamic Roles & Cookie Expiration</h1>
<p class="intro">
Welcome to <strong>Laboratory Module 9</strong>. In this module, students master advanced end-to-end (E2E) automated testing techniques using <strong>Playwright</strong>. Learn how to simulate dynamic role-based access controls, mock cookie expiration boundaries, and validate client-side state transitions in static progressive web apps (PWA).
</p>
</header>

<section class="learning-objectives">
<h2>🎯 Learning Objectives</h2>
<ul>
<li><strong>Dynamic Role Permissions Mocking:</strong> Use Playwright browser contexts and local storage fixtures to simulate multiple user roles (Admin, Student, Guest) on static pages.</li>
<li><strong>Cookie Expiration & Boundary Auditing:</strong> Test session time-outs, SameSite cookie attributes, and token expiration boundaries without requiring live backends.</li>
<li><strong>PWA Offline & Storage Assertions:</strong> Verify Service Worker cache interception and IndexedDB state persistence across simulated network disruptions.</li>
<li><strong>Visual Regression & DOM Assertion Patterns:</strong> Construct robust automated assertions that resist fragile UI refactoring.</li>
</ul>
</section>

<section class="exercise-box">
<h2>📝 Exercise 9.1: Dynamic Role Permission Fixtures</h2>
<p>
Even in static site architectures (SSG), client-side interactivity and micro-frontends require role-based access validation. Playwright allows tests to inject custom authentication states and localStorage claims prior to page navigation.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Authoring Role Assertion Tests</h3>
<p>
Examine how Playwright sets client-side role state before evaluating navigation capabilities:
</p>
<pre><code>import { test, expect } from '@playwright/test';

test('verify administrator access to lab manual solutions', async ({ page }) => {
  // Inject simulated admin credentials into localStorage
  await page.addInitScript(() => {
    window.localStorage.setItem('user_role', 'administrator');
    window.localStorage.setItem('auth_token', 'mock_jwt_admin_token');
  });

  await page.goto('http://127.0.0.1:4321/lab-manual');

  // Assert administrator-only solution toggle is visible
  const adminPanel = page.locator('#admin-solution-key');
  await expect(adminPanel).toBeVisible();
});</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 9.2: Cookie Expiration & Boundary Auditing</h2>
<p>
Validating cookie lifetimes and boundary conditions ensures that stale user sessions do not persist authorization privileges across static client routes.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Simulating Cookie Expiration</h3>
<p>
Write an automated Playwright test that sets an expired session cookie and verifies that client routing correctly redirects to the fallback login view:
</p>
<pre><code>test('verify automatic fallback when session cookie expires', async ({ context, page }) => {
  // Set an expired auth cookie (Expires in the past)
  await context.addCookies([{
    name: 'session_id',
    value: 'expired_session_123',
    domain: '127.0.0.1',
    path: '/',
    expires: Math.floor(Date.now() / 1000) - 3600, // 1 hour ago
    httpOnly: true,
    secure: false,
    sameSite: 'Lax'
  }]);

  await page.goto('http://127.0.0.1:4321/graduation');

  // Verify user is redirected to student welcome kit due to expired session
  await expect(page).toHaveURL(/.*welcome-kit/);
});</code></pre>
</div>
</section>

<section class="exercise-box">
<h2>📝 Exercise 9.3: PWA Service Worker & Storage Auditing</h2>
<p>
In modern Progressive Web Apps built with `@vite-pwa/astro`, testing offline availability requires verifying Service Worker cache registration using Playwright.
</p>
<div class="try-it-box">
<h3>🛠️ Student Task: Asserting Service Worker Active State</h3>
<p>
Inspect the end-to-end test fixture verifying PWA manifest and service worker registration in `tests/test_e2e.py`:
</p>
<pre><code>def test_pwa_manifest_linkage(page):
    page.goto('http://127.0.0.1:4321/')
    manifest_link = page.locator('link[rel="manifest"]')
    assert manifest_link.get_attribute('href') == '/manifest.webmanifest'</code></pre>
</div>
</section>

<nav class="footer-nav">
<a href="/lab-module8" class="btn btn-secondary">← Back to Module 8</a>
<a href="/lab-module10" class="btn btn-primary">Proceed to Module 10 →</a>
</nav>
</article>

<style>
.lab-module-page { max-width: 900px; margin: 0 auto; line-height: 1.7; color: #1e293b; }
.module-header h1 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 8px; }
.intro { background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 5px solid #22c55e; margin: 20px 0; }
.learning-objectives { background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
.exercise-box { margin-bottom: 40px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 25px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
.exercise-box h2 { color: #7c3aed; border-bottom: 2px solid #f3e8ff; padding-bottom: 6px; margin-top: 0; }
.try-it-box { background: #fafafa; border-left: 4px solid #7c3aed; padding: 15px; border-radius: 4px; margin-top: 15px; }
.try-it-box pre { background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 6px; overflow-x: auto; font-family: 'SF Mono', monospace; font-size: 0.9rem; }
.btn { display: inline-block; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 10px; }
.btn-primary { background: #0d6efd; color: white; }
.btn-secondary { background: #e2e8f0; color: #333; }
.footer-nav { display: flex; justify-content: space-between; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 30px; }
</style>
