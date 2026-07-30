---
okf_version: 0.1
type: documentation
title: "The Agent Registry & DSOM Gateway (CMSForNerd2)"
description: "Sovereign entry point instructing AI Agents to look up rules and memory under .agents/."
timestamp: "2026-07-30T12:00:00Z"
topics: [agents, dsom, gateway, constitution]
---

# AI Agent Registry & Sovereign Gateway

This file describes the agents and tools in our codebase, outlining their operational roles, interaction protocols, and input/output conventions. AI agents (such as Google Jules) use this file to understand the codebase and formulate contextually aligned execution plans.

> **Entry Point:** This is the root-level gateway file. The **full cognitive rulebook** and all spatial memory reside in `.agents/AGENTS.md` and `.agents/brain/`. You MUST navigate there immediately to establish alignment.

---

## Critical Instructions for AI Agents

1.  **Read the Full Rulebook**: Navigate immediately to [`.agents/AGENTS.md`](.agents/AGENTS.md) to parse the operational persona, writing styles, and detailed rules governing this project.
2.  **Access Spatial Memory**: Read all brain files located in `.agents/brain/` to restore operational context:
    *   `task.md` — Active and completed task list (present state).
    *   `walkthrough.md` — Session history and Mental Anchors (past state).
3.  **Execute the 5-Step Knowledge-First Discovery Flow**: Before executing terminal commands or external API queries:
    *   Search OKF frontmatter (`topics:` / `description:`) in `.agents/brain/` and `docs/`.
    *   Target specific line ranges via read tools.
    *   Verify the OKF `timestamp` for contextual relevance.
    *   Obtain human consensus if local knowledge is stale.
    *   Execute physical terminal commands only when necessary.
4.  **Synchronise Both Registries**: Keep this root gateway and `.agents/AGENTS.md` fully in sync to maintain architectural consistency.

---

## Deep State of Mind (DSOM) Core Principles

The DSOM framework operates on digital sovereignty, structured metacognition, and Git-native operational management:

| Principle | Description |
| :--- | :--- |
| **Zero-Global / Spatial Memory** | No global mutable state. Operational memory lives in `.agents/brain/`. |
| **Open Knowledge Format (OKF)** | All `.md` documents use OKF v0.1 YAML frontmatter with explicit timestamps. |
| **Atomic Git Commits** | Every logical action is committed granularly; blanket monolithic commits are strictly forbidden. |
| **Omni-Documentation Sync** | New documents must be mapped to `SUMMARY.md`, `START-HERE.md`, and `llms.txt`. |
| **UK English Dominance** | All files, logs, and messages use standard UK English (`-ise`, `-our`, `-re`). |

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
