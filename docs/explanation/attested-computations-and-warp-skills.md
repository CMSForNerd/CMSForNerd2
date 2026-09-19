---
type: "explanation"
title: "Attested Computations and Warp Agent Skills Standard"
description: "Comprehensive guide to Attested Computations in Open Knowledge Format (OKF) v0.2 and Warp/OpenViking Agent Skills capabilities within CMSForNerd2."
topics: ["okf", "attested-computations", "warp", "openviking", "agent-skills", "verification"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
spec_version: "0.2"
stale_after: "2027-09-17"
sources:
- id: redlinesoft_attested_computations
  title: Attested Computations in Open Knowledge Format (OKF)
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: warp_skills_docs
  title: Warp Agent Skills Capability Guide
  url: https://docs.warp.dev/agents/capabilities/skills/
- id: openviking_skills_api
  title: OpenViking Skills API Reference
  url: https://docs.openviking.ai/en/api/04-skills
- id: workspace_file
  title: attested-computations-and-warp-skills.md
  url: docs/explanation/attested-computations-and-warp-skills.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["okf", "attested-computations", "warp", "openviking", "agent-skills", "verification"]
---

# Attested Computations and Warp Agent Skills Standard

> **Classification:** Architectural Explanation & AI Skill Adoption Blueprint
> **Standard:** OKF v0.2 & Deep State of Mind (DSOM) AI Protocol
> **Target Audience:** Systems Architects, Autonomous AI Agents (Jules, Warp Agent, OpenViking), and SREs

---

## 1. Overview & Strategic Purpose

As AI agents operate within software repositories, answering complex analytical queries (such as calculating 36-month TCO, verifying SLA compliance, or computing vector embedding bounds) requires absolute mathematical precision. Agents must not improvise raw SQL queries or alter calculation formulas.

This guide details two core capabilities adopted into the codebase:
1. **Attested Computations in OKF v0.2:** Mechanically verifiable calculation contracts separating metric definitions from runtime execution.
2. **Warp & OpenViking Agent Skills:** Reusable, parameterised instructions stored under `.agents/skills/` that agents discover and execute autonomously or via slash commands (`/{skill-name}`).

---

## 2. Attested Computations Contract Architecture (OKF v0.2)

An **Attested Computation** is a standalone concept (`type: Attested Computation`) containing a sanctioned calculation. Instead of embedding unverified raw scripts in narrative documents, OKF v0.2 defines an execution and verification contract.

```yaml
---
type: "Attested Computation"
title: "Fiscal Revenue Calculation"
description: "Recognised fiscal revenue computed via sanctioned Finance policy."
status: "stable"
spec_version: "0.2"
runtime: "postgres"
parameters:
  - { name: "fiscal_year", type: "integer", required: true }
executor:
  resource: "references/skills/run-postgres-query.md"
  receipt: ["job_id", "executed_sql", "result"]
attester:
  resource: "tools/attesters/verify-sql-equality.py"
stale_after: "2027-09-17"
---

# Computation

```sql
SELECT SUM(amount) AS revenue
FROM finance.recognized_revenue
WHERE fiscal_year = @fiscal_year
```
```

### The 6-Step Verification Lifecycle:
1. **Discover:** Agent locates `type: Attested Computation`.
2. **Load:** Agent reads contract parameters and target runtime.
3. **Parameterise:** Agent binds parameter variables (`fiscal_year: 2026`) without modifying SQL body.
4. **Execute:** Executor runs query and captures execution receipt.
5. **Attest:** Deterministic (no-LLM) script compares execution receipt against contract SQL.
6. **Gate:** Output is accepted or rejected if modified or stale.

---

## 3. Warp and OpenViking Agent Skills Integration

Warp and OpenViking Agent Skills enable reusable task instructions discovered automatically from `.agents/skills/{skill-name}/SKILL.md`.

```
.agents/skills/
├── attested-computations/
│   └── SKILL.md
├── diagram-design-standards/
│   └── SKILL.md
└── warp-agent-skills/
    └── SKILL.md
```

### Skill Parameter Substitution Syntax:
- `$ARGUMENTS`: Full raw argument string.
- `$ARGUMENTS[N]` or `$N`: Nth whitespace-separated argument (e.g., `$0` = first argument).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
