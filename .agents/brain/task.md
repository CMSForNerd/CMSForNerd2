---
type: "task_list"
title: "CMSForNerd2 Active Tasks"
description: "Sovereign tracking list of active and completed tasks in this session."
topics: ["tasks", "track", "progress", "dsom"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: task.md
  url: .agents/brain/task.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-07T03:15:00Z'
tags: ["tasks", "track", "progress", "dsom"]
---

# CMSForNerd2 Tasks

## Session Tasks

- [x] Migrate all workspace Markdown files to OKF v0.2 frontmatter format (`spec_version: "0.2"`, `status`, `stale_after`, `sources`, `generated`).
- [x] Add Google Deep Research & Search skill under `.agents/skills/google-deep-research/SKILL.md` and `skills/google-deep-research/SKILL.md`.
- [x] Implement `tools/migrate_okf_v02.py` with `uv python` execution capabilities and PEP 723 inline script metadata.
- [x] Update `tools/refactor-okf.cjs` with fallback to `python3` for environments where `uv` is not present in PATH.
- [x] Update OKF v0.2 unit and integration test assertions (`tests/unit/markdown.py`, `tests/test_cms.py`).
- [x] Ensure strict PEP-257 Google-style docstrings and Mypy `--strict` type annotations across all Python tools and tests.
- [x] Ensure comprehensive JSDoc comments across Node.js utilities (`tools/refactor-okf.cjs`, `tools/verify-sitemaps.js`).
- [x] Verify complete test pass rate (43/43 tests) across Pytest unit, CMS integration, and Playwright E2E suites.
- [x] Synchronise spatial memory (`.agents/brain/task.md`, `.agents/brain/walkthrough.md`, `.agents/brain/knowledge.md`) for DSOM End of Day (EOD) Palace Sync.
- [x] Research and analyse legacy PHP CmsForNerd architecture.
- [x] Evaluate and compare static site generator (SSG) frameworks (selected Astro).
- [x] Author comprehensive static migration guide in `docs/migration-guide.md`.
- [x] Set up supporting repository structures (`README.md`, `START-HERE.md`, `SUMMARY.md`, `llms.txt`, `AGENTS.md`, and `.agents/AGENTS.md`).
- [x] Migrate `src/content/config.ts` to `src/content.config.ts` and update it to use the new glob loader API.
- [x] Refactor rendering logic in `src/pages/[...slug].astro` and `src/pages/[...slug]/amp.astro` to use Astro v6 content collection rendering API (`render`).
- [x] Verify complete local build and render/screenshot correctness of the home page via Playwright visual verification.
- [x] Complete pre-commit checks and verification.
- [x] Upgrade CMSForNerd2 to Astro 7.1 (specifically "^7.1.6") and verify local build correctness.
- [x] Resolve Render deployment failure regarding "Publish directory dist/ does not exist!" by adding blueprint configurations and documentation for static site deployments.
- [x] Document manual static site settings in root README.md to assist users with dashboard configuration.
- [x] Fix typo "(Herd)" to "(Nerd)" in Windows 11 Setup navigation link within `src/components/Navigation.astro`.
- [x] Modernise the GitHub Pages deployment pipeline and code architecture for CMSForNerd2 (Astro 7.1 SSG).
- [x] Document Google Jules sandbox environment limitations in `AGENTS.md` and `.agents/AGENTS.md`.
- [x] Implement Ansible Static Orchestration suite with dual environment branching logic (`ansible.cfg`, `deploy-static.yml`, `inventory/hosts.staging.yml`, `tools/deploy-static.sh`).
- [x] Adopt Deep State of Mind (DSOM) framework, conducting deep research on DSOM START-HERE specification and entry points.
- [x] Update Jules Knowledge Base in `.agents/brain/knowledge.md` with records 36-41 covering DSOM protocols, 19 Entry Points, Tri-Phasic Mind architecture, and OKF v0.2 opportunistic adoption.
- [x] Update active tasks and walkthrough anchors in `.agents/brain/`.
- [x] Adopt Technical Book Design & PDF Compilation Master Prompt Guide in `docs/governance/`.
- [x] Create How-To Guide for Technical Handbook Production in `docs/how-to/`.
- [x] Implement AI Agent Skills for Technical Book Compiler, Code Health, Docstrings/JSDoc, Unit Testing, and OKF v0.2.
- [x] Perform End of Day (EOD) Palace Sync as per DSOM Protocol.
- [x] Adopt all document-related AI Agent Skills (`docs-write`, `docs-review`, `docstring`, `docx`, `openapi-spec-generation`, `hyperparameter-tuning-expert`, `knowledge-base-templates`, `architecture-decision-records`, `changelog-automation`).
- [x] Synchronise agent gateways (`AGENTS.md`, `.agents/AGENTS.md`) and spatial memory (`.agents/brain/`).
- [x] Audit dependency security vulnerabilities using `npm audit fix` and verify CSP security headers in `nginx/nginx.conf`.
- [x] Refactor Python codebase for strict code health (`tests/` and `tools/`), resolving all `ruff` linting issues and adding strict type annotations for `mypy --strict` compliance.
- [x] Integrate `ruff` and `mypy` static analysis checks into `.github/workflows/docs-ci.yml`.
- [x] Expand Playwright End-to-End testing (`tests/test_e2e.py`) to cover dynamic light/dark theme switching, route navigation, and PWA service worker/manifest offline caching.
- [x] Adopt Vercel `web-design-guidelines` skill into `skills/` and `.agents/skills/`.
- [x] Create skill explanation and UI improvements documentation in `docs/explanation/`.
- [x] Apply UI accessibility and layout stability improvements in `src/components/Widgets.astro`.
- [x] Adopt LLM WIKI Adoption Strategy into `docs/governance/LLM-WIKI-ADOPTION.md`.
- [x] Fix preview server process group teardown in `tests/conftest.py` with `start_new_session=True` and `os.killpg`.
- [x] Implement FastMCP server in `tools/mcp/server.py` to expose live SSG routes, content, sitemap, and spatial memory to AI agents.
- [x] Integrate Pagefind WebAssembly (Wasm) client-side search engine (`npm run build`) and client UI at `/search`.
- [x] Implement WebAssembly Cryptographic & OKF v0.2 Document Processing Studio component and page at `/wasm-studio`.
- [x] Author Diátaxis explanation and how-to guides for FastMCP and WebAssembly tools in `docs/explanation/` and `docs/how-to/`.
- [x] Complete End of Day (EOD) Palace Brain Sync in `.agents/brain/`.
- [x] Adopt Diagram Design Standards skill (`diagram-design-standards`) in `.agents/skills/` and `skills/`.
- [x] Create skill explanation guide in `docs/explanation/diagram-design-standards-skill.md`.
- [x] Synchronise agent registries, documentation navigation, and compiled LLM context files (`llms-full.txt`, `llms-context.xml`).
