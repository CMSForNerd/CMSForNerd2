---
type: "documentation"
title: "OpenWiki Quickstart & Repository Navigation Map"
description: "Master entrypoint containing repository map, task-routing table, canonical links, and focused validation commands."
topics: ["openwiki", "quickstart", "navigation", "dsom"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: OpenWiki Quickstart & Repository Navigation Map
  url: openwiki/quickstart.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: '2026-10-04T21:17:34Z'
tags: ["openwiki", "quickstart", "navigation", "dsom"]
---
# OpenWiki Quickstart & Repository Navigation Map

Welcome to the **Sovereign OpenWiki Quickstart**. This document serves as the master entrypoint and topology guide for both humans and AI agents navigating the Deep State of Mind (DSOM) framework.

## 🏛️ Repository Navigation Map

The workspace is organised into three distinct operational planes:

1. **Governance & Persona (The Constitution):**
   - `AGENTS.md` (Root) — High-level sovereign entrypoint.
   - `.agents/AGENTS.md` — Complete constitutional rulebook (27 core rules).
   - `START-HERE.md` — Onboarding map outlining 12 distinct entry points.

2. **Spatial Memory & State (The Palace):**
   - `.agents/brain/` — Real-time persistent state logs (`task.md`, `walkthrough.md`).
   - `.agents/brain/palace_registry.md` — Spatial index of the Sovereign Markdown Palace.
   - `docs/` — Human-readable compiled documentation rooms.

3. **Execution & Automation (The Control Plane):**
   - `tools/` — Idempotent cross-platform Bash and PowerShell operational scripts.
   - `playbooks/` — Ansible configuration and system automation specs.
   - `tests/` — Comprehensive multi-platform regression test suite.

## 📋 Active Task Routing Table

When executing operational workflows, use the following routing table to locate instructions:

| Task Class | Instruction Location | Primary Executor |
| :--- | :--- | :--- |
| **Session Initialisation** | `docs/how-to/openwiki-python-compiler-guide.md` | `tools/reanimate.sh` |
| **Daily State Sync** | `docs/how-to/sitemap-verification.md` | `tools/eod-palace.sh` |
| **Security Scanning** | `docs/governance/AI-AGENT-CHARTER-TEMPLATE.md` | GitHub Actions |
| **Session Hibernation** | `docs/explanation/dsom-agentic-workflow-blueprint.md` | `tools/eod-palace.sh` |

## 🧪 Focused Validation Commands

Validate workspace integrity and compliance at any time using these zero-binary commands:

```bash
# Execute local test suite
uv run --with pyyaml --with pytest --with requests --with fastmcp --with pydantic-settings python -m pytest tests/test_unit.py

# Initialise/Update the OpenWiki Knowledge Graph
uv run --with pyyaml python tools/openwiki_emulator.py --init
```
