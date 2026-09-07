---
type: "skill"
title: "Web Design Guidelines Skill"
name: "web-design-guidelines"
description: "Review UI code for Web Interface Guidelines compliance including accessibility, typography, form attributes, and performance."
topics: ["web-design", "ui", "ux", "accessibility", "guidelines"]
status: "stable"
author: "vercel"
version: "1.0.0"
spec_version: "0.2"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: SKILL.md
  url: .agents/skills/web-design-guidelines/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T00:00:00Z'
tags: ["web-design", "ui", "ux", "accessibility", "guidelines"]
---

# Web Design Guidelines Skill

The `web-design-guidelines` skill is designed to assist in reviewing web interfaces to ensure they comply with established UI design guidelines, accessibility standards, and UX principles.

## Overview

This skill automates the review process, providing developers and designers with a quick and reliable way to evaluate their work against predefined guidelines, helping them improve the overall user experience and accessibility of their sites.

## How It Works

1. Read specified files or UI code components.
2. Check against all rules in the Web Interface Guidelines.
3. Output findings in a concise `file:line` format.

## Guidelines & Rules

### Accessibility

- Icon-only buttons need `aria-label`.
- Form controls need `<label>` or `aria-label`.
- Interactive elements need keyboard handlers (`onKeyDown`/`onKeyUp`).
- Use `<button>` for actions, `<a>` for navigation.
- Images need `alt` attributes (or `alt=""` if decorative).
- Decorative icons need `aria-hidden="true"`.
- Async updates (toasts, validation) need `aria-live="polite"`.
- Use semantic HTML (`<button>`, `<a>`, `<label>`, `<table>`) before ARIA.
- Headings must be hierarchical (`<h1>`–`<h6>`).
- Scroll margin top (`scroll-margin-top`) on heading anchors.

### Focus States

- Interactive elements need visible focus states (`focus-visible:ring-*` or equivalent).
- Never use `outline: none` without focus replacement.
- Use `:focus-visible` over `:focus`.

### Forms

- Inputs need `autocomplete` and meaningful `name` attributes.
- Use correct `type` (`email`, `tel`, `url`, `number`) and `inputmode`.
- Labels must be clickable.
- Placeholders end with `…` (unicode ellipsis) and show example patterns.
- `autocomplete="off"` on non-auth fields to avoid password manager triggers.

### Typography

- Use `…` (unicode ellipsis) instead of `...`.
- Use curly quotes (`“` `”`) instead of straight quotes (`"`).
- Non-breaking spaces for unit formatting (`10&nbsp;MB`, `⌘&nbsp;K`).
- Loading states end with `…`: "Loading…", "Saving…".
- Use `text-wrap: balance` or `text-pretty` on headings.

### Images & Performance

- `<img>` tags need explicit `width` and `height` (prevents CLS).
- Below-the-fold images: `loading="lazy"`.
- Above-the-fold critical images: `fetchpriority="high"`.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
