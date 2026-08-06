---
okf_version: 0.1
type: "skill"
title: "Build and Preview Workflow Skill"
name: "build-preview-workflow"
description: "Guides local compilation, testing, and preview workflows for Astro 7.1 static site generator."
timestamp: "2026-08-01T12:00:00Z"
topics: ["build", "preview", "astro", "static", "workflow"]
---

# Build and Preview Workflow Skill

This skill governs the compilation of CMSForNerd2's static assets, local port configuration, and live preview procedures.

## When to use this skill

- When building the static application locally or in a remote sandbox.
- When starting local preview servers to verify routing, layout, and styling.
- When configuring port and server parameters for local testing.

## Operational Standards & Procedures

### 1. Project Static Compilation
CMSForNerd2 is a static modernisation of the legacy database-free PHP CMS:
- Utilise the Astro Static Site Generator (SSG) to produce purely statically served assets (HTML5, CSS3, ES6+ JS).
- Compile the project to static assets in the `dist/` directory using the command: `npm run build`.

### 2. Local Previewing
To run and verify the compiled static assets locally:
- Preview the statically built application locally on port 4321 using the command: `npm run preview`.
- Active, non-historical references to PHP in style comments, routing code, and offline fallback messages are updated or removed to align fully with Astro 7.1.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
