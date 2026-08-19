---
okf_version: 0.1
type: "documentation"
title: "CMSForNerd2 Master Onboarding Map"
timestamp: "2026-08-01T12:00:00Z"
description: "Dual-audience Diátaxis onboarding standard and master entry point for human engineers and autonomous AI agents."
topics: ["onboarding", "diataxis", "navigation", "dsom", "agents"]
nav_order: 1
---

# 🎯 START HERE: CMSForNerd2 Master Onboarding Standard

> *"You do not need to read everything in this repository to make sense of CMSForNerd2, or to start contributing in practice. In fact, we recommend that you do not. The best way to get started with CMSForNerd2 is by applying it — to something, however small."*
>
> — *Adapted from the Diátaxis Principle (Daniele Procida)*

---

## 🏛️ Onboarding Philosophy & Dual-Interface Objective

Welcome to **CMSForNerd2**, a modern, database-free, statically served asset site powered by Astro SSG, HTML5, and CSS3.

Traditional software documentation forces engineers and AI agents to ingest exhaustive knowledge bases before executing a single action. In high-velocity software engineering, this approach creates cognitive overload for human operators and wastes precious context window capacity for autonomous agents.

This onboarding guide adapts the **Diátaxis learn-by-doing ethos** into a **Dual-Interface Standard**. It provides equal operational clarity for two distinct classes of contributors:

1. **Human Engineers**: Pragmatic developers seeking rapid local bootstrapping, structured contribution guidelines, and clear review protocols.
2. **Autonomous AI Agents**: Autonomous agents (including Google Jules, Google Antigravity, and sub-agents) requiring machine-parseable manifests, deterministic execution paths, and bounded context windows.

---

## 🧭 Dual-Audience Entry Matrix (Diátaxis Navigation Grid)

The documentation hierarchy is partitioned into four distinct Diátaxis quadrants. Choose your pathway based on your operational goal and user class:

| Quadrant | Purpose | Human Engineer Pathway | Autonomous AI Agent Pathway |
| :--- | :--- | :--- | :--- |
| **Tutorials**<br>*(Learning-Oriented)* | Skill acquisition & guided hands-on learning. | • [Local Development Quickstart](tutorials/local-development.md)<br>• [Static Site Deployment](tutorials/static-site-deployment.md) | • Ground sandbox environment<br>• Verify Node.js v22 & `.npmrc`<br>• Test `npm run preview` on port 4321 |
| **How-To Guides**<br>*(Problem-Oriented)* | Step-by-step solutions for specific real-world tasks. | • [OKF Metadata Refactoring](how-to/okf-refactoring.md)<br>• [Sitemap Integrity Verification](how-to/sitemap-verification.md)<br>• [Ansible Dual-Pathway Hardening](how-to/ansible-deployment.md) | • Execute `node tools/refactor-okf.cjs`<br>• Execute `node tools/verify-sitemaps.js`<br>• Run `deploy-static.yml` dual pathway |
| **Reference**<br>*(Information-Oriented)* | Technical specifications, API signatures & CLI flags. | • [OKF Crawler API](reference/refactor-okf.md)<br>• [Sitemap Engine Spec](reference/verify-sitemaps.md)<br>• [Deploy Orchestrator API](reference/deploy-static.md)<br>• [LLMS Context Parser CLI](reference/llms-txt2ctx.md) | • Parse `llms.txt` & `AGENTS.md`<br>• Verify OKF v0.1 YAML schemas<br>• Inspect `astro.config.mjs` & `render.yaml`<br>• Read JSDoc & Google docstrings |
| **Explanation**<br>*(Understanding-Oriented)* | High-level architecture, design context & philosophy. | • [Google Jules & Multi-Agent Operations](jules-platform-guide.md)<br>• [Legacy PHP to SSG Modernisation](explanation/modernisation-philosophy.md)<br>• [Spatial Memory & Sandbox Boundaries](explanation/spatial-memory-and-sandbox.md) | • Parse DSOM spatial memory rules<br>• Enforce Google Jules sandbox limits<br>• Respect zero-global memory model |

