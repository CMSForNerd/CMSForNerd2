---
okf_version: 0.1
type: "skill"
title: "Context7 Integration Skill"
name: "context7-integration"
description: "Maintains automated documentation indexing and updates utilizing Context7 services across CI workflows."
timestamp: "2026-08-01T12:00:00Z"
topics: ["context7", "documentation", "index", "gitlab-ci", "github-actions"]
---

# Context7 Integration Skill

This skill governs the integration, setup, and execution of Context7 services used to keep documentation indices synchronised across the project repository and CI/CD pipelines.

## When to use this skill

- When updating the Context7 service configurations in `context7.json`.
- When modifying CI/CD workflows that execute automated documentation refreshes.
- When configuring environment variables and secrets for external integration.

## Operational Standards & Procedures

### 1. Root Configuration Registry
Maintain the configuration parameters of Context7 services in a standardized location:
- The repository integrates Context7 services using the `context7.json` file located at the repository root.

### 2. CI/CD Workflow Automation
By utilising automated pipelines, ensure documentation updates are processed after changes:
- Automated documentation refreshes are configured via both GitLab CI (`.gitlab-ci.yml`) and GitHub Actions (`.github/workflows/context7-refresh.yml`).
- These pipelines require the `CONTEXT7_API_KEY` environment variable/secret to be successfully configured and executed.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
