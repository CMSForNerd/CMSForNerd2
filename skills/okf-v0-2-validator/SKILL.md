---
type: "skill"
title: "OKF v0.2 Frontmatter & Trust Signal Validator Skill"
name: "okf-v0-2-validator"
description: "Self-healing Agent Skill for inspecting, validating, and migrating workspace Markdown assets to Open Knowledge Format (OKF) v0.2 trust signal compliance."
topics: ["okf-v02", "frontmatter", "trust-signals", "validation", "agent-skill"]
status: "stable"
sources:
- id: workspace_file
  title: SKILL.md
  url: skills/okf-v0-2-validator/SKILL.md
spec_version: "0.2"
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-10-05T14:45:00Z'
tags: ["okf-v02", "frontmatter", "trust-signals", "validation", "agent-skill"]
---

# OKF v0.2 Frontmatter & Trust Signal Validator Skill

This skill provides an automated, repeatable validation procedure for auditing and enforcing Open Knowledge Format (OKF) v0.2 YAML frontmatter standards across all Markdown (`.md`) assets in the workspace.

## Key Capabilities

1. **Frontmatter Invariant Verification**: Asserts that YAML frontmatter begins at line 1, column 1, and contains `spec_version: "0.2"`, `type`, `title`, `description`, `status`, `stale_after`, `sources`, `generated`, and `tags`/`topics`.
2. **String Quote Normalisation**: Wraps special characters, colons, emojis, and brackets in double quotes.
3. **Execution Command**:

   ```bash
   ./skills/okf-v0-2-validator/run.sh
   ```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-10-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
