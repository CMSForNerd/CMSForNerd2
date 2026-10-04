---
type: "documentation"
title: "Session Memory Stratification & Palace Synchronisation"
description: "Brain artifact ownership, active-context, SOD/reanimation, EOD/hibernation, Palace Sync."
topics: ["openwiki", "memory", "session", "palace", "stratification"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: Session Memory Stratification & Palace Synchronisation
  url: openwiki/memory/session-and-palace.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: "2026-10-04T22:07:16Z"
---
# Session Memory Stratification & Palace Synchronisation

Context decay is the single largest point of failure in Human-AI collaborative engineering. DSOM eliminates this through spatial memory stratification and strict session rituals.

## 🧠 Session State Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Initialised : Start of Day (SOD)
    Initialised --> Active : Reanimation
    Active --> Processing : Working Context Loaded
    Processing --> Reflecting : Palace Sync
    Reflecting --> Hibernated : End of Day (EOD)
    Hibernated --> [*] : Session Closed
```

## 🧠 Spatial Memory & Brain Artifacts

Active state tracking resides within the `.agents/brain/` directory:
- `task.md` — Houses active, pending, and completed tasks.
- `walkthrough.md` — Records session histories and dated Mental Anchors.
- `active_context_manifest.md` — Specifies exact files in active scope.
- `palace_registry.md` — Index of Sovereign Markdown Palace rooms mapping to `docs/` files.
