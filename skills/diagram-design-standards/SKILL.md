---
type: "skill"
title: "Diagram Design Standards Skill"
name: "diagram-design-standards"
description: "Standardised specification and guidelines for generating production-ready multi-tier technical diagrams comprising ASCII trees, standalone Dark Slate SVG vector graphics, Git-native Mermaid blocks, and summary routing tables."
topics: ["diagrams", "svg", "mermaid", "architecture", "design-system", "visualization", "ASCII trees"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.1.0"
spec_version: "0.2"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: SKILL.md
  url: skills/diagram-design-standards/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-08T00:00:00Z'
tags: ["diagrams", "svg", "mermaid", "architecture", "design-system", "visualization", "ASCII trees"]
---

# Diagram Design Standards Skill (`diagram-design-standards`)

The `diagram-design-standards` skill governs the creation of production-grade, highly readable technical diagrams across all documentation, architecture decision records, and operational runbooks in the codebase.

When tasked with generating a diagram for architecture, network topology, sequence flows, or component interactions, autonomous AI agents and human contributors must strictly produce a unified four-part deliverable artifact in sequence.

---

## Required Diagram Artifact Output Structure

Every diagram generation request must output all four of the following components in order:

### 1. Plain-Text ASCII Tree Diagram
Generate a clean, structured plain-text ASCII box or tree diagram representing the component hierarchy, execution flow, or system topology using standard box-drawing characters (`┌`, `─`, `┐`, `│`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`, `▶`, `▲`, `▼`, `◄`).

### 2. Standalone Production-Ready SVG Vector Graphic (`.svg`)

Generate a self-contained, fully compliant raw SVG vector block inside a single ````xml ... ```` code fence matching these styling constraints:

* **Canvas Hygiene:**
  * Explicit `xmlns="http://www.w3.org/2000/svg"`.
  * Explicit `viewBox` (e.g. `viewBox="0 0 800 500"`).
  * `width="100%"` and `height="100%"`.
* **Palette & Design System (Dark Slate Navy Canvas for Dark Mode):**
  * **Background:** Dark Slate Navy canvas (`#0F172A` or `#0B0F19`).
  * **Container Cards:** Deep Slate Surface (`#1E293B`) with rounded corners (`rx="8"` or `rx="10"`), subtle card strokes (`#334155` or `#475569`), and card header bars (`#334155`).
  * **Typography:** High-contrast off-white/slate text (`#F8FAFC` or `#E2E8F0`) with modern sans-serif stack (`font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"`). Monospace font (`Consolas`, `Monaco`, or `'Courier New'`) for IP addresses, CIDRs, file paths, and network ports.
* **Light & Print Mode Adaptive Rules:**
  * Embedded CSS rules dynamically adapt Dark Slate SVGs in Light Mode and Print Mode (`@media print`): outer canvas changes to white (`#FFFFFF`) with subtle border (`#E2E8F0`), container cards adapt to `#F8FAFC` with `#CBD5E1` border, text converts to dark `#0F172A`, and title labels adapt to deep print-suitable tones (`#1D4ED8`, `#15803D`, `#B45309`, `#6B21A8`), saving color and toner when printing.
* **Structural Precision:**
  * Define explicit arrow markers (`<marker>`) inside `<defs>`.
  * Group logical subnets, tiers, or security boundaries into distinct container rectangles with uppercase section headers.
  * Every card must contain: entity title (bold), primary network/system identifier (IP, FQDN, or ID), and key functional metadata (ports, daemons, or roles).
  * Direct all connection paths (`<path>` or `<line>`) with explicit coordinates and distinct port/protocol callout pill badges.

### 3. Git-Native Mermaid Diagram (`.mmd` / Mermaid Block)

Directly beneath the SVG block, generate an equivalent, character-exact Mermaid diagram inside a single ````mermaid ... ```` code fence:

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
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-08*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
