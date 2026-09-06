---
okf_version: "0.1"
type: "skill"
title: "Project Technical Book & Handbook Compiler"
timestamp: "2026-09-05T00:00:00Z"
description: "Autonomously synthesizes repository code, Diataxis documentation, and system telemetry into publication-grade print-ready PDF, standalone HTML, and EPUB handbooks using Pandoc, Headless Chromium, and the Terminal & Cloud design framework."
topics: ["pandoc", "pdf", "html", "epub", "print-optimized", "diataxis", "handbook"]
status: "stable"
stale_after: "2027-09-05"
sources:
  - id: "dsom_agents_rulebook"
    title: "The Core AI Rulebook (DSOM Rule 11 & Rule 22)"
    path: ".agents/AGENTS.md"
name: "project-technical-book-compiler"
---

# Project Technical Book & Handbook Compiler

## Purpose
Standardizes the automated assembly, styling, and multi-format compilation of entire project repositories into unified, publication-grade engineering handbooks.

## Execution Workflow
1. **Build Master Markdown**: `python3 tools/build_project_book.py`
2. **Compile Standalone Interactive HTML**: `pandoc build/book/master_book.md -o build/book/handbook.html --standalone --toc --toc-depth=3 --number-sections --include-before-body=build/book/cover.html --css=terminal-theme.css --highlight-style=tango --metadata title="Project Technical Handbook"`
3. **Bake Native Vector SVGs & Inline CSS**: `python3 tools/bake_native_svg.py`
4. **Compile Publication-Grade PDF**: `chromium-browser --headless=new --disable-gpu --run-all-compositor-stages-before-draw --virtual-time-budget=8000 --print-to-pdf=build/book/handbook.pdf file:///path/to/build/book/handbook.html`
5. **Compile EPUB 3 Ebook**: `pandoc build/book/master_book.md -o build/book/handbook.epub -t epub3 --toc --toc-depth=3 --css=build/book/terminal-theme.css`

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
