---
okf_version: 0.1
type: "knowledge_base"
title: "Sovereign AI Agent Knowledge Base"
timestamp: "2026-08-01T12:00:00Z"
description: "Master directory cataloguing all Jules operational and domain-specific knowledge about CMSForNerd2."
topics: ["knowledge", "jules", "brain", "dsom"]
---

# Sovereign AI Agent Knowledge Base (CMSForNerd2)

This document contains a comprehensive record of all Google Jules operational, spatial, and domain-specific knowledge compiled from Day 0 to the present. This establishes a shared cognitive layer between Google Jules and Google Antigravity, fully compliant with the Deep State of Mind (DSOM) AI Protocol.

---

## Master Knowledge Records

1. **Ansible Idempotency Compliance**
   The Ansible playbook `deploy-static.yml` is 100% compliant with `ansible-lint`. It strictly utilises Fully Qualified Collection Names (FQCN) for all module actions and specifies `changed_when` parameters on commands to maintain idempotency.

2. **Comprehensive Unit Testing Suite**
   The repository includes a unit testing suite modularised into domain submodules inside `tests/unit/` (`ansible.py`, `containers.py`, `markdown.py`, `sitemaps.py`, `llms.py`), with `tests/test_unit.py` acting as a backward-compatible top-level facade module re-exporting test functions for Pytest execution.

33. **LLMs Context & Full Asset Compilation Utilities**
    The Python utility `tools/llms_txt2ctx.py` parses standard `llms.txt` files and compiles them into structured, standard-compliant XML context documents for AI model ingestion. An associated script `tools/build_llms_full.py` dynamically consolidates all Markdown documentation references inside `llms.txt` to compile a unified, complete `llms-full.txt` asset. Both files are automatically copied and kept synchronised within the `public/` folder.

34. **Diátaxis Documentation Framework Layout**
    The repository implements a robust documentation system organised inside `docs/` according to the Diátaxis framework, containing Tutorials (`docs/tutorials/`), How-To Guides (`docs/how-to/`), Reference (`docs/reference/`), and Explanation (`docs/explanation/`) quadrants, coupled with a GitBook-compatible index file `docs/SUMMARY.md` and detailed guidelines in `docs/README.md`.

35. **Automated Documentation CI Workflow**
    An automated documentation CI workflow is located at `.github/workflows/docs-ci.yml` that triggers on master push/PRs. It validates Markdown file structure and frontmatter compliance (via `tools/refactor-okf.cjs`), sitemap integrity (via `tools/verify-sitemaps.js`), compiles the Astro SSG site, and executes the Pytest validation suites.

3. **Code Comments and Docstrings Standards**
   Google-style docstrings are implemented in Python test suites (`tests/test_cms.py` and `tests/test_unit.py`), and JSDoc comments are strictly maintained in TS/JS configs and utility scripts (`src/utils/navigation.ts`, `src/pages/sitemap.xml.ts`, `tools/verify-sitemaps.js`, `tools/refactor-okf.cjs`, `astro.config.mjs`, `src/content.config.ts`) to maximise documentation standards across the project.

4. **Automated Integration Testing Suite**
   An automated integration testing suite is located at `tests/test_cms.py` using Pytest. It runs `npm run build`, starts the Astro preview server on port 4321, and dynamically checks sitemaps (`tools/verify-sitemaps.js`), frontmatter compliance (`tools/refactor-okf.cjs`), and the HTTP status and DOM elements of all Markdown content pages. Run it with `python3 -m pytest -v tests/test_cms.py` (requires `pytest` and `requests`).

5. **SEO Sitemap Architecture**
   The repository utilises standard SEO sitemap assets including plain-text files `sitemap.txt` (located at both repository root and `public/sitemap.txt`) and a dynamically built multi-host XML sitemap produced via the Astro endpoint `src/pages/sitemap.xml.ts` that includes Netlify, GitHub Pages, and GitBook publishing platforms.

6. **Sitemap Validation Utility**
   A Node.js validation utility is maintained at `tools/verify-sitemaps.js` to systematically check for formatting anomalies, validate multi-host URL structures, and verify that compiled sitemap links have corresponding physical HTML assets inside the built `dist/` folder to prevent broken links.

7. **Public Meta-Files Configuration**
   The repository contains an RFC 9116 compliant security contact file at `public/.well-known/security.txt` and a modernised sitemap crawler index path mapped in `public/robots.txt` to point explicitly to `/sitemap.xml` and `/sitemap.txt` instead of `/sitemap.php`.

