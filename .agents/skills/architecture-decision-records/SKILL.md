---
spec_version: "0.2"
type: "skill"
skill_id: "architecture_decision_records"
name: "architecture-decision-records"
title: "Architecture Decision Records (ADR) Skill"
description: "Guides writing and maintaining Architecture Decision Records (ADRs) following MADR standards for technical decision tracking."
version: "1.0.0"
author: "AI Workspace Assistant"
tags: ["adr", "madr", "architecture", "technical-decisions", "governance"]
status: "stable"
sources:
- id: wshobson_adr
  title: Architecture Decision Records Skill
  url: https://github.com/wshobson/agents
- id: madr_template
  title: Markdown Architectural Decision Records (MADR)
  url: https://adr.github.io/madr/
inputs:
  decision_title:
    type: string
    description: Short descriptive title of the architectural choice.
outputs:
  adr_document:
    type: string
    description: MADR-formatted Architecture Decision Record Markdown document.
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
topics: ["adr", "madr", "architecture", "technical-decisions", "governance"]
---

# Architecture Decision Records Skill (`architecture-decision-records`)

The `architecture-decision-records` skill provides templates and lifecycle governance for capturing significant technical and architectural choices in Architecture Decision Records (ADRs).

## When to Write an ADR

- When adopting or replacing major frameworks, database systems, or deployment architectures.
- When making non-trivial design trade-offs impacting security, performance, or operational workflows.
- *Do not write ADRs for minor version updates or routine bug fixes.*

## MADR Standard Format

Every ADR must include:

1. **Title & Status**: Clear sequential title (e.g., `ADR-001: Adopt Astro SSG for Static Modernisation`) and status (`Proposed`, `Accepted`, `Deprecated`, `Superseded`).
2. **Context & Problem Statement**: The background context and problem triggering the decision.
3. **Decision Drivers**: Factors influencing the choice (e.g. security, zero-cost cloud hosting, performance).
4. **Considered Options**: The alternatives evaluated.
5. **Decision Outcome**: The chosen option, rationale, and positive/negative consequences.

## FAQs

### When should an ADR be marked as Superseded?

When a subsequent architectural decision (recorded in a new ADR) replaces or alters a previously accepted choice.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
