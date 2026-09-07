---
spec_version: "0.2"
type: "skill"
title: "Google Deep Research & Search Skill"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: google_deep_research_spec
  title: Google Deep Research & Search Specification
  author: Google Cloud / Agent Architecture Guild
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T23:00:00Z'
tags: ["deep-search", "okf-v02", "research", "learn-protocol", "token-optimisation"]
topics: ["deep-search", "okf-v02", "research", "learn-protocol", "token-optimisation"]
---

# Skill: Google Deep Research & Search

## Overview

Enables Google Jules and autonomous AI agents to perform multi-step, iterative, and deep web research to gather comprehensive intelligence, verify technical facts, and synthesize detailed, context-ready Open Knowledge Format (OKF) v0.2 Markdown documents.

This skill integrates the `/learn` (or "to learn") Knowledge Ingestion Protocol to intercept external URLs, technical specifications, and raw documentation, transforming them into structured, trust-verified OKF v0.2 assets using deterministic `uv python` execution to minimise AI token usage.

## Context Integration & File Capabilities

- **Input Files:** Ingests repository files (codebases, `.md` files, internal spec docs) or attached external documents (PDF, TXT, CSV) to cross-reference or ground web research within project-specific data.
- **Output Files:** Generates structured Markdown (`.md`) reports, system documentation, or configuration files directly into the project's repository workspace for final review in Pull Requests.

## Knowledge Ingestion Protocol (/learn or "to learn")

Whenever a task or prompt includes `/learn [Topic, URL, or Context]` or "to learn":

1. **Intercept & Parse:** Suspend standard conversational behavior. Parse the target URL, raw text, or technical spec.
2. **Transform to OKF v0.2:** Extract core technical truths and generate/update `.md` documents with the **Five Trust & Freshness Pillars**:
   - `spec_version`: Explicitly set to `"0.2"`.
   - `type`: Functional classification (`"tutorial"`, `"how-to"`, `"reference"`, `"explanation"`, `"skill"`).
   - `title`: Concise title string.
   - `status`: Lifecycle state (`"stable"`, `"draft"`, `"deprecated"`).
   - `stale_after`: ISO date string (YYYY-MM-DD), typically set to 6-12 months out.
   - `sources`: Structural list (`id`, `title`, `author`, `url`).
   - `generated`: Provenance metadata (`by`, `timestamp`).
3. **Diátaxis & UK English Alignment:** Structure prose according to Diátaxis quadrants and adhere strictly to UK English spelling conventions (*optimise*, *organise*, *behaviour*).
4. **Token Optimisation via `uv python`:** Offload scanning, metadata parsing, and validation to deterministic `uv python` scripts (`tools/migrate_okf_v02.py`) to eliminate unnecessary LLM context consumption.

## Workspace Quality Enforcement (markdownlint-cli)

Before presenting generated knowledge assets or finalizing file writes:

1. Programmatically invoke `npx --no-install markdownlint-cli --fix <filename.md>` or run script-level linting.
2. Ensure compliance with `.markdownlint.json`.
3. Verify frontmatter starts cleanly on Line 1, Column 1 with `---`.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
