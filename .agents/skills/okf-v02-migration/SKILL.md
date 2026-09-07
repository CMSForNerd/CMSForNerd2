---
type: "skill"
title: "OKF v0.2 Migration & Compliance Standard Skill"
name: "okf-v02-migration"
description: "Governs OKF v0.1 and v0.2 schema validation, machine-readable trust signals, and opportunistic migration protocols."
topics: ["okf", "okf-v02", "frontmatter", "trust-signals", "schema-validation"]
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
tags: ["okf", "okf-v02", "frontmatter", "trust-signals", "schema-validation"]
---

# OKF v0.2 Migration & Compliance Standard Skill

This skill governs the adoption, validation, and maintenance of Open Knowledge Format (OKF) v0.1 and v0.2 metadata schemas across all Markdown files.

## Operational Standards

1. **OKF v0.1 Baseline**:
   - Every Markdown document must start on line 1, column 1 with `---` and conclude with `---`.
   - Must contain required fields: `okf_version`, `type`, `title`, `timestamp`, `topics`.
   - Any string containing emojis, colons, brackets, or special characters must be wrapped in double quotes.

2. **OKF v0.2 Trust Signals**:
   - Opportunistically adopt OKF v0.2 trust fields when modifying or creating documents:
     - `sources`: Array of source file paths or document IDs.
     - `verified`: Boolean indicator of manual or automated verification.
     - `status`: Document status (`"stable"`, `"draft"`, `"deprecated"`).
     - `stale_after`: Expiration ISO date string.

3. **Validation Command**:

   ```bash
   node tools/refactor-okf.cjs
   ```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
