---
type: "skill"
title: "Markdown Sanitation & Autofix Skill"
name: "markdownlint-autofix"
description: "Self-healing Agent Skill for inspecting, formatting, and auto-correcting Markdown style violations across the repository."
topics: ["markdownlint", "formatting", "sanitation", "agent-skill"]
status: "stable"
sources:
- id: workspace_file
  title: SKILL.md
  url: skills/markdownlint-autofix/SKILL.md
spec_version: "0.2"
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-10-05T14:45:00Z'
tags: ["markdownlint", "formatting", "sanitation", "agent-skill"]
---

# Markdown Sanitation & Autofix Skill

This skill provides automated Markdown linting and style correction using `markdownlint-cli` with workspace rules defined in `.markdownlint.json`.

## Key Capabilities

1. **Style Correction**: Fixes list spacing, fenced code block delimiters, and syntax anomalies across Markdown assets.
2. **Execution Command**:

   ```bash
   ./skills/markdownlint-autofix/run.sh
   ```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-10-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
