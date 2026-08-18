---
okf_version: 0.1
type: "skill"
title: "Documentation Governance Skill"
name: "documentation-governance"
description: "Enforces strict OKF standards, UK English conventions, and prevents orphaned pages in the documentation hierarchy."
timestamp: "2026-08-01T12:00:00Z"
topics: ["documentation", "governance", "okf", "uk-english", "navigation"]
---

# Documentation Governance Skill

This skill governs the writing styles, formatting regulations, and cross-navigational integrity standards for all documentation assets in CMSForNerd2.

## When to use this skill

- When creating or modifying markdown documentation files.
- When reorganising the project's documentation files or layout paths.
- When writing cognitive logs, plans, or commit messages.
- When adding or reviewing code comments (JSDoc, docstrings) across TS, JS, and Python files.

## Operational Standards & Procedures

### 1. Strict Standard UK English
Linguistic accuracy must be maintained at all times:
- Documentation and cognitive logs must be authored using Strict Standard UK English spelling and grammar conventions (e.g., *optimisation*, *colour*, *customise*).

### 2. Orphan Prevention & Navigation Mapping
To prevent orphaned documentation:
- Any new governance, architecture, or instructional documents must be explicitly mapped into navigation files: `SUMMARY.md`, `START-HERE.md`, `llms.txt`, and the project `README.md`.
- The repository implements a robust documentation system organised inside `docs/` according to the Diátaxis framework, containing Tutorials (`docs/tutorials/`), How-To Guides (`docs/how-to/`), Reference (`docs/reference/`), and Explanation (`docs/explanation/`) quadrants, coupled with a GitBook-compatible index file `docs/SUMMARY.md` and detailed guidelines in `docs/README.md`.
- An automated documentation CI workflow is located at `.github/workflows/docs-ci.yml` that triggers on master push/PRs. It validates Markdown file structure and frontmatter compliance (via `tools/refactor-okf.cjs`), sitemap integrity (via `tools/verify-sitemaps.js`), compiles the Astro SSG site, and executes the Pytest validation suites.
- The Python utility `tools/llms_txt2ctx.py` parses standard `llms.txt` files and compiles them into structured, standard-compliant XML context documents for AI model ingestion. An associated script `tools/build_llms_full.py` dynamically consolidates all Markdown documentation references inside `llms.txt` to compile a unified, complete `llms-full.txt` asset. Both files are automatically copied and kept synchronised within the `public/` folder.

### 3. Open Knowledge Format (OKF) Compliance & Automation
All repository documentation strictly adheres to the Open Knowledge Format (OKF) v0.1:
- Every markdown file requires YAML frontmatter starting on line 1, column 1, containing `okf_version`, `type`, `title`, `timestamp`, and `topics`.
- All string values containing emojis, colons, brackets, or other special characters must be enclosed in double quotes to prevent GitHub web view parsing issues.
- The repository contains an automated Node.js utility at `tools/refactor-okf.cjs` that recursively crawls, parses, formats, and validates the YAML frontmatter of all Markdown (`.md`) files (including injecting missing OKF fields where necessary) to ensure complete compliance with the OKF v0.1 schema.

### 4. Educational Preservation Layer
While modernisation is a priority, historical lab content is strictly preserved:
- Active, non-historical references to PHP in style comments, routing code, and offline fallback messages are updated or removed to align fully with Astro 7.1.
- However, all legacy educational laboratory pages and guides in `src/content/pages/` are preserved completely unchanged to maintain the historical context of the project's origin from the database-free `cmsfornerd` PHP CMS.

### 5. High Documentation Standards & navigation.ts Utility
Standardisation of comments and codebase utilities ensures clean readability:
- **Comments Standards**: Google-style docstrings are implemented in Python test suites (`tests/test_cms.py` and `tests/test_unit.py`), and JSDoc comments are strictly maintained in TS/JS configs and utility scripts (`src/utils/navigation.ts`, `src/pages/sitemap.xml.ts`, `tools/verify-sitemaps.js`, `tools/refactor-okf.cjs`, `astro.config.mjs`, `src/content.config.ts`) to maximise documentation standards across the project.
- **Centralised Utility**: The codebase uses a centralised content and navigation utility (`src/utils/navigation.ts`) containing `getCleanSlug` and `getNavigationPages` to handle page ID-to-slug cleaning and menu list generation, eliminating duplicated parsing logic in layout files (`Layout.astro`, `AmpLayout.astro`), page routes (`[...slug].astro`, `amp.astro`), and `sitemap.xml.ts`.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
