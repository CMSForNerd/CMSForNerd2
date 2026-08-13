---
okf_version: 0.1
type: "documentation"
title: "Static Site Deployment Tutorial"
description: "A guided lesson to deploy the CMSForNerd2 static build to cloud platforms like Render or GitHub Pages."
timestamp: "2026-08-01T14:40:00Z"
topics: ["tutorials", "deployment", "github-pages", "render"]

nav_order: 1
---

# 🎓 Static Site Deployment Tutorial

In this tutorial, you will learn how to configure and deploy CMSForNerd2 to **GitHub Pages** or **Render.com**.

---

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:
- Configure dynamic base paths for subpath deployments.
- Deploy static builds automatically via GitHub Actions.
- Launch a native static site on Render.com.

---

## 🏗️ Step-by-Step Lesson

### Step 1: Understand Path Structuring (GitHub Pages vs. Cloud)
GitHub Pages publishes sites in subdirectory pathways (e.g. `https://username.github.io/CMSForNerd2`), whereas standard cloud sites publish at the domain root (e.g. `https://cmsfornerd2.netlify.app`).

To avoid broken URLs, `astro.config.mjs` handles this dynamically. Open `astro.config.mjs` and observe the base configuration:

```javascript
import { defineConfig } from 'astro/config';

const isGitHubPages = process.env.GITHUB_ACTIONS === 'true';

export default defineConfig({
  site: isGitHubPages ? 'https://cmsfornerd.github.io' : 'https://cmsfornerd2.netlify.app',
  base: isGitHubPages ? '/CMSForNerd2' : '/',
  output: 'static',
});
```

### Step 2: Set Up GitHub Pages Deployment Pipeline
Your deployments can be automated on push to the `master` branch. Let's inspect `.github/workflows/deploy-gh-pages.yml`:

```yaml
name: Deploy Astro Static Site to GitHub Pages

on:
  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install dependencies
        run: npm ci

      - name: Build static files
        run: npm run build

      - name: Deploy static assets
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
          force_orphan: true
```

When you push your code to GitHub, this action automatically installs packages, runs `npm run build`, and publishes the static `dist/` directory to the `gh-pages` branch.

### Step 3: Deploy to Render.com Statically (Free Tier)
To deploy the compiled static assets directly to Render:

1.  Log in to your **Render.com Dashboard**.
2.  Click **New + > Static Site**.
3.  Connect your Git repository.
4.  Configure the service with these exact settings:
    *   **Build Command**: `npm run build`
    *   **Publish Directory**: `dist`
5.  Click **Create Static Site**.

Render will provision a free global CDN, automatically pull your repository, execute the static build, and serve `dist/` securely over HTTPS.

---

## 🚀 Verification

Once your deployment completes:
- Access your public site and verify that the navigation links function correctly.
- Verify that your URL bar reflects your secure hosting endpoint.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
