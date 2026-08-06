---
okf_version: 0.1
type: "walkthrough"
title: "CMSForNerd2 Active Walkthrough"
timestamp: "2026-08-01T01:10:00Z"
description: "Active record of steps and decisions made during the modernisation of CMSForNerd2."
topics: ["walkthrough", "history", "brain"]
---

# CMSForNerd2 Modernisation Session Walkthrough

## Milestones Reached:

1.  **Legacy Code Exploration**: Analyzed `CmsForNerd` (PHP 8.4 layout rendering, Pair Logic, and AMP/PWA routing design).
2.  **SSG Framework Selection**: Selected Astro as the target framework due to its lightweight zero-JS output, support for modern CSS3/HTML5, robust content collections, and native View Transitions replacing legacy ajax routers.
3.  **Migration Guide Compilation**: Created `docs/migration-guide.md` summarizing the exact transition playbook for the development team.
4.  **Spatial Environment Configuration**: Set up root navigation and AI registries complying with DSOM rules.
5.  **Astro v6 Content Collections Refactor**: Migrated `src/content/config.ts` to `src/content.config.ts` with the new glob loader, and refactored `[...slug].astro` and `amp.astro` to call `render(page)` instead of `page.render()`.
6.  **Visual Verification**: Successfully ran a preview server on port 4321 and used Playwright to generate and inspect a pixel-perfect full-page screenshot of the homepage.
7.  **Render Deployment Configuration**: Fixed Render deployment issue ("Publish directory dist/ does not exist!" due to skipped build) by adding a static service type configuration in `render.yaml` and documenting the static site deployment steps in `docs/migration-guide.md`.
8.  **Enhancing Repository Onboarding (README)**: Added clear manual static site deployment instructions in the root `README.md` so that users deploying manually through the Render Dashboard can see how to resolve the empty build command issue immediately.
9.  **Windows 11 Setup Navigation Link Typo Rectification**: Corrected the typo "(Herd)" to "(Nerd)" in the Windows 11 Setup navigation item within `src/components/Navigation.astro` to ensure brand consistency and layout professionalism.
10. **Google Jules Sandbox Limitations & Ansible Orchestration Dual-Pathway**: Researched and documented key sandbox limitations in root and agent registries. Created complete Ansible static orchestration files (`ansible.cfg`, `deploy-static.yml`, `inventory/hosts.staging.yml`, `tools/deploy-static.sh`) implementing environment detection and fallback branching options.
