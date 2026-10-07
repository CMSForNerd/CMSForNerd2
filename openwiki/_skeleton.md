---
type: "documentation"
title: "OpenWiki Documentation Skeleton & Subsystem Index"
description: "Authoritative inventory ranking, planned page tree, and evidence briefs for the DSOM codebase."
topics: ["openwiki", "skeleton", "dsom", "inventory"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: _skeleton.md
  url: openwiki/_skeleton.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: '2026-10-05T16:29:09Z'
tags: ["openwiki", "skeleton", "dsom", "inventory"]
---
# OpenWiki documentation skeleton

## Inventory and ranking

| Rank | System | Why it is substantial | Primary evidence |
| --- | --- | --- | --- |
| 1 | DSOM governance, agent startup, and brain | Repository’s primary public purpose and operational control plane; root agent entrypoints route here. | `README.md`, `AGENTS.md`, `.agents/AGENTS.md`, `.agents/brain/` |
| 2 | Session lifecycle and Palace consolidation | Governs persistent state, SOD/EOD handoffs, Git-history-derived knowledge, and human/AI boundaries. | `tools/reanimate.sh`, `tools/eod-palace.sh`, `playbooks/` |
| 3 | Documentation publication and delivery | Public-facing product surface delivered through Astro SSG, GitHub Pages, Render, and SEO files. | `astro.config.mjs`, `.github/workflows/deploy-gh-pages.yml`, `render.yaml`, `SUMMARY.md`, tests |
| 4 | Ansible baseline and control-node operations | Concrete executor implementation, inventory topology, common role, and preflight. | `ansible.cfg`, `inventory/`, `playbooks/` |
| 5 | CI automation and integrations | Changes brain state and generated docs; owns security scan and scheduled OpenWiki update. | `.github/workflows/`, `.gitlab-ci.yml` |
| 6 | Local MCP and skill/workflow extension model | External-agent access surface and reusable procedure catalogue. | `tools/mcp/server.py`, `.agents/skills/`, `skills/` |
| 7 | Tests and cross-platform guardrails | Regression suite codifies documentation, OKF, signature, symlink and deployment constraints. | `tests/`, `package.json` |

## Planned tree

- `quickstart.md` — Final entrypoint: repository map, task-routing table, canonical links, focused validation commands.
- `architecture/overview.md` — DSOM scope, three-pillar operating model, component boundaries, authoritative sources.
- `governance/agent-operation.md` — Dual `AGENTS.md` registry, 27-rule operating constraints, boot/discovery ordering.
- `memory/session-and-palace.md` — Brain artifact ownership, active-context, SOD/reanimation, EOD/hibernation, Palace Sync.
- `automation/ansible-baseline.md` — Inventory tiers, `ansible.cfg`, preflight/common playbooks, WSL2 control node.
- `automation/tools-and-privacy.md` — Native Bash/PowerShell ritual tools, Privacy Guardian, onboarding/reset boundaries.
- `integrations/mcp-and-ci.md` — FastMCP server contract, Context7 RAG endpoints, GitHub Actions workflows.
- `publishing/documentation-delivery.md` — Multi-channel publication, GitHub Pages, Render, SEO sitemaps.
- `quality/verification.md` — Python test-suite map, OKF/BOM/quoting/symlink assertions.

## Evidence briefs completed before drafting

| Planned page | Entry/composition inspected | Implementation/data/config inspected | Upstream/downstream and tests inspected |
| --- | --- | --- | --- |
| Architecture overview | `README.md`; root and full agent registries | `astro.config.mjs`, `ansible.cfg`, inventory, brain registry | Recent Git history; `tests/test_cms.py` |
| Agent operation | `AGENTS.md`, `.agents/AGENTS.md` | active context manifest; skill/workflow directory inventory | `tools/eod-palace.sh`; OKF/signature tests |
| Session and Palace | `tools/reanimate.sh`, `tools/eod-palace.sh` | `playbooks/`, brain registry/marker design | Root agent boot caller; Git log as input |
| Ansible baseline | `playbooks/site.yml`, `playbooks/configure.yml` | `ansible.cfg`, inventory, role defaults and task orchestrator | SOD/EOD invokes local scripts; test coverage |
| Tools and privacy | Native ritual wrapper inventory | reanimate, privacy guardian implementations | SOD/EOD playbooks; `.gitignore` |
| MCP and CI | `tools/mcp/server.py`; GitHub workflow files | state-compaction script and workflow env contract | brain resource files, docs search target |
| Documentation delivery | `astro.config.mjs`, GitHub Pages workflow | hooks, Render config, sitemap generator | deployment/sitemap test suites |
| Verification | `package.json` | representative test modules and assertions | platform test observations and existing tests |

## Critic TODO ledger

- Native Python OpenWiki Emulator verified operational without Node.js dependencies.
