---
type: "skill"
title: "Code Health and Static Analysis Skill"
name: "code-health-linting"
description: "Governs code health, static analysis, type checking (mypy/tsc), and linter rules (ruff/markdownlint) across the project."
topics: ["code-health", "linting", "static-analysis", "ruff", "markdownlint"]
status: "stable"
sources:
- id: dsom_agents_rulebook
  title: The Core AI Rulebook (DSOM)
  path: .agents/AGENTS.md
spec_version: "0.2"
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-05T08:00:00Z'
tags: ["code-health", "linting", "static-analysis", "ruff", "markdownlint"]
---

# Code Health and Static Analysis Skill

This skill enforces code health, static analysis, and code quality standards across Python, JavaScript/Node.js, Shell, and Markdown files in the repository.

## Operational Standards

1. **Python Code Health**:
   - Strictly adhere to PEP-8 and PEP-257 style standards.
   - Enforce type hinting and `mypy` strict type checking compatibility.
   - Code refactoring must preserve functional behavior while improving readability and cleanliness.

2. **Markdown Linting & OKF Schema**:
   - Maintain MD031 compliance (surrounding code fences with blank lines).
   - Enforce OKF v0.1 and v0.2 frontmatter metadata rules across all `.md` files.

3. **Shell Script Security & Hygiene**:
   - Set strict error flags (`set -euo pipefail`) in Bash scripts.
   - Include complete headers, requirements, usage instructions, and inline comments.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
