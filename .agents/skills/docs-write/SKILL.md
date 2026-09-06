---
spec_version: "0.2"
type: "skill"
skill_id: "docs_write"
name: "docs-write"
title: "Documentation Writing Skill"
description: "Assists users in creating and editing documentation adhering to clear, conversational, and user-focused writing standards."
version: "1.0.0"
timestamp: "2026-09-06T00:00:00Z"
author: "AI Workspace Assistant"
tags: ["documentation", "writing", "markdown", "diataxis", "user-focused"]
status: "stable"
sources:
  - id: "metabase_docs_write"
    title: "Metabase Documentation Writing Guide"
    url: "https://github.com/metabase/metabase"
  - id: "google_developer_docs_style_guide"
    title: "Google Developer Documentation Style Guide"
    url: "https://developers.google.com/style"
inputs:
  reader_intent:
    type: "string"
    description: "The targeted audience and what they are attempting to accomplish."
  format:
    type: "string"
    description: "Document format (Markdown, MDX, HTML)."
    default: "Markdown"
outputs:
  documentation:
    type: "string"
    description: "Clear, user-focused documentation written in Standard UK English."

okf_version: "0.1"
---

# Documentation Writing Skill (`docs-write`)

The `docs-write` skill assists users and agents in creating, updating, and structuring high-quality documentation adhering to clear, conversational, and reader-focused principles.

## Operational Standards & Best Practices

1. **Identify Reader Intent First**:
   - Determine who the reader is (new user, developer, administrator) and their specific objective.
   - Align content with the **Diátaxis framework** (Tutorials, How-To Guides, Reference, or Explanation).

2. **Style & Tone Guidelines**:
   - Use **Standard UK English** spelling (e.g., *optimise*, *synchronise*, *prioritise*).
   - Use active voice, precise nouns, concrete examples, and scannable headings.
   - Avoid overly formal jargon, vague headings (e.g., "Overview"), or non-functional code blocks.

3. **Writing Process**:
   - **Drafting**: Focus on audience needs, concrete code/command examples, and realistic scenarios.
   - **Editing**: Remove passive constructions, trim fluff, and verify that instructions can be executed sequentially.
   - **Polishing**: Ensure frontmatter carries valid OKF compliance metadata.

## FAQs

### How do I start using the `docs-write` skill?
Begin by defining the reader's intent and target Diátaxis quadrant, then draft content using active voice and Standard UK English conventions.

### What document formats are supported?
This skill is tailored for Markdown (`.md`), MDX (`.mdx`), and Open Knowledge Format (OKF) files.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
