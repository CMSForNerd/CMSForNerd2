---
spec_version: "0.2"
type: "skill"
skill_id: "docx"
name: "docx"
title: "Document Creation, Editing & Conversion Skill"
description: "Handles professional Word document (.docx) creation, redlining, tracked changes, comment extraction, and Pandoc Markdown conversion."
version: "1.0.0"
author: "AI Workspace Assistant"
tags:
- docx
- pandoc
- document-processing
- redlining
- markdown-conversion
status: "stable"
sources:
- id: "anthropics_docx"
  title: Anthropic Skills - Docx
  url: https://github.com/anthropics/skills
inputs:
  input_file:
    type: string
    description: Path to input .docx or source text.
outputs:
  output_document:
    type: string
    description: Generated or processed .docx file or converted Markdown text.
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
topics:
- docx
- pandoc
- document-processing
- redlining
- markdown-conversion
---

# Document Creation, Editing & Conversion Skill (`docx`)

The `docx` skill manages the creation, modification, redlining, and text extraction of professional `.docx` documents and their lossless conversion to Markdown using Pandoc and Node.js libraries.

## Operational Workflows

1. **New Document Generation**:
   - Utilize standard document creation tooling or scripts (`docx-js` / Pandoc) to produce structured, styled Word documents.

2. **Editing & Redlining Workflow**:
   - Preserve tracked changes, comments, and document structure when editing legal, technical, or administrative documents.

3. **Lossless Markdown Extraction (`markitdown` / Pandoc)**:
   - Extract content from `.docx`, PDF, or HTML into Markdown using Pandoc (`pandoc -f docx -t markdown input.docx -o output.md`).
   - Report any structural conversion limitations (e.g., flattened complex nested tables or missing image captions).

## FAQs

### How do I convert a .docx document to Markdown?

Run `pandoc -f docx -t markdown input.docx -o output.md` or use Python's `markitdown` utility to convert document contents into scannable text.

### How are tracked changes handled during edits?

For formal document reviews, maintain tracked changes and comments using redlining protocols to ensure revision auditability.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
