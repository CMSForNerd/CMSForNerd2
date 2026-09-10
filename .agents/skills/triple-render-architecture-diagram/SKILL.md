---
name: "triple-render-architecture-diagram"
type: "skill"
title: "Triple-Render Architecture Diagram Specification Skill (ASCII trees + SVG + Mermaid)"
description: "Generates and enforces production-grade triple-tier visual deliverables combining ASCII trees, raw SVG vector graphics, Git-native Mermaid blocks, and summary routing tables."
status: "active"
stale_after: "2027-09-08T00:00:00Z"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-08T00:00:00Z'
verified: true
sources:
- url: README.md
  description: Master platform index.
topics: ["dsom", "skill", "architecture", "diagrams", "svg", "mermaid", "ASCII trees"]
spec_version: "0.2"
tags: ["dsom", "skill", "architecture", "diagrams", "svg", "mermaid", "ASCII trees"]
---

# Triple-Render Architecture Diagram Specification Skill (ASCII trees + SVG + Mermaid)

This skill enforces the **Triple-Render Architecture Diagram Specification (ASCII trees + SVG + Mermaid)** across all architecture, topology, sequence, or workflow visual deliverables in the codebase and documentation.

---

### SYSTEM DIRECTIVE: TRIPLE-RENDER ARCHITECTURE DIAGRAM SPECIFICATION (SVG + MERMAID)

Translate the architecture, topology, sequence, or workflow established in the conversation or specification into a production-grade, multi-tier visual deliverable.

Generate the output strictly in the following sequence without introductory fluff or conversational filler:

---

#### 1. ASCII Trees Diagram
Generate a clean, structured plain-text ASCII box or tree diagram representing the component hierarchy, execution flow, or system topology using standard box-drawing characters (`┌`, `─`, `┐`, `│`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`, `▶`, `▲`, `▼`, `◄`).

#### 2. Standalone Production-Ready SVG Vector Graphic (`.svg`)
Generate a self-contained, fully compliant raw SVG vector block inside a single ````xml ... ```` code fence matching these styling constraints:
* **Canvas Hygiene:** Explicit `xmlns="http://www.w3.org/2000/svg"`, explicit `viewBox`, `width="100%"`, and `height="100%"`.
* **Palette & Design System (Dark Slate Navy Canvas for Dark Mode):**
  * Canvas Background: Dark Slate Navy (`#0F172A` or `#0B0F19`).
  * Container Cards: Deep Slate Surface (`#1E293B`) with rounded corners (`rx="8"` or `rx="10"`), subtle card strokes (`#334155` or `#475569`), and card header bars (`#334155`).
  * Header Accents & Text: High-contrast off-white/slate text (`#F8FAFC` or `#E2E8F0`).
  * Accent Pill Labels: Distinct deep tones (#60A5FA blue, #4ADE80 green, #FBBF24 amber, #C084FC purple, #38BDF8 sky).
  * Typography: Modern sans-serif typography stack (`font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"`). Monospace font (`Consolas`, `Monaco`, or `'Courier New'`) for IP addresses, CIDRs, file paths, and network ports.
* **Light / Print Mode Adaptive Rules:**
  * Embedded CSS styles in the application dynamically transform the Dark Slate canvas into a crisp `#FFFFFF` white background canvas with `#F8FAFC` card fills, dark `#0F172A` typography, and rich deep accent labels (`#1D4ED8`, `#15803D`, `#B45309`, `#6B21A8`) in Light Mode and Print Mode (`@media print`), ensuring zero toner waste when printing.
* **Structural Precision:**
  * Define explicit arrow markers (`<marker>`) inside `<defs>`.
  * Group logical subnets, tiers, or security boundaries into distinct container rectangles with uppercase section headers.
  * Every card must contain: entity title (bold), primary network/system identifier (IP, FQDN, or ID), and key functional metadata (ports, daemons, or roles).
  * Direct all connection paths (`<path>` or `<line>`) with explicit coordinates and distinct port/protocol callout pill badges.

#### 3. Git-Native Mermaid Diagram (`.mmd` / Mermaid Block)
Directly beneath the SVG block, generate an equivalent, character-exact Mermaid diagram inside a single ````mermaid ... ```` code fence:
* **Orientation:** Choose the most readable layout (`graph TD`, `graph LR`, or `sequenceDiagram`).
* **Grouping:** Enclose security tiers, VLANs, clusters, or operational domains inside explicit `subgraph` blocks.
* **Label Precision:** Display clear port bindings, protocol indicators, and service actions along link connectors (e.g., `-->|"TCP 5432 / mTLS"|` or `-->|"SSH Port 22"|`).
* **Readability:** Break long node labels across multiple lines using HTML break tags (`<br/>`).

#### 4. Summary Interface & Routing Table
Conclude with a clean Markdown comparison table summarizing:
* Source Component
* Target Component
* Port / Protocol / API Ingress
* Security Boundary / Trust Zone / Access Key
* Operational Significance / Flow Description

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-08*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
