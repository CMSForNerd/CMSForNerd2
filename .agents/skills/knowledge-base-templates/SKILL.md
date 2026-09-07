---
spec_version: "0.2"
type: "skill"
skill_id: "knowledge_base_templates"
name: "knowledge-base-templates"
title: "Knowledge Base Structure & Templates Skill"
description: "Provides reusable templates and structural protocols for codebase knowledge bases and internal wikis using Diátaxis."
version: "1.0.0"
author: "AI Workspace Assistant"
tags:
- knowledge-base
- diataxis
- wiki
- templates
- documentation
status: "stable"
sources:
- id: "rp1_kb_templates"
  title: RP1 Knowledge Base Templates
  url: https://github.com/rp1-run/rp1
- id: "diataxis_framework"
  title: "Di\xE1taxis Documentation Framework"
  url: https://diataxis.fr
inputs:
  document_type:
    type: string
    description: "Di\xE1taxis quadrant type (tutorial, how-to, reference, explanation)."
outputs:
  template_markdown:
    type: string
    description: Structured OKF-compliant Markdown document template.
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
topics:
- knowledge-base
- diataxis
- wiki
- templates
- documentation
---

# Knowledge Base Structure & Templates Skill (`knowledge-base-templates`)

The `knowledge-base-templates` skill governs the creation, structural organization, ownership, and maintenance of project knowledge bases and internal wikis.

## Operational Guidelines & Diátaxis Alignment

1. **Apply the Diátaxis Quadrant System**:
   - **Tutorials (`docs/tutorials/`)**: Learning-oriented guides for newcomers.
   - **How-To Guides (`docs/how-to/`)**: Task-oriented steps for completing specific goals.
   - **Reference (`docs/reference/`)**: Information-oriented specs, APIs, and command lists.
   - **Explanation (`docs/explanation/`)**: Understanding-oriented architecture and design concepts.

2. **Knowledge Base Governance & Pruning**:
   - Every knowledge base page must carry explicit frontmatter, an owner, and cross-navigation links (`SUMMARY.md`, `START-HERE.md`).
   - Identify and prune stale or duplicated pages rather than creating overlapping content.

## FAQs

### How are orphaned pages prevented?

Map every new knowledge base page into `docs/SUMMARY.md`, `SUMMARY.md`, `START-HERE.md`, `llms.txt`, and `README.md`.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
