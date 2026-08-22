---
okf_version: 0.1
type: "documentation"
title: "GitHub Pages Deployment and Troubleshooting Guide"
description: "How-To guide for understanding, troubleshooting, and managing GitHub Pages deployments for CMSForNerd2."
timestamp: "2026-08-22T01:00:00Z"
topics: ["how-to", "github-pages", "actions", "astro", "troubleshooting"]

nav_order: 1
---

# 🚀 How to Troubleshoot and Manage GitHub Pages Deployments

This guide provides step-by-step instructions for understanding, configuring, and troubleshooting GitHub Pages deployments for CMSForNerd2.

---

## 🎯 Background and Architecture

CMSForNerd2 is a modernised static website built with the Astro 7.1 Static Site Generator (SSG) and Node.js. It compiles source files into pure HTML, CSS, and JS static assets in the `dist/` directory.

### Why Legacy Jekyll Workflows Fail

In earlier web projects, GitHub Pages automatically built markdown files using Jekyll (`actions/jekyll-build-pages`). However, CMSForNerd2 uses Astro SSG rather than Jekyll.

If a legacy Jekyll workflow (`.github/workflows/jekyll-gh-pages.yml`) is triggered, the `Build with Jekyll` step fails with build errors because the codebase does not follow Jekyll conventions.

### Active Astro Deployment Pipeline

CMSForNerd2 utilizes a dedicated Astro deployment workflow configured in `.github/workflows/deploy-gh-pages.yml`. This workflow:
1. Checks out the repository using `actions/checkout@v4`.
2. Sets up Node.js v22 using `actions/setup-node@v4`.
3. Installs dependencies using `npm ci`.
4. Compiles static assets using `npm run build`.
5. Deploys the generated `./dist` directory directly to the `gh-pages` branch using `peaceiris/actions-gh-pages@v4`.

---

## 📋 Step-by-Step Directions

### Step 1: Remove Obsolete Jekyll Workflows
To avoid workflow collisions and erroneous build failures on the `master` branch, ensure that no Jekyll workflow files exist in `.github/workflows/`. Remove any file named `jekyll-gh-pages.yml`:

```bash
rm -f .github/workflows/jekyll-gh-pages.yml
```

### Step 2: Verify Active GitHub Pages Workflow
Confirm that `.github/workflows/deploy-gh-pages.yml` exists and contains the correct build and publish configuration:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - master
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Build Site
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
          force_orphan: true
          user_name: 'github-actions[bot]'
          user_email: 'github-actions[bot]@users.noreply.github.com'
          commit_message: 'deploy: rebuild GitHub Pages'
```

### Step 3: Verify Local Build and Sitemaps Before Pushing
Run the local build and sitemap verification tools to ensure all compiled pages render cleanly:

```bash
npm run build
node tools/refactor-okf.cjs
node tools/verify-sitemaps.js
python3 -m pytest tests/test_unit.py -v
```

---

## 🔒 Best Practices for GitHub Pages

1. **Single Source of Truth**: Only maintain `.github/workflows/deploy-gh-pages.yml` for GitHub Pages deployment.
2. **Subpath Base URL Handling**: `astro.config.mjs` dynamically configures the subpath base URL when running in GitHub Actions (`GITHUB_ACTIONS=true`) to ensure root-relative links resolve correctly.
3. **Automated Validation**: The `docs-ci.yml` pipeline automatically validates OKF v0.1 frontmatter standards, multi-host sitemaps, and Pytest unit tests on every push and pull request.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-22*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
