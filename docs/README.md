---
okf_version: 0.1
type: "documentation"
title: "CMSForNerd2 Documentation System"
description: "High-quality production-ready documentation system adhering to the Diátaxis Framework."
timestamp: "2026-08-01T14:35:00Z"
topics: ["diataxis", "documentation", "framework", "architecture"]

nav_order: 1
---

# 📚 CMSForNerd2 Documentation System

Welcome to the **CMSForNerd2** documentation system. This repository utilizes the **Diátaxis Framework**, a systematic approach to technical documentation design.

---

## 🏛️ What is the Diátaxis Framework?

The Diátaxis Framework organizes documentation into four distinct quadrants, each serving a unique user need and operational context:

```
                  PRACTICAL
                     ▲
                     │
     TUTORIALS       │      HOW-TO GUIDES
  (Learning-oriented)│   (Problem-oriented)
                     │
◀────────────────────┼────────────────────▶
                     │
    EXPLANATION      │      REFERENCE
  (Understanding-    │   (Information-
     oriented)       │      oriented)
                     │
                     ▼
                THEORETICAL
```

1.  **Tutorials (`docs/tutorials/`)**: Guided, step-by-step learning lessons designed to help beginners start using the system. They are **learning-oriented** and focus on immediate execution success.
2.  **How-To Guides (`docs/how-to/`)**: Problem-oriented, practical directions designed to solve specific real-world tasks. They are **goal-oriented** and assume basic familiarity.
3.  **Reference Material (`docs/reference/`)**: Key information, CLI parameters, API signatures, and specs for every tool. They are **information-oriented** and designed for rapid lookup.
4.  **Explanation (`docs/explanation/`)**: Conceptual context and architecture design decisions behind the tools and project layout. They are **understanding-oriented**.

---

## 🧭 Navigational Index

To explore our documentation system, navigate using the following curated pathways:

*   **Learning Pathways (Tutorials)**
    *   [Local Development Quickstart](tutorials/local-development.md) — Learn how to set up, build, and run the CMSForNerd2 workspace locally.
    *   [Static Site Deployment](tutorials/static-site-deployment.md) — Step-by-step lesson to deploy the CMS statically onto cloud hosting.
*   **Practical Workflows (How-To Guides)**
    *   [OKF Frontmatter Refactoring](how-to/okf-refactoring.md) — How to automatically validate and repair Markdown metadata.
    *   [Sitemap Verification](how-to/sitemap-verification.md) — How to verify that generated sitemap links match built static files.
    *   [Ansible Static Security Hardening](how-to/ansible-deployment.md) — How to configure and deploy a production static site with dual-pathway branching.
*   **Technical Specifications (Reference)**
    *   [`refactor-okf.cjs` API](reference/refactor-okf.md) — Reference specifications for the YAML validation crawler.
    *   [`verify-sitemaps.js` API](reference/verify-sitemaps.md) — Reference specifications for the sitemap testing engine.
    *   [`deploy-static.sh` Orchestrator](reference/deploy-static.md) — Specifications for the dual-pathway bash deployment orchestrator.
    *   [`llms_txt2ctx.py` CLI](reference/llms-txt2ctx.md) — Parser interface specifications for generating XML contexts.
*   **Conceptual Depth (Explanation)**
    *   [Legacy PHP to SSG Modernisation](explanation/modernisation-philosophy.md) — Why we migrated from PHP to Astro.
    *   [Spatial Memory & Dual Pathways](explanation/spatial-memory-and-sandbox.md) — Explaining sandbox boundaries and Google Jules compatibility.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
