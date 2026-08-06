---
okf_version: 0.1
type: "skill"
title: "Documentation Governance Skill"
name: "documentation-governance"
description: "Enforces strict OKF standards, UK English conventions, and prevents orphaned pages in the documentation hierarchy."
timestamp: "2026-08-01T12:00:00Z"
topics: ["documentation", "governance", "okf", "uk-english", "navigation"]
---

# Documentation Governance Skill

This skill governs the writing styles, formatting regulations, and cross-navigational integrity standards for all documentation assets in CMSForNerd2.

## When to use this skill

- When creating or modifying markdown documentation files.
- When reorganising the project's documentation files or layout paths.
- When writing cognitive logs, plans, or commit messages.

## Operational Standards & Procedures

### 1. Strict Standard UK English
Linguistic accuracy must be maintained at all times:
- Documentation and cognitive logs must be authored using Strict Standard UK English spelling and grammar conventions (e.g., *optimisation*, *colour*, *customise*).

### 2. Orphan Prevention & Navigation Mapping
To prevent orphaned documentation:
- Any new governance, architecture, or instructional documents must be explicitly mapped into navigation files: `SUMMARY.md`, `START-HERE.md`, `llms.txt`, and the project `README.md`.

### 3. Open Knowledge Format (OKF) Compliance
All repository documentation strictly adheres to the Open Knowledge Format (OKF) v0.1:
- Every markdown file requires YAML frontmatter containing `okf_version`, `type`, `title`, `timestamp`, and `topics`.

### 4. Educational Preservation Layer
While modernization is a priority, historical lab content is strictly preserved:
- Active, non-historical references to PHP are updated or removed to align fully with Astro 7.1.
- However, all legacy educational laboratory pages and guides in `src/content/pages/` are preserved completely unchanged to maintain the historical context of the project's origin from the database-free `cmsfornerd` PHP CMS.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