8. **Frontend Visual Verification**
   Visual verification of frontend modifications requires launching the local preview server (`npm run preview` on port 4321) and running Playwright in a Python execution environment to capture and review screenshot outputs.

9. **Node.js Compatibility Requirements**
   The project requires Node.js v22 (>=22.12.0) for Astro 7.1 compatibility. The GitHub Actions deployment workflow (`deploy-gh-pages.yml`) utilises Node.js version 22, and both the `Dockerfile` and `Containerfile` configure their builder stage using `node:22-alpine`.

10. **GitHub Actions Collision Prevention**
    To avoid deployment collisions on the `master` branch, any Jekyll-based GitHub Actions workflows are excluded to ensure only the Astro-specific `deploy-gh-pages.yml` pipeline manages GitHub Pages deployments.

11. **Centralised Navigation Utility**
    The codebase uses a centralised content and navigation utility (`src/utils/navigation.ts`) containing `getCleanSlug` and `getNavigationPages` to handle page ID-to-slug cleaning and menu list generation, eliminating duplicated parsing logic in layout files (`Layout.astro`, `AmpLayout.astro`), page routes (`[...slug].astro`, `amp.astro`), and `sitemap.xml.ts`.

12. **Strict OKF Frontmatter Schema**
    All repository documentation strictly adheres to the Open Knowledge Format (OKF) v0.1, requiring YAML frontmatter starting on line 1, column 1, containing `'okf_version'`, `'type'`, `'title'`, `'timestamp'`, and `'topics'`. All string values containing emojis, colons, brackets, or other special characters must be enclosed in double quotes to prevent GitHub web view parsing issues.

13. **OKF frontmatter Validator Utility**
    The repository contains an automated Node.js utility at `tools/refactor-okf.cjs` that recursively crawls, parses, formats, and validates the YAML frontmatter of all Markdown (`.md`) files (including injecting missing OKF fields where necessary) to ensure complete compliance with the OKF v0.1 schema.

14. **Dual Rulebook Synchronisation**
    Root-level `AGENTS.md` and `.agents/AGENTS.md` rules and configurations are fully synchronised, establishing an AI Agent Gateway, registering all Google Antigravity-compatible Agent Skills, and explicitly documenting the strict OKF v0.1 compliance rules.

15. **Dual-Pathway Sandbox Branching Rule**
    All automation scripts, deployment pipelines, and Ansible playbooks in the repository must explicitly check for limited sandbox environments (such as the Google Jules container, typically by checking for username 'jules', custom environment variables, or virtualisation types) and implement a dual-pathway branching logic. Limited sandbox environments must bypass system-level modifications (such as systemd configurations, global packages installations, or firewall rule adjustments) to focus strictly on unprivileged workspace operations (e.g. local dependencies and compilation), whereas real OS environments are permitted to execute full administrative configurations with no limitations. An Ansible orchestration suite (`ansible.cfg`, `deploy-static.yml`, `inventory/hosts.staging.yml`, and `tools/deploy-static.sh`) is configured to demonstrate and enforce this rule.

16. **Google Antigravity Agent Skills**
    The workspace defines a comprehensive suite of 8 Google Antigravity-compatible Agent Skills located under `.agents/skills/` (`static-security-hardening`, `github-pages-deployment`, `render-deployment`, `dependency-management`, `context7-integration`, `build-preview-workflow`, `documentation-governance`, and `dsom-cognitive-protocol`). Each skill contains a `SKILL.md` file featuring a unified OKF/Antigravity YAML frontmatter block and a standard Deep State of Mind (DSOM) AI Protocol footer.

17. **Static Security Lab manual Integration**
    The `cmsfornerd2` laboratory manual (`src/content/pages/lab-manual.md`) features an interactive educational worksheet, 'Laboratory Module 7: Static Security Whitelisting & Performance Hardening' (`src/content/pages/lab-module7.md`), instructing students on applying OWASP standards, cryptographic CSP hashes, Nginx defensive configurations, and static performance caching.

18. **Asset Bundling and Theme-Switching**
    The main theme-switching logic in `src/layouts/Layout.astro` has had its `is:inline` attribute removed, allowing Astro to compile and bundle it as a cacheable static asset. Early flash prevention remains inline in the `<head>` with its SHA-256 hash whitelisted in Nginx.

19. **Nginx OWASP Defensive Hardening**
    The Nginx configuration (`nginx/nginx.conf`) implements strict OWASP-aligned security headers, including Strict-Transport-Security (HSTS), a Permissions-Policy, and a hardened Content Security Policy (CSP) that whitelists only specific SHA-256 hashes of essential inline scripts (e.g., early theme switcher in `Layout.astro`, graduation signature in `graduation.md`, sitemap in `sitemap-page.md`) and trusted script origins like `https://cdn.ampproject.org`.

