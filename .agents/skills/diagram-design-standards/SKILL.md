---
type: "skill"
title: "Diagram Design Standards Skill"
name: "diagram-design-standards"
description: "Standardised specification and guidelines for generating production-ready multi-tier technical diagrams incorporating Cathryn Lavery diagram design principles (grid alignment, typography hierarchy, visual flow, high-contrast light/printer-friendly mode) comprising ASCII trees, standalone light/printer-friendly adaptive SVG vector graphics, Git-native Mermaid blocks, and summary routing tables."
topics: ["diagrams", "svg", "mermaid", "architecture", "design-system", "visualization", "cathryn-lavery", "print-optimized"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.2.0"
spec_version: "0.2"
stale_after: "2027-09-17"
sources:
- id: cathryn_lavery_diagram_design
  title: Cathryn Lavery Diagram Design Guidelines
  url: https://github.com/cathrynlavery/diagram-design
- id: workspace_file
  title: SKILL.md
  url: .agents/skills/diagram-design-standards/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["diagrams", "svg", "mermaid", "architecture", "design-system", "visualization", "cathryn-lavery", "print-optimized"]
---

# Diagram Design Standards Skill (`diagram-design-standards`)

The `diagram-design-standards` skill governs the creation of publication-grade, highly legible technical diagrams across all documentation, architecture decision records, and operational runbooks in the codebase. It incorporates the **Cathryn Lavery Diagram Design Principles** (grid discipline, deliberate visual hierarchy, typographic rhythm, intentional whitespace, high-contrast light/printer-friendly mode) to ensure diagrams are elegant on high-DPI screens and zero-toner-waste printer friendly.

When tasked with generating a diagram for architecture, network topology, sequence flows, or component interactions, autonomous AI agents and human contributors must strictly produce a unified four-part deliverable artifact in sequence.

---

## Cathryn Lavery Diagram Design Core Principles

1. **Grid Discipline & Alignment System:**
   - All components, card containers, connector lines, and text blocks must strictly align to an underlying 8px / 16px grid system (`x`, `y`, `width`, `height` in explicit grid steps).
   - Maintain uniform spacing between parallel connector paths and adjacent container blocks (minimum 24px gap).

2. **Typographic Hierarchy & Legibility:**
   - **Primary Titles / Section Headers:** 14pt bold, high-contrast slate (`#0F172A` in light/print mode, `#F8FAFC` in dark mode).
   - **Entity Titles:** 11pt semibold, Linux Blue (`#1E3A8A`) or Deep Slate (`#1E293B`).
   - **Identifiers / Code / IP / Ports:** 9pt monospace (`JetBrains Mono`, `Consolas`, or `Fira Code`) using crisp, high-contrast tones (`#0284C7` or `#0F172A`).
   - **Connector Labels / Pill Badges:** 8.5pt semibold with high contrast.

3. **High-Contrast Light & Printer-Friendly Pure White Mode (Zero Ink Waste):**
   - Solid dark or black canvas backgrounds are strictly forbidden for print or light-mode exports.
   - Base canvas: Pure White (`#FFFFFF`).
   - Card background: Alabaster / Light Gray (`#F8FAFC` or `#F1F5F9`) with slate hairline borders (`1px solid #CBD5E1`).
   - Dark Slate Navy (`#0F172A`) is permitted as a dark-mode fallback, but MUST incorporate adaptive `@media print` and light-mode CSS overrides (`@media (prefers-color-scheme: light)`) to dynamically invert to white background `#FFFFFF` and light container cards `#F8FAFC` with dark text `#0F172A`.

4. **Visual Rhythm & Intentional Whitespace:**
   - Avoid cluttered overlapping connectors or dense text packing.
   - Use distinct pill badges (`<rect rx="10">`) for protocol/port indicators on connection lines.
   - Structure complex system flows into balanced orthogonal grids or 2-column tiers to prevent tall vertical towers that break physical pages.

---

## Required Diagram Artifact Output Structure

Every diagram generation request must output all four of the following components in order:

### 1. Plain-Text ASCII Tree Diagram

Generate a clean, structured plain-text ASCII box or tree diagram representing the component hierarchy, execution flow, or system topology using standard box-drawing characters (`┌`, `─`, `┐`, `│`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`, `▶`, `▲`, `▼`, `◄`).

### 2. Standalone Production-Ready SVG Vector Graphic (`.svg`)

Generate a self-contained, fully compliant raw SVG vector block inside a single ````xml ...```` code fence matching these styling constraints:

* **Canvas Hygiene:**
  * Explicit `xmlns="http://www.w3.org/2000/svg"`.
  * Explicit `viewBox` (e.g. `viewBox="0 0 800 500"`).
  * `width="100%"` and `height="100%"`.
* **Light & Print Mode Primary Palette (Cathryn Lavery Light/Printer-Friendly Standard):**
  * **Canvas Background:** Pure White (`#FFFFFF`).
  * **Container Cards:** Light Alabaster (`#F8FAFC` or `#F1F5F9`) with subtle slate stroke (`#CBD5E1`), rounded corners (`rx="8"`), and clear header bar (`#E2E8F0`).
  * **Text & Glyph Hierarchy:** Dark Charcoal (`#0F172A`) for primary prose, Linux Blue (`#1E3A8A`) for titles, Deep Teal (`#0D9488`) for ports/IPs.
  * **Adaptive Dark Mode Support:** Includes `@media (prefers-color-scheme: dark)` overrides for `#0F172A` background when viewed in dark interfaces, while guaranteeing `@media print` forces pure `#FFFFFF` white background and zero toner waste.
* **Structural Precision:**
  * Define explicit arrow markers (`<marker>`) inside `<defs>`.
  * Group logical subnets, tiers, or security boundaries into distinct container rectangles with uppercase section headers.
  * Every card must contain: entity title (bold), primary network/system identifier (IP, FQDN, or ID), and key functional metadata (ports, daemons, or roles).
  * Direct all connection paths (`<path>` or `<line>`) with explicit coordinates and distinct port/protocol callout pill badges.

### 3. Git-Native Mermaid Diagram (`.mmd` / Mermaid Block)

Directly beneath the SVG block, generate an equivalent, character-exact Mermaid diagram inside a single ````mermaid ...```` code fence:

* **Orientation:** Choose the most readable layout (`graph TD`, `graph LR`, or `sequenceDiagram`).
* **Grouping:** Enclose security tiers, VLANs, clusters, or operational domains inside explicit `subgraph` blocks.
* **Label Precision:** Display clear port bindings, protocol indicators, and service actions along link connectors (e.g., `-->|"TCP 5432 / mTLS"|` or `-->|"SSH Port 22"|`).
* **Readability:** Break long node labels across multiple lines using HTML break tags (`<br/>`).

### 4. Summary Interface & Routing Table

Conclude with a clean Markdown comparison table summarizing:

| Source Component | Target Component | Port / Protocol / API Ingress | Security Boundary / Trust Zone / Access Key | Operational Significance / Flow Description |
| :--- | :--- | :--- | :--- | :--- |

---

## Operational Guidelines & Best Practices

1. **Self-Contained Rendering:** The raw SVG must render cleanly in standard web browsers, GitHub web views, and Pandoc PDF compilers without requiring external stylesheet dependencies or missing fonts.
2. **Accessible Contrast:** Ensure text colors maintain minimum 4.5:1 contrast against card and canvas backgrounds in both dark and light/print modes.
3. **Symmetry & Alignment:** Calculate SVG coordinates (`x`, `y`, `width`, `height`) methodically to align cards, arrows, and pill badges symmetrically.
4. **Mermaid Namespace Safety:** When creating Mermaid subgraphs or multi-diagram suites, prefix node identifiers to prevent ID collisions in single-page HTML previews.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
