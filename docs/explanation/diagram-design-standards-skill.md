---
type: "documentation"
title: "Diagram Design Standards Skill Overview"
description: "Comprehensive guide to the diagram-design-standards skill, detailing the unified specification for standalone SVG vector graphics, Git-native Mermaid blocks, and summary routing tables."
topics: ["diagrams", "svg", "mermaid", "architecture", "design-system", "explanation"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: skill_definition
  title: Diagram Design Standards Skill Definition
  url: .agents/skills/diagram-design-standards/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["diagrams", "svg", "mermaid", "architecture", "design-system", "explanation"]
---

# Diagram Design Standards Skill Overview

The `diagram-design-standards` skill provides autonomous AI agents (such as Google Jules and Google Antigravity) and human software engineers with a unified, repeatable specification for producing production-ready, highly legible technical diagrams across the CMSForNerd2 ecosystem.

## Overview & Rationale

Visual architecture and network topology diagrams in modern software systems frequently suffer from visual inconsistency, platform lock-in, and lack of metadata clarity. Traditional image formats (such as PNG or JPEG) cannot be diffed in Git or indexed by AI search agents, whereas raw Mermaid diagrams alone may lack fine-grained aesthetic control required for executive handbooks and print publications.

The `diagram-design-standards` skill addresses these challenges by mandating a tri-part output format for every diagram generation task:

1. **Standalone SVG Vector Graphic (`.svg`):** Provides pixel-perfect visual styling, crisp vector resolution, custom card containers, color-coded security tiers, and precise connection pill badges.
2. **Git-Native Mermaid Block (`.mmd`):** Guarantees native, interactive rendering in GitHub web views, Markdown viewers, and web applications with version-controlled plain-text readability.
3. **Summary Interface & Routing Table:** Offers structured, machine-readable operational tabular metadata detailing ports, protocols, security boundaries, and traffic flow mechanics.

---

## Detailed Formatting & Design Specifications

### 1. SVG Design System & Palette Constraints

All standalone SVG vector blocks generated under this skill must adhere to the following design system:

* **Canvas Hygiene:** Explicit `xmlns="http://www.w3.org/2000/svg"`, explicit `viewBox` matching element coordinates, and relative `width="100%"` / `height="100%"`.
* **Color Palette:**
  * Canvas Background: `#F8FAFC` (slate-50) or `#FFFFFF` (pure white).
  * Container Cards: Background `#FFFFFF` with rounded corners (`rx="8"` or `rx="10"`) and subtle strokes (`#CBD5E1` or `#94A3B8`).
  * Header Accents: Soft pastel fills (`#EFF6FF` blue, `#DCFCE7` green, `#F1F5F9` slate).
  * Text Colors: High-contrast slate text (`#0F172A` / `#334155`).
* **Typography Stack:** Modern sans-serif stack (`font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"`) for titles and labels; Monospace (`Consolas`, `Monaco`, `'Courier New'`) for network ports, IP addresses, paths, and protocols.
* **Markers & Connecting Lines:** Arrows defined inside `<defs>` with explicit `<marker>` tags. Lines styled with distinct callout pill badges indicating network protocols (e.g., `HTTPS/443`, `mTLS/5432`, `SSH/22`).

### 2. Git-Native Mermaid Specifications

Directly following the SVG code fence, an equivalent Mermaid diagram is placed inside a ````mermaid ... ```` code fence:

* **Subgraphs:** Group subnets, VLANs, trust zones, or operational clusters inside explicit `subgraph` blocks.
* **Connector Precision:** Annotate every edge connector with protocol details (e.g., `-->|"TCP 4321 / HTTP"|`).
* **Multi-Line Labels:** Use `<br/>` HTML tags to break long component descriptions into clean multi-line blocks.

### 3. Summary Interface & Routing Table Specifications

Conclude each diagram output with a clean Markdown comparison table formatted as follows:

| Source Component | Target Component | Port / Protocol / API Ingress | Security Boundary / Trust Zone / Access Key | Operational Significance / Flow Description |
| :--- | :--- | :--- | :--- | :--- |
| *Client Browser / Agent* | *Nginx Reverse Proxy* | `443 / HTTPS (TLS 1.3)` | *DMZ / Public Ingress / TLS Cert* | *Handles incoming SSL termination and routes static web requests.* |

---

## AI Agent & Developer Execution Workflow

When invoked during documentation writing, architecture decision record (ADR) drafting, or technical handbook creation:

1. Identify the architectural entities, network ingress paths, and trust boundaries.
2. Construct the standalone SVG vector block inside an ````xml ... ```` fence.
3. Construct the character-exact Mermaid block inside a ````mermaid ... ```` fence.
4. Construct the summary routing comparison table in standard Markdown format.
5. Audit the generated output to ensure zero missing text nodes, valid SVG syntax, and complete table mapping.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
