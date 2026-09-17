---
type: "skill"
title: "Attested Computations Skill"
name: "attested-computations"
description: "Standardised specification for defining and executing Attested Computations in Open Knowledge Format (OKF) v0.2, bridging metrics definitions with executable queries, parameters, runtime contracts, and deterministic attester verification."
topics: ["okf", "attested-computation", "verifiable-analytics", "data-governance", "ai-agents", "verification"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
spec_version: "0.2"
stale_after: "2027-09-17"
sources:
- id: redlinesoft_attested_computations
  title: Attested Computations in Open Knowledge Format (OKF)
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: workspace_file
  title: SKILL.md
  url: .agents/skills/attested-computations/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-17T00:00:00Z'
tags: ["okf", "attested-computation", "verifiable-analytics", "data-governance", "ai-agents", "verification"]
---

# Attested Computations Skill (`attested-computations`)

The `attested-computations` skill provides a standardized operational framework for defining, parameterising, executing, and mechanically attesting sanctioned calculations in Open Knowledge Format (OKF) v0.2.

When AI agents answer complex analytical or financial queries (e.g. fiscal revenue, operational metrics, vector similarity bounds), they must not improvise raw queries. Instead, they reference standalone concepts (`type: Attested Computation`) that guarantee deterministic execution contracts.

---

## Contract Structure of an Attested Computation (OKF v0.2)

Every Attested Computation concept uses standard OKF v0.2 frontmatter with execution metadata:

```yaml
---
type: "Attested Computation"
title: "Revenue for fiscal year"
description: "Recognised revenue for a fiscal year, per Finance's definition."
status: "stable"
spec_version: "0.2"
runtime: "bigquery"
parameters:
  - { name: "year", type: "integer", required: true }
executor:
  resource: "references/skills/run-on-bq.md"
  receipt: ["job_id", "executed_sql", "result"]
attester:
  resource: "references/attesters/sql-equality.py"
generated:
  by: "reference_agent/gemini-2.5-pro"
  timestamp: "2026-09-17T22:53:05Z"
verified:
  by: "Harisfazillah Jamel (LinuxMalaysia)"
  timestamp: "2026-09-17T09:00:00Z"
stale_after: "2027-09-17"
sources:
  - id: "rev-policy"
    resource: "https://wiki.acme/finance/revenue-recognition"
    title: "Revenue recognition policy"
topics: ["finance", "revenue", "okf", "attested-computation"]
---

# Computation

```sql
SELECT SUM(amount) AS revenue
FROM finance.recognized_revenue
WHERE fiscal_year = @year
```

The computation binds only the declared `parameters`, per the recognition policy.[^rev-policy]

[^rev-policy]: Revenue recognition policy
```

---

## The 6-Step Attested Computation Lifecycle

1. **Discover:** Agents locate the computation contract via `type: Attested Computation` or links from narrative documents.
2. **Load:** The consumer reads the contract parameters, runtime target, executor, and attester definitions.
3. **Parameterise:** The agent supplies valid values for declared parameters (e.g. `year: 2026`) without modifying the underlying query string.
4. **Execute:** The executor agent or tool runs the bound query in the target runtime (`bigquery`, `postgres`, `dbt`, `python`) and captures an execution receipt.
5. **Attest:** A deterministic (no-LLM) attester script inspects the receipt to verify that the query executed matches the sanctioned computation without unauthorised modifications.
6. **Gate:** The system surfaces the verified result or refuses stale/failed computations.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
