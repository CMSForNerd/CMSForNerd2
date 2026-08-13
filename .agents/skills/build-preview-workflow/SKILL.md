---
okf_version: 0.1
type: "skill"
title: "Build and Preview Workflow Skill"
name: "build-preview-workflow"
description: "Guides local compilation, testing, and preview workflows for Astro 7.1 static site generator."
timestamp: "2026-08-01T12:00:00Z"
topics: ["build", "preview", "astro", "static", "workflow"]
---

# Build and Preview Workflow Skill

This skill governs the compilation of CMSForNerd2's static assets, local port configuration, live preview procedures, and comprehensive Python/Node testing suites.

## When to use this skill

- When building the static application locally or in a remote sandbox.
- When starting local preview servers to verify routing, layout, and styling.
- When configuring port and server parameters for local testing.
- When running unit, integration, or visual verification tests on project modifications.

## Operational Standards & Procedures

### 1. Project Static Compilation
CMSForNerd2 is a static modernisation of the legacy database-free PHP CMS:
- Utilise the Astro Static Site Generator (SSG) to produce purely statically served assets (HTML5, CSS3, ES6+ JS).
- Compile the project to static assets in the `dist/` directory using the command: `npm run build`.

### 2. Local Previewing
To run and verify the compiled static assets locally:
- Preview the statically built application locally on port 4321 using the command: `npm run preview`.
- Active, non-historical references to PHP in style comments, routing code, and offline fallback messages are updated or removed to align fully with Astro 7.1.

### 3. SEO Sitemap Assets & Validation
To maintain high SEO performance and prevent broken links:
- The repository utilises standard SEO sitemap assets including plain-text files `sitemap.txt` (located at both repository root and `public/sitemap.txt`) and a dynamically built multi-host XML sitemap produced via the Astro endpoint `src/pages/sitemap.xml.ts` that includes Netlify, GitHub Pages, and GitBook publishing platforms.
- A Node.js validation utility is maintained at `tools/verify-sitemaps.js` to systematically check for formatting anomalies, validate multi-host URL structures, and verify that compiled sitemap links have corresponding physical HTML assets inside the built `dist/` folder to prevent broken links.

### 4. Comprehensive Unit and Integration Testing Suites
Testing is an integral component of the development lifecycle:
- **Unit Testing**: The repository includes a comprehensive unit testing suite in `tests/test_unit.py` (executed via Pytest) that validates Ansible playbook FQCN syntax/idempotency, Dockerfile and Containerfile properties (node:22-alpine base, USER nginx, EXPOSE 8080), Markdown OKF frontmatter and DSOM footer standards, strict UK English spellings, and sitemap/context7.json structures.
- **Integration Testing**: An automated integration testing suite is located at `tests/test_cms.py` using Pytest. It runs `npm run build`, starts the Astro preview server on port 4321, and dynamically checks sitemaps (`tools/verify-sitemaps.js`), frontmatter compliance (`tools/refactor-okf.cjs`), and the HTTP status and DOM elements of all Markdown content pages. Run it with: `python3 -m pytest -v tests/test_cms.py` (requires `pytest` and `requests`).
- **Visual Verification**: Visual verification of frontend modifications requires launching the local preview server (`npm run preview` on port 4321) and running Playwright in a Python execution environment to capture and review screenshot outputs.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
