---
type: "documentation"
title: "Dual Agent Registry & Sovereign Operational Laws"
description: "Dual AGENTS.md registry, 27-rule operating constraints, mechanical boot and behaviour/discovery ordering."
topics: ["openwiki", "governance", "agents", "protocols", "rules"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: Dual Agent Registry & Sovereign Operational Laws
  url: openwiki/governance/agent-operation.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: '2026-10-05T16:29:09Z'
tags: ["openwiki", "governance", "agents", "protocols", "rules"]
---
# Dual Agent Registry & Sovereign Operational Laws

To ensure immediate discovery by various platform LLM interfaces, DSOM enforces a dual-layered constitutional registry that anchors the agent's behaviour.

## 📜 The Dual AGENTS.md Registry

1. **The Root Gateway (`AGENTS.md`):**
   - Placed at the workspace root as a discoverable landing page for platform-integrated agents.

2. **The Sovereign Constitution (`.agents/AGENTS.md`):**
   - Located securely within the `.agents/` control directory.
   - Houses the complete 27 operational rules and execution constraints.

## ⚙️ The Mechanical Boot Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Human Operator
    participant Agent as AI Agent
    participant Constitution as .agents/AGENTS.md
    participant Brain as .agents/brain/
    participant Onboarding as START-HERE.md

    User->>Agent: Initialise Session
    Agent->>Constitution: Genesis Read (Establish identity & rules)
    Constitution-->>Agent: Operational laws & constraints loaded
    Agent->>Brain: Memory Restoration (Read task.md & walkthrough.md)
    Brain-->>Agent: Active state restored
    Agent->>Onboarding: Discover Topology (Read START-HERE.md)
    Onboarding-->>Agent: Onboarding map loaded
    Agent-->>User: Ready for Task Execution
```