20. **Subpath Deployments Support**
    To support subpath deployments on GitHub Pages (`/CMSForNerd2`) without breaking local development or root-relative cloud environments, `astro.config.mjs` dynamically adjusts the `site` and `base` settings depending on whether `process.env.GITHUB_ACTIONS` is `true`. Layouts (`Layout.astro`, `AmpLayout.astro`) and components (`Navigation.astro`) construct all root-relative paths by dynamically prefixing them with `import.meta.env.BASE_URL`.

21. **Custom Rehype Base Rewriter**
    A custom Rehype post-processing plugin `rehypeAddBase` is registered inside Astro's markdown processor configuration using `unified` from `@astrojs/markdown-remark` in `astro.config.mjs`. This plugin dynamically rewrites root-relative links within Markdown files during the production build for GitHub Pages, preserving original content files.

22. **GitHub Pages Continuous Deployment Pipeline**
    The project's GitHub Pages deployment is automated via a GitHub Actions workflow (`.github/workflows/deploy-gh-pages.yml`) that runs on pushes to the `master` branch. It installs dependencies with `npm ci`, compiles the static assets using `npm run build`, and publishes the resulting `dist/` directory to the `gh-pages` branch using `peaceiris/actions-gh-pages@v4` with `force_orphan: true`.

23. **Render Blueprint Pathways**
    The repository is configured for deployment to Render.com via a root-level `render.yaml` Blueprint Specification supporting two pathways: (1) a containerised Web Service using a multi-stage Dockerfile that packages the Astro site in a hardened, unprivileged Nginx server listening on port 8080 with a `/healthz` health check, and (2) a native free Static Site service ('cmsfornerd2-static') configured to run `npm run build` and publish the `dist` directory. For manual dashboard deployments on Render, the Build Command must be set to `npm run build` and the Publish Directory to `dist` to prevent 'Publish directory dist/ does not exist!' failures, as documented in `README.md` and `docs/migration-guide.md`.

24. **Environment Package Configuration (.npmrc)**
    The development environment is configured via a root-level `.npmrc` file specifying `legacy-peer-deps=true` to automatically resolve peer-dependency conflicts (such as between `@vite-pwa/astro` and newer Astro versions like `astro@7.1.6`) across any local, containerised, or cloud deployment environments (e.g., Render.com host environments).

25. **PHP Reference Removal & Lab Content Preservation**
    Active, non-historical references to PHP in style comments, routing code, and offline fallback messages are updated or removed to align fully with Astro 7.1. However, all legacy educational laboratory pages and guides in `src/content/pages/` are preserved unchanged to maintain the historical context of the project's origin from the database-free `cmsfornerd` PHP CMS.

26. **Deterministic Build Dependencies**
    To guarantee build determinism and handle peer-dependency constraints with legacy packages like `@vite-pwa/astro`, dependencies in `package.json` (such as `astro`, `@astrojs/mdx`, and `@vite-pwa/astro`) are strictly pinned to exact versions (e.g., `astro@7.1.6`).

27. **Context7 Documentation Synchronization**
    The repository integrates Context7 services using `context7.json` at the root. Automated documentation refreshes are configured via both GitLab CI (`.gitlab-ci.yml`) and GitHub Actions (`.github/workflows/context7-refresh.yml`), requiring the `CONTEXT7_API_KEY` environment variable/secret to execute.

28. **Static Assets Local Compilation**
    The project is compiled to static assets in the `dist/` directory using `npm run build`, and can be locally previewed on port 4321 using `npm run preview`.

29. **UK English Documentation Standard**
    Documentation and cognitive logs must be authored using Strict Standard UK English spelling and grammar conventions.

30. **Orphan Prevention Navigation Rules**
    To prevent orphaned documentation, any new governance, architecture, or instructional documents must be explicitly mapped into navigation files: `SUMMARY.md`, `START-HERE.md`, `llms.txt`, and the project `README.md`.

31. **DSOM Cognitive Protocol Integration**
    The workspace implements the Deep State of Mind (DSOM) cognitive protocol, which requires maintaining synchronised AI agent rules in root-level `AGENTS.md` and `.agents/AGENTS.md`, and tracking spatial memory within `.agents/brain/`.

32. **Pure Static SSG Modernisation**
    CMSForNerd2 is a static modernisation of the legacy database-free PHP CMS, utilising Astro Static Site Generator (SSG) to produce purely statically served assets (HTML5, CSS3, ES6+ JS).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
