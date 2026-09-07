---
type: "documentation"
title: "Web Design Guidelines Skill Overview"
description: "Comprehensive guide to the web-design-guidelines skill, its purpose, guidelines, and execution workflow for human developers and AI agents."
topics: ["skill", "web-design", "accessibility", "ux", "guidelines"]
nav_order: 10
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: web-design-guidelines-skill.md
  url: docs/explanation/web-design-guidelines-skill.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["skill", "web-design", "accessibility", "ux", "guidelines"]
---

# Web Design Guidelines Skill Guide

The `web-design-guidelines` skill is designed to assist developers, designers, and autonomous AI agents (such as Google Jules and Google Antigravity) in reviewing web interfaces to ensure they strictly comply with established UI design guidelines, accessibility standards, and UX principles.

## Purpose and Problem Statement

The 'web-design-guidelines' skill solves the problem of checking websites and web applications for adherence to best practices, accessibility standards, and UX principles. It automates the review process, providing developers and designers with a quick and reliable way to evaluate their work against predefined guidelines, helping them improve the overall user experience and accessibility of their sites. By using this skill, users can streamline their design audits and ensure their web interfaces meet industry standards.

---

## Core Guidelines & Rule Categories

### 1. Accessibility (a11y)

- **Icon-only buttons**: Must carry an explicit `aria-label` attribute.
- **Form controls**: Must be associated with an explicit `<label>` or carry an `aria-label`.
- **Keyboard navigation**: Interactive elements must support standard keyboard event handlers (`onKeyDown`/`onKeyUp`).
- **Semantic HTML**: Prefer `<button>` for actions and `<a>` for navigation over `<div>` or `<span>` click listeners.
- **Image alt text**: Every `<img>` element must have an `alt` attribute (or `alt=""` if purely decorative).
- **Decorative icons**: Mark decorative icons with `aria-hidden="true"`.
- **Async updates**: Dynamic status messages or toasts must use `aria-live="polite"`.
- **Heading hierarchy**: Enforce hierarchical `<h1>` through `<h6>` tags.

### 2. Focus States

- Interactive elements must provide visible focus indicators (e.g. `:focus-visible` or focus rings).
- Never use `outline: none` or `outline-none` without providing a visible focus replacement.

### 3. Forms & Inputs

- Text inputs must specify explicit `autocomplete` and meaningful `name` attributes.
- Use appropriate `type` attributes (`email`, `tel`, `url`, `number`) and `inputmode`.
- Labels must be clickable by sharing an explicit hit target with the form control.
- Placeholders must end with a single unicode ellipsis `…` and display an example pattern.
- Non-authentication fields should explicitly use `autocomplete="off"` to prevent unintended browser auto-fill triggers.

### 4. Typography & Copy

- Use unicode ellipsis `…` (`\u2026`) instead of three full stops `...`.
- Use curly quotes (`“` `”`) instead of straight double quotes (`"`).
- Ensure non-breaking spaces before units (`10&nbsp;MB`, `⌘&nbsp;K`).
- Use heading balancing via `text-wrap: balance` or `text-pretty`.

### 5. Images & Layout Performance

- Every `<img>` tag must specify explicit `width` and `height` dimensions to eliminate Cumulative Layout Shift (CLS).
- Below-the-fold assets must specify `loading="lazy"`.
- Above-the-fold critical assets must specify `fetchpriority="high"`.

---

## Agent and Human Execution Workflow

1. **Audit Phase**: The agent or developer inspects specified source files (`.astro`, `.html`, `.js`, `.css`, `.md`) against the rules.
2. **Finding Output**: Issues are reported concisely using standard `file:line - description` formatting for rapid navigation.
3. **Remediation Phase**: Source code is modified directly in accordance with the guidelines.
4. **Verification**: Automated tests (e.g. Pytest and Playwright E2E suites) confirm visual rendering and functional compliance.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
