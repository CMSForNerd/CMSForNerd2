---
spec_version: "0.2"
type: "skill"
title: "Mermaid Diagram Validation Skill"
name: "mermaid-validation"
description: "Validates Mermaid diagram syntax across Markdown files in a headless Node.js environment using the official Mermaid parser and jsdom, ensuring zero broken rendering on GitHub or SSG builds without Chromium overhead."
topics: ["mermaid", "validation", "diagrams", "markdown", "documentation", "quality"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
stale_after: "2027-03-06"
sources:
- id: garden_mermaid_validation
  title: Mermaid Validation Skill
  url: https://github.com/kriscendobot/garden/tree/main/skills/mermaid-validation
- id: skills_rest_mermaid_validation
  title: skills.rest mermaid-validation
  url: https://skills.rest/skill/mermaid-validation
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["mermaid", "validation", "diagrams", "markdown", "documentation", "quality"]
---

# Mermaid Diagram Validation Skill (`mermaid-validation`)

The `mermaid-validation` skill ensures all embedded Mermaid diagrams in Markdown files parse cleanly using the official Mermaid syntax rules. By running locally in a headless Node.js environment backed by `jsdom`, it catches grammar anomalies before git commits without requiring heavy browser binaries like Chromium or Puppeteer.

---

## What Problem Does It Solve?

In complex documentation systems, invalid Mermaid syntax (such as syntax typos, unclosed brackets, or unescaped characters in node labels) breaks diagram rendering on GitHub web views and SSG static builds. Traditional rendering validation relies on Puppeteer or full browser instances, which frequently fail or timeout in containerised CI/CD environments.

`mermaid-validation` solves this by using the official `mermaid` JavaScript library inside a lightweight `jsdom` virtual DOM context.

---

## Key Capabilities & Execution Model

1. **Headless Grammar Parsing:** Extract all ````mermaid ... ```` code blocks from `.md` files and validate them against `mermaid.parse()`.
2. **Container-Friendly Execution:** Runs cleanly in CI/CD pipelines, pre-commit hooks, and restricted sandboxes (e.g., Google Jules container) without GUI dependencies.
3. **Synergy with Diagram Design Standards:** Integrates seamlessly with `diagram-design-standards` (Cathryn Lavery principles), checking that the Git-native Mermaid block in 4-tier visual deliverables is syntactically valid.

---

## Quick Start & Usage Instructions

Execute the repository validator script to scan all Markdown files across the codebase:

```bash
node tools/validate-mermaid.js
```

### Script API & Configuration (`tools/validate-mermaid.js`)

The validator utility scans recursively across `docs/`, `src/content/`, `.agents/`, and root directories (excluding `node_modules`, `.git`, `dist`, `.astro`), extracting every Mermaid code block and asserting syntactical validity via `mermaid.parse()`.

---

## Operational Guidelines & Workflow Integration

* **Pre-Commit Hook Integration:** Add `node tools/validate-mermaid.js` to `tools/eod-palace.sh` or local Git commit hooks to block invalid diagrams before commit.
* **4-Tier Deliverable Compliance:** Ensure Mermaid code blocks in technical documentation conform to the multi-tier sequence required by `diagram-design-standards` (ASCII tree, raw SVG, Mermaid block, summary routing table).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