---

## ⚡ Immediate Action: "The Smallest Viable Task"

Do not attempt to read the entire codebase. Begin immediately with the smallest viable verification task.

### 👤 Human Developer Pathway
To verify your local setup in under 60 seconds, run this 3-step command chain:

```bash
# 1. Install pinned dependencies with legacy peer dependency support
npm ci

# 2. Audit and refactor Open Knowledge Format (OKF) v0.1 frontmatter
node tools/refactor-okf.cjs

# 3. Build static assets and preview locally
npm run build && npm run preview
```

### 🤖 Autonomous AI Agent Pathway
When an issue or task is assigned to an AI agent, execute the following standardized task ingestion protocol:

1. **State Ingestion**: Inspect `.agents/AGENTS.md` and `.agents/brain/task.md` to establish current operational parameters and active context.
2. **Context Bounding**: Locate task-relevant files in `src/` or `docs/`. Read only specific target line ranges using read tools; do not load unreferenced directories into the context window.
3. **Execution & Verification**: Apply targeted code modifications and run verification scripts (`node tools/refactor-okf.cjs`, `npm run build`, and `node tools/verify-sitemaps.js`).
4. **Structured Output**: Format final changes as precise Git merge diffs and submit updates with standard UK English commit messages.

---

## 🛡️ Agent Context Governance (DSOM & OKF Integration)

To guarantee operational stability across multi-agent workflows, all autonomous systems MUST comply with the following context governance principles:

### 1. Minimal Context Window Ingestion
AI agents must maintain context hygiene. Loading the full repository into context windows causes hallucination and degrades reasoning accuracy. Agents must read `.agents/AGENTS.md` for gateway rules, parse `.agents/brain/` for active state, and selectively load target files on demand.

### 2. Deep State of Mind (DSOM) Spatial Memory
All operational memory is zero-global and spatial. Spatial state lives strictly within `.agents/brain/`:
* `task.md`: Tracks active and completed execution steps.
* `walkthrough.md`: Retains historical session anchors.
* `knowledge.md`: Stores domain-specific operational knowledge.

### 3. Multi-Agent Interoperability
CMSForNerd2 supports collaborative agent workflows across **Google Jules**, **Google Antigravity**, and **CI/CD pipelines**. Agents interact via the 8 Google Antigravity-compatible Agent Skills in `.agents/skills/` (`static-security-hardening`, `github-pages-deployment`, `render-deployment`, `dependency-management`, `context7-integration`, `build-preview-workflow`, `documentation-governance`, and `dsom-cognitive-protocol`).

### 4. Open Knowledge Format (OKF) v0.1 Schema Standard
Every Markdown document in this workspace MUST contain valid OKF v0.1 YAML frontmatter starting on line 1, column 1:

```yaml
---
okf_version: 0.1
type: "documentation"
title: "Document Display Title"
timestamp: "2026-08-01T12:00:00Z"
topics: ["topic1", "topic2"]
---
```
*Note: Any string value containing emojis, colons, or brackets must be double-quoted.*

### 5. Standard UK English Rule
All documentation, code comments, commit messages, and cognitive logs MUST strictly adhere to Standard UK English spelling conventions (e.g. *optimisation*, *synchronise*, *behaviour*, *modularise*, *colour*).

---

## 🔗 Core Repository Map

- [../README.md](../README.md) — Executive project summary and architectural overview.
- [SUMMARY.md](SUMMARY.md) — GitBook-compatible documentation index.
- [README.md](README.md) — Full Diátaxis framework specification and index.
- [../AGENTS.md](../AGENTS.md) — Gateway AI agent rulebook and DSOM protocol entry point.
- [../llms.txt](../llms.txt) — High-density context document optimised for LLM crawlers.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
