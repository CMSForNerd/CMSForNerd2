---
okf_version: 0.1
type: "skill"
title: "GitHub Pages Deployment Skill"
name: "github-pages-deployment"
description: "Manages and automates subpath static deployments to GitHub Pages without breaking root-relative cloud or local development."
timestamp: "2026-08-01T12:00:00Z"
topics: ["github-pages", "deployment", "base-url", "subpath", "ssg"]
---

# GitHub Pages Deployment Skill

This skill governs the techniques, dynamic configurations, and automation workflows necessary to compile and deploy the project to GitHub Pages under a repository subpath (such as `/CMSForNerd2`).

## When to use this skill

- When configuring or troubleshooting GitHub Pages deployment issues.
- When updating routing or layout navigation paths.
- When modifying the GitHub Actions CI/CD workflows.
- When updating base or site settings in the Astro build engine.

## Operational Standards & Procedures

### 1. Dynamic Path Prefixing and Routing
To support subpath deployments on GitHub Pages (`/CMSForNerd2`) without breaking local development or root-relative cloud environments:
- Define dynamic configuration in `astro.config.mjs` to adjust `site` and `base` settings depending on whether `process.env.GITHUB_ACTIONS` is `true`.
- Layouts (`Layout.astro`, `AmpLayout.astro`) and components (`Navigation.astro`) construct all root-relative paths by dynamically prefixing them with `import.meta.env.BASE_URL`.

### 2. Custom Rehype Base Rewriting Plugin
In contrast to standard build pipelines, markdown-rendered links inside content files must be post-processed to align with the subpath:
- A custom Rehype post-processing plugin `rehypeAddBase` is registered inside Astro's markdown processor configuration using `unified` from `@astrojs/markdown-remark` in `astro.config.mjs`.
- This plugin dynamically rewrites root-relative links within Markdown files during the production build for GitHub Pages, preserving original content files.

### 3. Automated Deployment Pipeline & Collision Prevention
By utilising standard workflows, GitHub Pages deployment is kept entirely automated:
- The project's GitHub Pages deployment is automated via a GitHub Actions workflow (`.github/workflows/deploy-gh-pages.yml`) that runs on pushes to the `master` branch.
- It installs dependencies with `npm ci`, compiles the static assets using `npm run build`, and publishes the resulting `dist/` directory to the `gh-pages` branch using `peaceiris/actions-gh-pages@v4` with `force_orphan: true`.
- To avoid deployment collisions on the `master` branch, any Jekyll-based GitHub Actions workflows are excluded to ensure only the Astro-specific `deploy-gh-pages.yml` pipeline manages GitHub Pages deployments.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
