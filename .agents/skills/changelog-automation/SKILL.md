---
spec_version: "0.2"
type: "skill"
skill_id: "changelog_automation"
name: "changelog-automation"
title: "Changelog Automation & Release Notes Skill"
description: "Automates changelog generation from commits, PRs, and releases following Keep a Changelog and Conventional Commits."
version: "1.0.0"
author: "AI Workspace Assistant"
tags:
- changelog
- release-notes
- conventional-commits
- keep-a-changelog
- automation
status: "stable"
sources:
- id: "wshobson_changelog"
  title: Changelog Automation Skill
  url: https://github.com/wshobson/agents
- id: "keep_a_changelog"
  title: Keep a Changelog 1.1.0 Specification
  url: https://keepachangelog.com/en/1.1.0/
inputs:
  commit_range:
    type: string
    description: Git commit range or release tag.
outputs:
  changelog_markdown:
    type: string
    description: Structured release notes categorized by user and technical impact.
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
topics:
- changelog
- release-notes
- conventional-commits
- keep-a-changelog
- automation
---

# Changelog Automation & Release Notes Skill (`changelog-automation`)

The `changelog-automation` skill structures change histories, release notes, and product updates following the **Keep a Changelog** standard and **Conventional Commits** specification.

## Core Directives

1. **Audience-Centric Grouping**:
   - Do not dump raw commit messages. Group changes into clear categories:
     - `Added` for new features.
     - `Changed` for changes in existing functionality.
     - `Deprecated` for soon-to-be removed features.
     - `Removed` for now removed features.
     - `Fixed` for any bug fixes.
     - `Security` in case of vulnerabilities.

2. **Explain User & Technical Impact**:
   - Highlight breaking changes, migration steps for developers, and behavior modifications for users.

3. **Conventional Commits Enforcement**:
   - Map standard prefixes (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`) to changelog categories.

## FAQs

### What tools integrate with this skill?

Standard release tools like `@commitlint`, `standard-version`, `semantic-release`, and GitHub/GitLab release workflows.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
