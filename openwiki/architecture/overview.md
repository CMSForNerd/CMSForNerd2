---
type: "documentation"
title: "DSOM Scope & Three-Pillar Operational Model"
description: "DSOM scope, three-pillar operating model, component boundaries, and authoritative sources."
topics: ["openwiki", "architecture", "overview", "pillars"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: DSOM Scope & Three-Pillar Operational Model
  url: openwiki/architecture/overview.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: '2026-10-05T16:29:09Z'
tags: ["openwiki", "architecture", "overview", "pillars"]
---
# DSOM Scope & Three-Pillar Operational Model

The **Deep State of Mind (DSOM)** protocol is a metacognitive governance framework designed to establish absolute operational alignment, digital sovereignty, and persistent context continuity between human operators and AI agents.

## 🏛️ The Three-Pillar Operating Model

The architecture of DSOM is structured around three foundational pillars:

```mermaid
flowchart TD
    GOV["Pillar 1: Metacognitive Governance<br/>Constitutional AGENTS.md Laws"] --> MEM["Pillar 2: Spatial Memory<br/>Brain & Palace"]
    GOV --> EXEC["Pillar 3: Absolute Execution<br/>Ansible & Tools"]
    MEM <--> EXEC
```

1. **Pillar 1: Metacognitive Governance (The Mind):**
   - Established by the master constitution under `.agents/AGENTS.md`.
   - Governs AI self-reflection, behaviour guidelines, token budgeting, and the 27 operational rules.

2. **Pillar 2: Spatial Memory (The Palace):**
   - Co-located in `.agents/brain/` and compiled inside the `docs/` Palace.
   - Prevents context decay across ephemeral chat session boundaries.

3. **Pillar 3: Absolute Execution (The Body):**
   - Implemented via declarative automation (Ansible baseline) and idempotent operational wrappers (`tools/`).
