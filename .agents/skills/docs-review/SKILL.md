---
spec_version: "0.2"
type: "skill"
skill_id: "docs_review"
name: "docs-review"
title: "Documentation Review Skill"
description: "Facilitates structured reviews of documentation changes to ensure accuracy, style guide compliance, and maintainability."
version: "1.0.0"
author: "AI Workspace Assistant"
tags: ["documentation", "review", "quality-assurance", "okf", "diataxis"]
status: "stable"
sources:
- id: metabase_docs_review
  title: Metabase Documentation Review Skill
  url: https://github.com/metabase/metabase
- id: microsoft_writing_style_guide
  title: Microsoft Writing Style Guide
  url: https://learn.microsoft.com/en-us/style-guide/welcome/
inputs:
  target_file:
    type: string
    description: Path to the documentation file or pull request diff being reviewed.
outputs:
  review_feedback:
    type: string
    description: Numbered, prioritised review findings categorized by severity.
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
topics: ["documentation", "review", "quality-assurance", "okf", "diataxis"]
---

# Documentation Review Skill (`docs-review`)

The `docs-review` skill provides a systematic review protocol for evaluating documentation changes, pull requests, and Markdown files against quality and style standards.

## Operational Review Protocol

1. **Verify Evidence vs Claims**:
   - Confirm that UI labels, CLI flags, API parameters, and configuration paths physically match implementation code.
   - Flag outdated instructions, broken links, or missing edge-case warnings.

2. **Categorise Findings by Severity**:
   - **Critical / Incorrect**: Commands fail, parameters are wrong, or security assumptions are false.
   - **Missing**: Crucial prerequisite steps or output descriptions are omitted.
   - **Confusing / Outdated**: Ambiguous phrasing or references to legacy code/PHP endpoints.
   - **Style / Formatting**: Non-compliance with OKF v0.1/v0.2 metadata or Standard UK English.

3. **Mandatory Feedback Format**:
   - Number issues sequentially starting from `Issue 1`.
   - Provide concrete remedies or suggested Markdown diffs.

## FAQs

### How do I determine which review mode to use?

In local terminal workflows, use local review mode. When GitHub review tools or pull request comments are available, integrate with PR review workflows.

### What should I do with trivial or insignificant formatting issues?

Focus feedback on material issues impacting reader understanding or technical accuracy. Ignore minor stylistic choices if they do not violate project standards.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
