---
spec_version: "0.2"
type: "skill"
title: "Agent Charter Reskilling and Procedural Refactoring Skill"
name: "reskill"
description: "Audits AI agent charters and operational histories to extract procedural knowledge, checklists, and duplicated instructions into reusable Agent Skills, slimming charters to core identity, ownership, and behavioral boundaries while optimizing token efficiency."
topics: ["reskill", "agent", "charter", "token-optimisation", "procedural-knowledge", "refactoring"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
stale_after: "2027-03-06"
sources:
- id: aithena_reskill
  title: Reskill Agent Skill
  url: https://github.com/jmservera/aithena/tree/main/.squad/skills/reskill
- id: skills_rest_reskill
  title: skills.rest reskill
  url: https://skills.rest/skill/reskill
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["reskill", "agent", "charter", "token-optimisation", "procedural-knowledge", "refactoring"]
---

# Agent Charter Reskilling & Refactoring Skill (`reskill`)

The `reskill` skill provides an automated and structured methodology for auditing AI agent charters, extracting repetitive procedural knowledge, checklists, and operational workflows into modular, reusable Agent Skills.

---

## What Problem Does It Solve?

As agentic AI deployments scale across repositories, agent charters often suffer from prompt bloat. Charters become overloaded with repetitive step-by-step instructions (e.g., how to run test suites, format pull request comments, validate OKF frontmatter, or check sitemap links). This duplication:

1. **Inflates Token Overhead:** Consumes valuable context window space before execution begins.
2. **Dilutes Agent Focus:** Increases the probability of prompt drift and non-deterministic behavior.
3. **Creates Maintenance Friction:** Requires updating identical procedural rules across multiple agent charters when workflow steps evolve.

---

## Core Capabilities & Operational Protocol

1. **Charter Audit & Friction Identification:** Scans agent charters (`AGENTS.md`, `.agents/AGENTS.md`, and system prompts) for embedded step-by-step checklists, CLI invocation guides, and formatting templates.
2. **Procedural Knowledge Extraction:** Isolates reusable procedures into self-contained `SKILL.md` packages inside `.agents/skills/<skill-name>/` carrying OKF v0.2 frontmatter.
3. **Charter Slimming:** Replaces inline procedural instructions in charters with clean skill registry references, leaving charters focused strictly on identity, ownership, authority boundaries, and stop conditions.
4. **Token Efficiency Optimization:** Reduces token footprint per agent invocation by up to 60-80% through dynamic skill loading.

---

## Step-by-Step Reskilling Workflow

### Step 1: Analyze Target Charters
Identify charters or system prompts containing procedural instructions, such as:
* Pull request formatting and git commit rules.
* Test execution commands (`pytest`, `mypy`, `ruff`, `npm run build`).
* Frontmatter validation or documentation formatting protocols.

### Step 2: Formulate the Reusable Skill Package
Create a new directory `.agents/skills/<skill-name>/SKILL.md` and copy to `skills/<skill-name>/SKILL.md`:
* Add OKF v0.2 YAML frontmatter.
* Define input parameters, execution steps, and verification commands.
* Append the standard Deep State of Mind (DSOM) governance footer.

### Step 3: Slim the Agent Charter
Update the original charter file to reference the new skill in the Agent Skill Registry table. Strip out line-by-line procedural steps from the charter body.

---

## Operational Guidelines

* **Preserve Identity and Authority:** Never extract an agent's core identity, named human owners, decision rights, or stop conditions into a skill. Those MUST remain in the primary charter document.
* **Registry Synchronization:** Always maintain complete synchronization between `.agents/skills/` and `skills/` directories.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
