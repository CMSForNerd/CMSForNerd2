---
okf_version: 0.1
type: "documentation"
title: "Spatial Memory & Dual-Pathway Design"
description: "Conceptual overview explaining Deep State of Mind spatial memory boundaries, Google Jules sandbox environment limits, and dual-pathway Ansible orchestration."
timestamp: "2026-08-01T15:00:00Z"
topics: ["explanation", "dsom", "sandbox", "jules", "ansible"]

nav_order: 1
---

# 🧠 Spatial Memory & Dual-Pathway Design

This document describes the architectural theory and conceptual principles governing **Sovereign AI Agent Memory**, **Google Jules Sandbox Limitations**, and **Dual-Pathway Automation** within the CMSForNerd2 project.

---

## 🏛️ Deep State of Mind (DSOM) Spatial Memory

Unlike traditional software development where operational rules and context exist only in the human mind, the CMSForNerd2 project uses the **Deep State of Mind (DSOM)** cognitive protocol.

Under DSOM, AI agents (like Google Jules) and human developers share a synchronized, Git-native memory model:
1.  **Rulebook Synchronization**: Core rules are fully synchronized between `AGENTS.md` and `.agents/AGENTS.md`. These rulebooks act as the "constitution" of the repository, setting coding standards, language rules, and verification pathways.
2.  **Zero-Global Operational Memory**: Active context, tasks, and historical mental anchors are recorded in Markdown format inside `.agents/brain/` (`task.md`, `walkthrough.md`, `knowledge.md`).
3.  **Self-Contained Discovery**: By establishing spatial memories within the repository, agents can instantly restore context on subsequent runs without relying on external, stateful API databases.

---

## 🔒 Google Jules Sandbox Constraints

When executing inside the Google Jules workspace, automation tasks run under specialized unprivileged virtual machine constraints:
- **No Persistent OS Modifications**: Though passwordless `sudo` is configured, there is no persistent init/systemd system. Changes made outside the workspace directory are discarded when the container finishes running.
- **Headless Execution**: No physical or virtual display server exists, meaning visual validation (like Playwright browser tests) must run in strict headless mode.
- **Transient VM Lifecycle**: The sandbox environment is transient.

---

## 🚀 Dual-Pathway Automation Principle

To prevent build failures and environment blocks under restricted sandboxes, all shell scripts, deployment tools, and Ansible orchestration playbooks follow the **Dual-Pathway Automation Principle**.

Instead of assuming full OS privileges, the automation engine performs dynamic detection:

```
                  [AUTOMATION TRIGGER]
                           │
             Check if $USER is "jules" or JULES_ENV?
              /                         \
            YES                         NO
            /                             \
     [Pathway A: Sandbox]         [Pathway B: Production]
     - Run in local workspace     - Trigger full playbook execution
     - npm install & build        - Update system Nginx servers
     - Skip system modifications  - Run full security hardening
```

### Pathway A: Sandbox-Safe Unprivileged Builds
If the execution user is detected as `jules` (or `JULES_ENV` is present), the tool skips system-level alterations (such as modifying firewalls, copying system files, or running administrative package managers). It runs local workspace builds inside the unprivileged directory using standard user commands.

### Pathway B: Production System Orchestration
When executing on a persistent staging or production server, the engine launches the full Ansible playbook (`deploy-static.yml`), allowing administrative system configurations, secure Nginx reverse proxy routing, and cryptographic whitelisting.

By separating unprivileged compilation from server provisioning, we guarantee that the build pipeline remains portable, robust, and safe across different running environments.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
