---
type: "documentation"
title: "The Core AI Rulebook (DSOM) - CMSForNerd2"
description: "OKF-compliant constitution detailing the operational persona, cognitive rules, and spatial memory protocols."
topics: ["agents", "dsom", "rulebook", "constitution", "skills"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: AGENTS.md
  url: AGENTS.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["agents", "dsom", "rulebook", "constitution", "skills"]
---

# AI Agent Registry & Sovereign Gateway

This file describes the agents and tools in our codebase, outlining their operational roles, interaction protocols, and input/output conventions. AI agents (such as Google Jules and Google Antigravity) use this file to understand the codebase and formulate contextually aligned execution plans.

> **Entry Point:** This is the root-level gateway file. The **full cognitive rulebook**, **agent skills**, and all spatial memory reside in `.agents/AGENTS.md`, `.agents/skills/`, and `.agents/brain/`. You MUST navigate there immediately to establish alignment.

---

## Critical Instructions for AI Agents

1. **Read the Full Rulebook**: Navigate immediately to [`.agents/AGENTS.md`](.agents/AGENTS.md) to parse the operational persona, writing styles, and detailed rules governing this project.
2. **Access Spatial Memory**: Read all brain files located in `.agents/brain/` to restore operational context:
    * `task.md` — Active and completed task list (present state).
    * `walkthrough.md` — Session history and Mental Anchors (past state).
    * `knowledge.md` — Sovereign AI Agent Knowledge Base containing all Jules operational and domain-specific knowledge from day 0 to present.
3. **Deploy Agent Skills**: Discover, load, and execute Google Antigravity-compatible Agent Skills from `.agents/skills/` to automate operational procedures.
4. **Execute the 5-Step Knowledge-First Discovery Flow**: Before executing terminal commands or external API queries:
    * Search OKF frontmatter (`topics:` / `description:`) in `.agents/brain/` and `docs/`.
    * Target specific line ranges via read tools.
    * Verify the OKF `timestamp` for contextual relevance.
    * Obtain human consensus if local knowledge is stale.
    * Execute physical terminal commands only when necessary.
5. **Synchronise Both Registries**: Keep this root gateway and `.agents/AGENTS.md` fully in sync to maintain architectural consistency.
6. **Acknowledge Environment & Sandbox Limitations**: When operating in the Google Jules environment (or other restricted, unprivileged container/sandbox settings), be aware of key execution limits (e.g. no persistent OS system setting modifications, headless execution, transient sandbox lifecycle, and limited raw root privileges). Always ensure code and automation scripts (such as Ansible playbooks) detect this environment and gracefully offer options to branch between a limited environment and a real, unconstrained OS.

---

## Google Jules Sandbox & Environment Limitations

When creating, editing, or using automation playbooks, shell scripts, or deployment tools in this workspace, AI agents must respect the specific constraints of the Google Jules environment:

### 1. Key Sandbox Constraints

* **Ephemeral VM Lifecycle**: Tasks execute in temporary, isolated Google Cloud VMs/containers. Any system-wide configuration or package installation is discarded after the task completes.
* **No Persistent OS Modifications**: Though passwordless `sudo` is configured, there is no systemd init system available, and you cannot permanently change system-wide configurations, alter kernel modules, or adjust low-level OS settings.
* **Headless Execution Only**: No physical or virtual graphical display exists. Browser-based tests (e.g., Playwright) must run in strict headless mode.
* **Isolated & Async**: No inter-task coordination or real-time pair-programming is supported.

### 2. Dual-Pathway Branching Rule (Ansible & Shell Code)

To prevent build failures and environment blocks, all automation scripts, Ansible playbooks, and shell scripts **must** dynamically detect whether they are running in a limited environment (like Google Jules) or on a real OS:

* **Detection Mechanism**: Check if the current user is `jules` (e.g., `ansible_env.USER == 'jules'` or `$USER == "jules"`), check for specific environment variables, or inspect virtualisation types (`ansible_virtualization_type in ['docker', 'container', 'lxc']`).
* **Branching Pathways**:
  * *Limited Sandbox (e.g. Google Jules)*: Skip system-wide configurations (such as systemd daemon reloads, raw `ufw` firewall updates, `/etc` configuration overwrites, or APT package installations) and run unprivileged local builds (e.g., `npm install` and local static builds).
  * *Real OS*: Run the complete, unrestricted system-level orchestration, security hardening, and daemon configuration with full privileges and no limitations.

---

## Google Antigravity & AgentSkills.io Agent Skills

By using the open standard for extending agent capabilities, our workspace publishes 14 specialised skills in `.agents/skills/`. Each skill consists of a `SKILL.md` file featuring combined OKF/Antigravity YAML frontmatter and concludes with the standard DSOM footer, bridging Google Jules' and Antigravity's capabilities.
By using the open standard for extending agent capabilities, our workspace publishes 22 specialised skills in `.agents/skills/`. Each skill consists of a `SKILL.md` file featuring combined OKF/Antigravity YAML frontmatter and concludes with the standard DSOM footer, bridging Google Jules' and Antigravity's capabilities.

Agents can discover, activate, and execute these skills on demand as per the open standard documented at `https://antigravity.google/docs/skills` and `https://agentskills.io/home`.

| Skill | Folder Path | Description |
| :--- | :--- | :--- |
| **Static Security Hardening** | `.agents/skills/static-security-hardening/` | Applies static security whitelisting, cryptographic CSP hashes, OWASP standard defensive headers, sitemap/robots mapping, and static performance caching. |
| **GitHub Pages Deployment** | `.agents/skills/github-pages-deployment/` | Manages and automates subpath static deployments to GitHub Pages, excluding Jekyll collision files without breaking root-relative cloud or local development. |
| **Render Deployment** | `.agents/skills/render-deployment/` | Configures and manages Render.com deployments via Docker containerisation or native Free Static Site pathways, and handles Ansible-based staging setups. |
| **Dependency Management** | `.agents/skills/dependency-management/` | Maintains pinned dependency determinism (Astro 7.1.6, Node 22), and resolves peer-dependency conflicts via .npmrc legacy options across all runtime environments. |
| **Context7 Integration** | `.agents/skills/context7-integration/` | Maintains automated documentation indexing and updates utilising Context7 services across CI workflows. |
| **Build and Preview Workflow** | `.agents/skills/build-preview-workflow/` | Guides local compilation, visual and regression testing, sitemap validation, and preview workflows for Astro 7.1 static site generator. |
| **Documentation Governance** | `.agents/skills/documentation-governance/` | Enforces strict OKF standards, UK English conventions, navigation/mapping integrity, comments standards (Google docstrings, JSDoc), and prevents orphaned pages in the documentation hierarchy. |
| **DSOM Cognitive Protocol** | `.agents/skills/dsom-cognitive-protocol/` | Manages Zero-Global Spatial Memory, rulebook synchronisation, and 5-step knowledge-first discovery flows. |
| **DSOM Technical Book Compiler** | `.agents/skills/dsom-technical-book-compiler/` | Compiles documentation suites into publication-grade handbooks (PDF, HTML, EPUB, ODT) using Pandoc and the Terminal & Cloud design system. |
| **Project Technical Book Compiler** | `.agents/skills/project-technical-book-compiler/` | Autonomously synthesizes repository code, Diataxis documentation, and telemetry into print-ready PDF and HTML handbooks. |
| **Code Health & Static Analysis** | `.agents/skills/code-health-linting/` | Governs static analysis, type checking (mypy/tsc), and linter rules (ruff/markdownlint) across the project. |
| **Docstring & JSDoc Standards** | `.agents/skills/docstring-and-jsdoc/` | Enforces PEP-257 Google-style docstrings for Python and detailed JSDoc comments for JavaScript/Node.js utilities. |
| **Unit Testing Suite** | `.agents/skills/unit-testing-suite/` | Governs unit testing across Pytest modules, Ansible compliance, Podman containerization, OKF frontmatter, and Playwright E2E suites. |
| **Google Deep Research & Search** | `.agents/skills/google-deep-research/` | Iterative deep web research, `/learn` knowledge ingestion, and OKF v0.2 trust signal generation with `uv python` token optimisation. |
| **OKF v0.2 Migration & Compliance** | `.agents/skills/okf-v02-migration/` | Governs OKF v0.1 and v0.2 schema validation, machine-readable trust signals, and opportunistic migration protocols. |
| **Docstring & JSDoc Standards** | `.agents/skills/docstring-and-jsdoc/` & `.agents/skills/docstring/` | Enforces PEP-257 Google-style docstrings for Python and detailed JSDoc comments for JavaScript/Node.js utilities. |
| **Unit Testing Suite** | `.agents/skills/unit-testing-suite/` | Governs unit testing across Pytest modules, Ansible compliance, Podman containerization, OKF frontmatter, and Playwright E2E suites. |
| **OKF v0.2 Migration & Compliance** | `.agents/skills/okf-v02-migration/` | Governs OKF v0.1 and v0.2 schema validation, machine-readable trust signals, and opportunistic migration protocols. |
| **Documentation Writing** | `.agents/skills/docs-write/` | Guides creating clear, conversational, reader-focused documentation in Standard UK English adhering to Diátaxis principles. |
| **Documentation Review** | `.agents/skills/docs-review/` | Provides a structured review protocol for verifying technical claims, evidence, and style guide compliance across Markdown docs. |
| **Document Processing & Conversion** | `.agents/skills/docx/` | Manages professional Word document (.docx) creation, tracked changes redlining, comment extraction, and Pandoc Markdown conversion. |
| **OpenAPI 3.1 Spec Generation** | `.agents/skills/openapi-spec-generation/` | Drafts, validates, and maintains OpenAPI 3.1+ specifications, contract compliance, and SDK schema documentation. |
| **AI Hyperparameter Tuning Expert** | `.agents/skills/hyperparameter-tuning-expert/` | Analyzes, optimizes, and debugs deep learning hyperparameters and learning rates across PyTorch and TensorFlow. |
| **Knowledge Base Templates** | `.agents/skills/knowledge-base-templates/` | Reusable templates and structural protocols for codebase knowledge bases and internal wikis using Diátaxis. |
| **Architecture Decision Records** | `.agents/skills/architecture-decision-records/` | Guides writing and maintaining Architecture Decision Records (ADRs) following MADR standards. |
| **Changelog Automation** | `.agents/skills/changelog-automation/` | Automates changelog generation from commits, PRs, and releases following Keep a Changelog and Conventional Commits. |
| **Web Design Guidelines** | `.agents/skills/web-design-guidelines/` | Review UI code for Web Interface Guidelines compliance, accessibility standards, typography, and UX best practices. |

---

## Deep State of Mind (DSOM) Core Principles

The DSOM framework operates on digital sovereignty, structured metacognition, and Git-native operational management:

| Principle | Description |
| :--- | :--- |
| **Zero-Global / Spatial Memory** | No global mutable state. Operational memory lives in `.agents/brain/`. |
| **Open Knowledge Format (OKF)** | All `.md` documents use OKF v0.1/v0.2 YAML frontmatter with explicit timestamps. |
| **Atomic Git Commits** | Every logical action is committed granularly; blanket monolithic commits are strictly forbidden. |
| **Omni-Documentation Sync** | New documents must be mapped to `SUMMARY.md`, `START-HERE.md`, `llms.txt`, and `README.md`. |
| **UK English Dominance** | All files, logs, and messages use standard UK English (`-ise`, `-our`, `-re`). |

---

## Open Knowledge Format (OKF) v0.1 / v0.2 Compliance Guidelines

To prevent parsing anomalies and ensure absolute compatibility across different rendering platforms (including GitHub web view and automated SSG compilation), all Markdown (`.md`) files in the repository must adhere strictly to the following YAML frontmatter rules:

1. **Exact Structure**: The YAML frontmatter block MUST start on line 1, column 1 with exactly three hyphens `---` and conclude with exactly three hyphens `---` on its own line.
2. **Double Quoting Rule**: Any string value containing emojis, colons, brackets, or other special characters MUST be wrapped in double quotes (e.g. `title: "🧠 Deep State of Mind (DSOM)"` or `description: "Standard: UK English | GNU GPL v3"`).
3. **Array Structure**: Arrays (such as `topics` or `tags`) must be preserved in compact, square-bracketed horizontal list formatting with double-quoted strings (e.g. `topics: ["dsom", "documentation", "gateway"]`).
4. **Required Field Schema**: Every document must carry a complete set of five required fields:
   * `okf_version` / `spec_version`: `0.1` or `"0.2"`.
   * `type`: Explicit concept or page classification (e.g., `"documentation"`, `"content_page"`, or `"skill"`).
   * `title`: Human-readable display title (double-quoted if containing special characters).
   * `timestamp`: Date and time string formatted according to ISO 8601, wrapped in double quotes (e.g. `"2026-09-06T00:00:00Z"`).
   * `topics`: An array of associated category tags.
5. **Body Isolation**: The original Markdown body text residing beneath the closing `---` block must remain entirely unaltered.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
