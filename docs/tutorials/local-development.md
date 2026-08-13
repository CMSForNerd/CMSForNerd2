---
okf_version: 0.1
type: "documentation"
title: "Local Development Quickstart Tutorial"
description: "A step-by-step tutorial guiding beginners through installing dependencies, compiling static assets, and previewing CMSForNerd2."
timestamp: "2026-08-01T14:40:00Z"
topics: ["tutorials", "onboarding", "local-development", "astro"]

nav_order: 1
---

# 🎓 Local Development Quickstart

Welcome to CMSForNerd2! In this tutorial, you will set up your local development workspace, compile the static site, and verify the build.

---

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:
- Configure your local Node.js v22 environment.
- Install verified workspace dependencies.
- Compile standard and AMP static pages.
- Run a local preview server on port `4321`.

---

## 🏗️ Step-by-Step Lesson

### Step 1: Verify System Prerequisites
Before starting, ensure that Node.js (version 22) and Python (for testing) are installed. Check your versions:

```bash
node --version
python3 --version
```

### Step 2: Install Project Dependencies
Run `npm install` to load pinned packages. This command resolves peer-dependency constraints automatically via our `.npmrc` configuration:

```bash
npm install
```

Expected output:
```text
added 632 packages, and audited 633 packages in 15s
```

### Step 3: Run the Local Development Server
Launch the Astro dev engine in live reloading mode. This is useful for authoring new content or updating CSS:

```bash
npm run dev
```

The terminal will print:
```text
  🚀 Astro v7.1.6 started on http://localhost:4321/
```

Open `http://localhost:4321` in your browser to inspect the landing page. Press `Ctrl+C` to terminate the dev server.

### Step 4: Compile Production Static Assets
To verify that all layout components, Markdown pages, and AMP variants render without build-time errors, compile the site:

```bash
npm run build
```

Expected output:
```text
▶ Astro collects anonymous usage data.
14:32:55 [content] Syncing content
14:32:56 [types] Generated 2.13s
14:32:57 [build] Building static entrypoints...
generating static routes
✓ Completed in 961ms.
[build] 57 page(s) built in 6.05s
```

This compiles your pages into pure static HTML/CSS inside the `dist/` directory.

### Step 5: Run the Local Production Preview
Start the local preview server to run tests against the compiled output directory:

```bash
npm run preview
```

Open `http://localhost:4321` to verify the offline pages and PWA service workers in action.

---

## 🚀 Next Steps

Congratulations! You have completed the local development quickstart. To learn how to deploy these compiled assets to the web, continue to the [Static Site Deployment Tutorial](static-site-deployment.md).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
