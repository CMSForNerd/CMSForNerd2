---
spec_version: "0.2"
type: "documentation"
title: "AI Agent Charter Template and Operating Governance Standard"
description: "Comprehensive enterprise AI agent charter template adapted from Alignbase specification, defining explicit purpose, human ownership, bounded authority, context boundaries, fail-closed stop conditions, and release controls."
topics: ["governance", "agent-charter", "alignbase", "dsom", "ai-safety", "authority-boundaries"]
status: "stable"
stale_after: "2027-03-06"
sources:
- id: alignbase_charter_template
  title: Alignbase AI Agent Charter Template
  url: https://alignbase.ai/blogs/ai-agent-charter-template/
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["governance", "agent-charter", "alignbase", "dsom", "ai-safety", "authority-boundaries"]
---

# AI Agent Charter Template & Operating Governance Standard

This document establishes the official **AI Agent Charter Template** for `CMSForNerd2`, derived from the enterprise Alignbase AI Agent Charter specification and aligned with the Deep State of Mind (DSOM) governance framework.

An AI Agent Charter serves as the approved operating contract for a specific agent-workflow-environment combination. It transforms generic AI prompts into explicit, testable boundaries governing purpose, human ownership, action authority, tool access, context boundaries, human checkpoints, fail-closed stop paths, and retirement procedures.

---

## AI Agent Charter Structural Sections

```
┌────────────────────────────────────────────────────────────────────────┐
│                      AI AGENT CHARTER TEMPLATE                         │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Record Metadata & Unique Identity (Agent ID, Workflow ID, Env)      │
│ 2. Purpose & Intended Outcome (Bounded business task, affected users)  │
│ 3. Named Human Ownership & Decision Rights (Business, Tech, Risk)      │
│ 4. Bounded Authority & Prohibited Actions (Read, Draft, Write, Exec)   │
│ 5. Identity, Tools & Credential Scope (Attributable non-secret tokens) │
│ 6. Data & Context Boundaries (Knowledge, Skills, Working Memory)       │
│ 7. Human Checkpoints & Review Gates (Triggers, decision expiry, diffs) │
│ 8. Release Binding, Risk Tier & Test Evidence (Version-bound approvals)│
│ 9. Continuous Monitoring & Audit Evidence (Logs, metrics, telemetry)   │
│ 10. Fail-Closed Stop Path & Recovery (Revocation, queues, fallback)    │
│ 11. Dependencies, Delegation & Change Control (CHILD agents, MCPs)     │
│ 12. Periodic Review, Reconciliation & Retirement (Decommissioning)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Standard Charter Specification Template

```markdown
# AI Agent Charter: [Agent Name] - [Workflow Name]

## 1. Charter Record & Metadata
- **Charter ID:** CHARTER-2026-[WORKFLOW-ID]
- **Agent Identity / ID:** `agent-[name]-[env]`
- **Target Environment:** Development / Staging / Production
- **Lifecycle Status:** Draft / Conditional Approval / Active / Suspended / Retired
- **Effective Date:** [ISO 8601 Date]
- **Review Cadence:** Quarterly / Event-Driven

## 2. Bounded Purpose & Intended Outcomes
- **Approved Business Task:** [Explicit description of the single business workflow]
- **Initiating Principals:** [Allowed users, service accounts, or trigger webhooks]
- **Affected Stakeholders:** [People or downstream systems impacted by actions]
- **Success Criteria & Volume Thresholds:** [Max execution spend, rate limits, latency]
- **Out-of-Scope Uses:** [Explicitly prohibited adjacent tasks]

## 3. Named Human Ownership & Decision Rights
- **Business Owner:** [Named Person & Role]
- **Technical Lead:** [Named Engineer & Role]
- **Security & Risk Approver:** [Named Security Officer & Role]
- **Decision Authority Matrix:**
  - *Purpose / Charter Changes:* Business Owner + Technical Lead
  - *Emergency Suspension / Stop:* Any Named Owner / Security Officer
  - *Release Activation:* Technical Lead + Security Approver

## 4. Enforceable Authority & Prohibited Actions
### Approved Actions
| System / Target | Action Type | Scope / Boundaries | Human Checkpoint Required? |
| :--- | :--- | :--- | :--- |
| `src/content/` | Create / Edit | Markdown content files | No (Automated PR diff review) |
| `tools/` | Execute Script | Unprivileged local Python/Node | No (Sandboxed execution) |
| `/etc/` | Write / Edit | System configuration | YES (Human approval required) |

### Prohibited Actions
- The agent MUST NEVER modify root system configurations or systemd daemons in sandbox environments.
- The agent MUST NEVER expose credentials, tokens, or private keys in logs or git commits.
- The agent MUST NEVER self-grant extended permissions or bypass defined test suites.

## 5. Identity, Tools & Credentials
- **Authenticated Principal:** `service-account-jules` / `agent-antigravity`
- **Tool Adaptor Scope:** Local CLI, FastMCP Gateway, Pytest Test Runner
- **Credential Storage:** Environment secrets manager (Never committed in code)

## 6. Data & Context Boundaries
- **Data Classification Limit:** Public / Internal Engineering Documentation
- **Knowledge Resources:** `.agents/brain/knowledge.md`, `docs/`
- **Skill Packages:** `.agents/skills/*`
- **Working Memory Baseline:** `.agents/brain/active_context_manifest.md`

## 7. Human Checkpoints & Review Gates
- **Trigger Condition:** Structural schema changes, system-level modifications, or test failures.
- **Reviewer Required:** Technical Lead or Security Approver.
- **Diff Presentation:** Single Git merge diff block or explicit PR comment.
- **Fail-Closed Rule:** Expiry without response forces session rollback and halt.

## 8. Release Binding, Risk & Testing Evidence
- **Risk Tier:** Low (SSG Documentation) / Medium (IaC Manifests) / High (Production Deployments)
- **Test Suite References:** `python3 -m pytest tests/`, `tools/eod-palace.sh`
- **Release Verification ID:** [Commit Hash or Build Artifact ID]

## 9. Monitoring & Audit Trail
- **Log Destination:** `.agents/brain/checkpoint_summary.txt`
- **Tracked Telemetry:** Token usage metrics, files mutated, test results.

## 10. Fail-Closed Stop Path & Containment
- **Stop Triggers:** Unhandled test exceptions, unapproved system alteration attempts, security guardrail violations.
- **Containment Method:** Revoke transient session token, terminate sub-processes, reset workspace via `git reset --hard`.

## 11. Dependencies, Delegation & Change Control
- **Upstream Dependencies:** Node.js v22, Python 3.12, FastMCP Server
- **Delegated Child Agents:** Hello World Agent, Sub-agents
- **Material Change Trigger:** Change in purpose, tool scope, or authorization boundaries requires full charter re-approval.

## 12. Review, Reconciliation & Retirement
- **Reconciliation Audit:** Compare charter authorization against active Git commit logs and system evidence.
- **Retirement Protocol:** Revoke identity credentials, purge temporary cache, archive charter record with status `Retired`.
```

---

*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
