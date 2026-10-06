---
type: "documentation"
title: "Sovereign Automation Tools & Privacy Guardian Boundaries"
description: "Native Bash/PowerShell ritual tools, Privacy Guardian, onboarding/reset boundaries."
topics: ["openwiki", "automation", "tools", "privacy", "guardian"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: Sovereign Automation Tools & Privacy Guardian Boundaries
  url: openwiki/automation/tools-and-privacy.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: '2026-10-05T16:29:09Z'
tags: ["openwiki", "automation", "tools", "privacy", "guardian"]
---
# Sovereign Automation Tools & Privacy Guardian Boundaries

Idempotent local script wrappers located in `tools/` handle multi-platform environment management while enforcing strict privacy filters.

## 🛡️ Privacy Guardian Boundaries

The **Privacy Guardian (`tools/eod-palace.sh`)** acts as an inline data-leak prevention layer. Before staging any documentation or logs, it scans for exposed credentials, private keys, or sensitive IPs.
