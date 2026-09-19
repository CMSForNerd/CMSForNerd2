---
type: "knowledge_base"
title: "Sovereign AI Agent Knowledge Base"
description: "Master directory cataloguing all 50 Jules operational and domain-specific knowledge points about CMSForNerd2."
topics: ["knowledge", "jules", "brain", "dsom", "antigravity"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: knowledge.md
  url: .agents/brain/knowledge.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-16T00:00:00Z'
tags: ["knowledge", "jules", "brain", "dsom", "antigravity"]
---

# Sovereign AI Agent Knowledge Base (CMSForNerd2)

This document contains a comprehensive record of all 50 Google Jules operational, spatial, and domain-specific knowledge points compiled from Day 0 to the present. This establishes a shared cognitive layer between Google Jules and Google Antigravity, fully compliant with the Deep State of Mind (DSOM) AI Protocol and Open Knowledge Format (OKF) v0.2.

---

## Master Knowledge Records (50 Core Capabilities)

1. **Python FastMCP Gateway Server**
   The repository adopts a Python FastMCP (Model Context Protocol) server gateway located at `tools/mcp/server.py` (with unit tests in `tests/unit/mcp.py`) supporting stdio, SSE, WebSocket, WebRTC P2P mesh signaling, and HTTP/3 WebTransport datagram transport modes via `create_mcp_app()`, exposing live Astro SSG routes (`list_ssg_routes`), route content (`get_route_content`), full-text search (`search_ssg_routes`), sitemaps (`get_sitemap_routes`), spatial memory knowledge graph concepts (`get_openwiki_concept`), and diagram schema validation (`validate_diagram_schema`) directly to AI agents.

2. **WebGPU Application Development Framework**
   Comprehensive documentation for building WebGPU applications within CMSForNerd2 is located at `docs/how-to/webgpu-application-development.md` and indexed in `docs/SUMMARY.md`, `docs/README.md`, and `src/components/Navigation.astro`. The guide covers hardware capability probing, WebLLM execution, tri-tiered ensemble fallbacks (WebGPU -> Wasm SIMD CPU -> AST Synthesizer), local vector search integration with IndexedDB, custom WGSL compute pipelines, INT4 bit-unpacking math/WGSL snippets, and COOP/COEP isolation security hardening.

3. **Modular Domain Unit Testing Suite**
   The repository includes a unit testing suite modularised into domain submodules inside `tests/unit/` (`ansible.py`, `containers.py`, `markdown.py`, `sitemaps.py`, `llms.py`, `mcp.py`, `links.py`), with `tests/test_unit.py` acting as a backward-compatible top-level facade module re-exporting test functions and classes (`InternalBrokenLinksTest`, `ExternalBrokenLinksTest`, `test_websocket_reconnect_failure_mode`, `test_mcp_webrtc_p2p_mesh_transport`, `test_mcp_webtransport_datagram_handler`) for Pytest execution.

4. **WebAssembly Cryptographic & Offline AI Studio**
   The repository features a browser-native WebAssembly Cryptographic, OKF v0.2 Document Processing, WebTreeSitter AST Parsing, WebGPU Multi-Model Ensemble Fallbacks for Air-Gapped Code Remediation, WebNN (Web Neural Network API `navigator.ml`) browser integration, FastMCP WebRTC/WebTransport P2P agent mesh collaboration, and Offline Semantic AI Search Studio at `/wasm-studio` (`src/pages/wasm-studio.astro` and `src/components/WasmStudio.astro`) enabling client-side SHA-256 hash calculation, CSP header whitelist string generation, OKF v0.2 frontmatter parsing and validation, WebTreeSitter client-side AST parsing, WebGPU pipeline layout and compute pipeline caching (`pipelineLayoutCache`, `computePipelineCache`), asynchronous Web Worker WGSL shader compilation, WebGPU compute shader visual matrix canvas (`#webgpu-canvas`), WGSL INT4 speculative KV-cache dequantization (`unpack_int4_weight`), offline vector embedding search, WebLLM WebGPU generation, and HuggingFace ONNX Web Runtime streaming completion.

5. **Dependabot Automated Vulnerability Scans**
   The repository configures Dependabot (`.github/dependabot.yml`) for weekly npm and pip updates, accompanied by an automated GitHub Actions security workflow (`.github/workflows/dependabot-vulnerability-scan.yml`) executing npm audit and pip-audit vulnerability checks.

6. **Render.com Dual Blueprint Deployment Pathways**
   The repository is configured for deployment to Render.com via a root-level `render.yaml` Blueprint Specification supporting two pathways: (1) a containerised Web Service using a multi-stage Dockerfile that packages the Astro site in a hardened, unprivileged Nginx server listening on port 8080 with a `/healthz` health check, and (2) a native free Static Site service ('cmsfornerd2-static') configured with static caching header policies, COOP (`same-origin`), COEP (`require-corp`), and CSP (`worker-src 'self' blob:;`) security headers for `/pagefind/*` and `/_astro/*` assets, running `npm run build` and publishing `dist`.

7. **Nginx OWASP Security Headers**
   The Nginx configuration (`nginx/nginx.conf`) implements strict OWASP-aligned security headers including Cross-Origin-Opener-Policy: `same-origin` (COOP), Cross-Origin-Embedder-Policy: `require-corp` (COEP), Content Security Policy (`worker-src 'self' blob:;`), `gzip_static on;`, explicitly declared `application/wasm` MIME types, and dedicated immutable caching policy rules (`Cache-Control: "public, max-age=31536000, immutable"`) for WebAssembly search binaries under `/pagefind/`.

8. **Pytest Session Preview Server Management**
   The Pytest test suite manages the Astro preview server on port 4321 via a shared, session-scoped fixture in `tests/conftest.py` to prevent port binding collisions when running multiple test modules (`tests/test_cms.py` and `tests/test_e2e.py`). The fixture explicitly forces `GITHUB_ACTIONS=false` during test session setup so `npm run build` and `npm run preview` consistently serve assets at root (`http://127.0.0.1:4321/`) across both local and CI environments, spawning the process with `start_new_session=True` so `os.killpg` can cleanly terminate the entire process group on teardown without sending SIGTERM signals to Pytest.

9. **Playwright End-to-End Browser Test Suite**
   The repository includes a Playwright End-to-End browser test suite at `tests/test_e2e.py` that verifies light/dark theme switching, route navigation across dynamic pages, PWA web manifest (`manifest.webmanifest`) linkage, service worker asset availability, Wasm Studio SHA-256 hash calculation, OKF frontmatter parsing, interactive vector synchronization, Pagefind search query execution, dynamic role permissions (`test_dynamic_role_permissions`), cookie expiration boundary checks (`test_cookie_expiration_boundary`), and WebGPU canvas matrix visual regression snapshots (`test_webgpu_canvas_visual_regression`) against the Astro SSG preview server.

10. **Interactive Laboratory Manual Modules**
    The cmsfornerd2 laboratory manual (`src/content/pages/lab-manual.md`) features interactive educational laboratory modules in `src/content/pages/` (Modules 1 through 11), covering static security whitelisting, performance hardening, Wasm SRI whitelisting, Playwright E2E role permission testing, client-side Wasm vector search with FastMCP ADR validation, and WebGPU multi-model ensemble fallbacks with dynamic air-gapped code remediation.

11. **Python Static Analysis & Type Inspection**
    Python static analysis and tests across `tests/` and `tools/` are verified using `ruff check tests/ tools/`, `PYTHONPATH=. mypy --explicit-package-bases --strict tests tools`, and `PYTHONPATH=. pytest tests/`.

12. **Code Comment & Docstring Standards**
    PEP-257-compliant Google-style docstrings are implemented across Python utility tools (`tools/migrate_okf_v02.py`, `tools/build_llms_full.py`, `tools/llms_txt2ctx.py`, `tools/mcp/server.py`) and test suites (`tests/test_cms.py`, `tests/test_e2e.py`, `tests/unit/*.py`), JSDoc comments are maintained in Node.js scripts (`tools/verify-sitemaps.js`, `tools/refactor-okf.cjs`), and Bash scripts (`tools/eod-palace.sh`, `tools/deploy-static.sh`) feature execution requirements, usage guidelines, and line-by-line comments.

13. **Google Antigravity Agent Skills Ecosystem**
    The workspace defines a suite of Google Antigravity-compatible Agent Skills located under `.agents/skills/` (including `google-deep-research`, `triple-render-architecture-diagram`, `diagram-design-standards`, `docs-write`, `docs-review`, `docstring`, `docx`, `openapi-spec-generation`, `hyperparameter-tuning-expert`, `knowledge-base-templates`, `architecture-decision-records`, `changelog-automation`, `okf-v02-migration`, `unit-testing-suite`, `code-health-linting`, `documentation-governance`, `dsom-cognitive-protocol`, `docstring-and-jsdoc`, and `web-design-guidelines`). Each skill contains a `SKILL.md` file featuring a unified OKF v0.2 YAML frontmatter block, standard operational parameters, and a Deep State of Mind (DSOM) AI Protocol footer.

14. **Astro Content Collection Loader & Slug Normalisation**
    The Astro Content Collection loader in `src/content.config.ts` uses `base: '.'` with glob patterns `['src/content/pages/**/*.md', 'docs/**/*.md']` to load both `src/content/pages/` and `docs/` Markdown files into the pages collection, while `getCleanSlug` in `src/utils/navigation.ts` strips `src/content/pages/` prefixes to normalize route slugs.

15. **Triple-Render Architecture Diagram Specification**
    The repository adopts the Triple-Render Architecture Diagram Specification skill (`triple-render-architecture-diagram` located in `.agents/skills/triple-render-architecture-diagram/SKILL.md` and `skills/triple-render-architecture-diagram/SKILL.md`, documented in `docs/explanation/diagram-design-standards-skill.md`), mandating a unified 4-tier visual deliverable sequence for all technical diagrams: (1) ASCII trees, (2) standalone Dark Slate Navy raw SVG vector graphics (`#0F172A`), (3) Git-native Mermaid diagram block, and (4) summary interface and routing comparison table, backed by adaptive CSS in `src/styles/global.css` for light mode and toner-saving print mode (`@media print`).

16. **Vite PWA Cache Maximum Limit**
    The Vite PWA Astro configuration in `astro.config.mjs` sets `workbox.maximumFileSizeToCacheInBytes` to 35 MB (35 *1024* 1024) to allow pre-caching large WebAssembly binaries (such as ONNX Runtime Web WASM files) and bundled client script assets.

17. **GitHub Pages Deployment Workflow**
    The GitHub Pages deployment for the Astro SSG site is published from `dist/` via `.github/workflows/deploy-gh-pages.yml`, with `public/.nojekyll` ensuring that asset directories like `_astro/` are not processed or ignored by GitHub Pages.

18. **Deterministic Build Dependencies**
    To guarantee build determinism and handle peer-dependency constraints with legacy packages like `@vite-pwa/astro`, dependencies in `package.json` (such as `astro`, `@astrojs/mdx`, and `@vite-pwa/astro`) are managed with exact versions or controlled ranges (e.g., `astro@^7.3.2` updated to resolve security audit vulnerabilities).

19. **Jules Autonomous Platform Guide**
    The repository includes a technical guide at `docs/jules-platform-guide.md` covering autonomous AI pair-programming with Google Jules, OpenTofu IaC provisioning, Ansible automation, PR comment collaboration models, Google Antigravity multi-agent orchestration, and Deep State of Mind (DSOM) governance.

20. **Spatial Memory & Pre-Commit Guardrail Inspector**
    The workspace maintains an executable pre-commit guardrail script at `tools/eod-palace.sh` that validates spatial memory brain files in `.agents/brain/`, enforces OKF v0.2 frontmatter compliance (via `tools/migrate_okf_v02.py`), and verifies sitemaps (`tools/verify-sitemaps.js`) prior to git commits.

21. **Audience-Modularised Documentation Structure**
    Documentation within `docs/` is modularized into dedicated audience volumes including `docs/executive/` (Executive & Financial Blueprint covering 36-month TCO and PDPA 2010 Section 129 / 2025 CBPDT regulatory compliance) and `docs/engineering/` (DevOps Implementation Runbook covering OpenTofu manifests, systemd DNS troubleshooting, Ansible ASIMP hardening playbooks, and EFS mount scripts), using visual architecture badges (`[STRATEGIC FINANCIAL]`, `[SECURITY & COMPLIANCE]`, `[DEVOPS EXECUTION]`) and indexed in `SUMMARY.md`, `docs/SUMMARY.md`, and `src/components/Navigation.astro`.

22. **Automated Documentation CI Workflow**
    An automated documentation CI workflow is located at `.github/workflows/docs-ci.yml` that triggers on master push/PRs. It installs Python dependencies (including `fastmcp`, `pytest`, `playwright`, `mypy`, and `ruff`), Playwright Chromium, executes Ruff linting, Mypy `--strict` type checking, validates Markdown file structure and frontmatter compliance (via `tools/refactor-okf.cjs`), sitemap integrity (via `tools/verify-sitemaps.js`), compiles the Astro SSG site, and executes the full Pytest validation suite.

23. **Pagefind Client-Side Search Integration**
    The project integrates Pagefind WebAssembly (Wasm) client-side search into the build process (`package.json` script `astro build && pagefind --site dist`), generating client search bundles in `dist/pagefind/` and providing a client search route at `/search` (`src/pages/search.astro`) using `src/components/Search.astro`.

24. **Open Knowledge Format (OKF) v0.2 Governance**
    All repository documentation strictly adheres to the Open Knowledge Format (OKF) v0.2 standard (`spec_version: "0.2"`), requiring YAML frontmatter starting on line 1, column 1, containing five trust and freshness pillars (`status`, `stale_after`, `sources`, `generated`), type classification, title, and topics/tags. All string values containing emojis, colons, brackets, or special characters must be enclosed in double quotes.

25. **Google Deep Research & Learn Ingestion Protocol**
    The repository includes the Google Deep Research & Search skill (`.agents/skills/google-deep-research/SKILL.md` and `skills/google-deep-research/SKILL.md`), which governs iterative research workflows, `/learn` knowledge ingestion, and OKF v0.2 frontmatter metadata production.

26. **OKF v0.2 Automated Migration Utility**
    The Python utility `tools/migrate_okf_v02.py` (executable via `uv run python tools/migrate_okf_v02.py`) recursively crawls, parses, formats, and migrates YAML frontmatter across all workspace `.md` files to OKF v0.2 compliance while preserving nested structures and enforcing UK English spelling. The Node.js utility `tools/refactor-okf.cjs` acts as a facade delegating execution to `tools/migrate_okf_v02.py`.

27. **Markdown Quality & Formatting Enforcement**
    The repository enforces Markdown quality standards via a root `.markdownlint.json` configuration file restricting line length (MD013 line_length: 120, ignoring code blocks and tables) and frontmatter title formatting (MD025 regex).

28. **Andrej Karpathy LLM WIKI Paradigm Integration**
    The repository governance includes `docs/governance/LLM-WIKI-ADOPTION.md`, defining the integration strategy between Andrej Karpathy's LLM WIKI paradigm (Ingest, Query, Lint protocols) and the Deep State of Mind (DSOM) Protocol, including spatial memory tracking across `.agents/brain/palace_registry.md`, `.agents/brain/active_context_manifest.md`, and `.agents/brain/checkpoint_summary.txt`.

29. **Automated Integration Testing Suite**
    An automated integration testing suite is located at `tests/test_cms.py` using Pytest. It dynamically checks sitemaps (`tools/verify-sitemaps.js`), frontmatter compliance (`tools/refactor-okf.cjs`), and the HTTP status and DOM elements of all Markdown content pages against the shared Astro preview server on port 4321.

30. **Dual Rulebook AI Agent Gateway**
    Root-level `AGENTS.md` and `.agents/AGENTS.md` rules and configurations are fully synchronized, establishing an AI Agent Gateway, registering all Google Antigravity-compatible Agent Skills, and explicitly documenting the strict OKF compliance rules.

31. **Master Technical Book Design & PDF Compiler Prompt Standard**
    The workspace incorporates master technical book design and PDF compilation standards under DSOM Rules 11 & 22 (`docs/governance/TECHNICAL-BOOK-DESIGN-AND-PDF-COMPILER-PROMPT-GUIDE.md` and `docs/how-to/how-to-produce-a-project-technical-handbook.md`), defining the Terminal & Cloud design system, zero toner waste constraints, Pandoc compilation suites, and pre-rendered vector diagram pipelines.

32. **Deep State of Mind (DSOM) Spatial Memory Specifications**
    The repository's spatial memory (`.agents/brain/knowledge.md`) incorporates full Deep State of Mind (DSOM) specifications, documenting the 19 Entry Points, Tri-Phasic Cognitive Architecture (Active, Twilight, Deep), OKF v0.2 adoption rules, FastMCP Server Integration, OpenWiki Knowledge Graph emulator, and Episodic Record Protocols.

33. **Cross-Platform Agent Skills Interoperability**
    The workspace leverages Google Antigravity-compatible Agent Skills in `.agents/skills/` (conforming to `antigravity.google/docs/skills` and `agentskills.io/home`) with each skill's `SKILL.md` carrying combined OKF/Antigravity frontmatter, and preserves all core Jules knowledge points within both the skills and `.agents/brain/knowledge.md` to ensure seamless cognitive integration.

34. **Dual-Audience Onboarding Framework**
    The repository implements a dual-audience onboarding standard in `START-HERE.md` (and synchronized at `docs/start-here.md`) adapting the Diátaxis practical ethos ('learn-by-doing') for both Human Engineers and Autonomous AI Agents (e.g. Jules, Google Antigravity), defining a 4-quadrant routing matrix, smallest viable task execution pathways, and DSOM context-window governance rules.

35. **LLMs XML Context & Full Asset Compilation**
    The Python utility `tools/llms_txt2ctx.py` parses standard `llms.txt` files and compiles them into structured, standard-compliant XML context documents for AI model ingestion. An associated script `tools/build_llms_full.py` dynamically consolidates all Markdown documentation references inside `llms.txt` to compile a unified, complete `llms-full.txt` asset. Both files are automatically copied and kept synchronized within the `public/` folder.

36. **Diátaxis Documentation Quadrants Layout**
    The repository implements a robust documentation system organized inside `docs/` according to the Diátaxis framework, containing Tutorials (`docs/tutorials/`), How-To Guides (`docs/how-to/`), Reference (`docs/reference/`), and Explanation (`docs/explanation/`) quadrants, coupled with a GitBook-compatible index file `docs/SUMMARY.md` and detailed guidelines in `docs/README.md`.

37. **Ansible Idempotency & FQCN Linting Compliance**
    The Ansible playbook `deploy-static.yml` is 100% compliant with `ansible-lint`. It strictly utilizes Fully Qualified Collection Names (FQCN) for all module actions and specifies `changed_when` parameters on commands to maintain idempotency.

38. **Multi-Host SEO Sitemap Architecture**
    The repository utilizes standard SEO sitemap assets including plain-text files `sitemap.txt` (located at both repository root and `public/sitemap.txt`) and a dynamically built multi-host XML sitemap produced via the Astro endpoint `src/pages/sitemap.xml.ts` that includes Netlify, GitHub Pages, and GitBook publishing platforms.

39. **Sitemap Link Integrity Validation Utility**
    A Node.js validation utility is maintained at `tools/verify-sitemaps.js` to systematically check for formatting anomalies, validate multi-host URL structures, and verify that compiled sitemap links have corresponding physical HTML assets inside the built `dist/` folder to prevent broken links.

40. **RFC 9116 Security Contact & Robots Mapping**
    The repository contains an RFC 9116 compliant security contact file at `public/.well-known/security.txt` and a modernized sitemap crawler index path mapped in `public/robots.txt` to point explicitly to `/sitemap.xml` and `/sitemap.txt` instead of `/sitemap.php`.

41. **Frontend Visual Verification Protocols**
    Visual verification of frontend modifications requires launching the local preview server (`npm run preview` on port 4321) and running Playwright in a Python execution environment to capture and review screenshot outputs.

42. **Node.js 22 Runtime Requirements**
    The project requires Node.js v22 (>=22.12.0) for Astro 7.1 compatibility. The GitHub Actions deployment workflow (`deploy-gh-pages.yml`) utilizes Node.js version 22, and both the `Dockerfile` and `Containerfile` configure their builder stage using `node:22-alpine`.

43. **Centralised Content Navigation Utility**
    The codebase uses a centralized content and navigation utility (`src/utils/navigation.ts`) containing `getCleanSlug` and `getNavigationPages` to handle page ID-to-slug cleaning and menu list generation, eliminating duplicated parsing logic in layout files (`Layout.astro`, `AmpLayout.astro`), page routes (`[...slug].astro`, `amp.astro`), and `sitemap.xml.ts`.

44. **Dual-Pathway Sandbox Branching Logic**
    All automation scripts, deployment pipelines, and Ansible playbooks in the repository must explicitly check for limited sandbox environments (such as the Google Jules container, typically by checking for username 'jules', custom environment variables, or virtualization types) and implement a dual-pathway branching logic. Limited sandbox environments must bypass system-level modifications (such as systemd configurations, global packages installations, or firewall rule adjustments) to focus strictly on unprivileged workspace operations (e.g. local dependencies and compilation), whereas real OS environments are permitted to execute full administrative configurations with no limitations. An Ansible orchestration suite ('ansible.cfg', 'deploy-static.yml', 'inventory/hosts.staging.yml', and 'tools/deploy-static.sh') is configured to demonstrate and enforce this rule.

45. **Cacheable Theme Switching Asset Bundling**
    The main theme-switching logic in `src/layouts/Layout.astro` has had its `is:inline` attribute removed, allowing Astro to compile and bundle it as a cacheable static asset. Early flash prevention remains inline in the `<head>` with its SHA-256 hash whitelisted in Nginx.

46. **GitHub Pages Dynamic Subpath Base URL Handling**
    To support subpath deployments on GitHub Pages (`/CMSForNerd2`) without breaking local development or root-relative cloud environments, `astro.config.mjs` dynamically adjusts the `site` and `base` settings depending on whether `process.env.GITHUB_ACTIONS` is `true`. Layouts (`Layout.astro`, `AmpLayout.astro`) and components (`Navigation.astro`) construct all root-relative paths by dynamically prefixing them with `import.meta.env.BASE_URL`.

47. **Custom Rehype Base Rewriter Plugin**
    A custom Rehype post-processing plugin `rehypeAddBase` is registered inside Astro's markdown processor configuration using `unified` from `@astrojs/markdown-remark` in `astro.config.mjs`. This plugin dynamically rewrites root-relative links within Markdown files during the production build for GitHub Pages, preserving original content files.

48. **GitHub Pages Continuous Deployment Pipeline**
    The project's GitHub Pages deployment is automated via a GitHub Actions workflow (`.github/workflows/deploy-gh-pages.yml`) that runs on pushes to the `master` branch. It installs dependencies with `npm ci`, compiles the static assets using `npm run build`, and publishes the resulting `dist/` directory to the `gh-pages` branch using `peaceiris/actions-gh-pages@v4` with `force_orphan: true`.

49. **Environment Legacy Peer Dependencies Resolution**
    The development environment is configured via a root-level `.npmrc` file specifying `legacy-peer-deps=true` to automatically resolve peer-dependency conflicts (such as between `@vite-pwa/astro` and newer Astro versions like `astro@7.1.6`) across any local, containerised, or cloud deployment environments (e.g., Render.com host environments).

50. **PHP Legacy References Cleanup & Educational Preservation**
    Active, non-historical references to PHP in style comments, routing code, and offline fallback messages are updated or removed to align fully with Astro 7.1. However, all legacy educational laboratory pages and guides in `src/content/pages/` are preserved unchanged to maintain the historical context of the project's origin from the database-free `cmsfornerd` PHP CMS.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
