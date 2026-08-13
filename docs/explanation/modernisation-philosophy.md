---
okf_version: 0.1
type: "documentation"
title: "PHP-to-Static Modernisation Philosophy"
description: "Architectural concepts, performance impacts, and design decisions behind modernising CMSForNerd to Astro SSG."
timestamp: "2026-08-01T15:00:00Z"
topics: ["explanation", "architecture", "migration", "static", "php"]

nav_order: 1
---

# 🧠 PHP-to-Static Modernisation Philosophy

This document explains the core architectural reasoning, conceptual principles, and technical design decisions behind the transition from the legacy database-free PHP CMS (**CMSForNerd**) to the modern static-site generator architecture (**CMSForNerd2**).

---

## 🏛️ Context & Origins

The legacy **CMSForNerd** was created to address the overhead of database-driven systems (such as WordPress). It relied on flat-file JSON and HTML fragment files compiled dynamically at runtime by PHP 8.4. While this approach eliminated database vulnerabilities (like SQL injection) and reduced server complexity, it still required:
1.  **Dynamic Runtime Compute**: Every page view forced the PHP-FPM worker engine to reconstruct components and templates, placing an execution load on server CPUs.
2.  **Server Security Concerns**: Hosting PHP-FPM opens vectors for common runtime exploits, such as Local File Inclusion (LFI), command injection, or directory traversal.
3.  **Complex Dual Rendering**: Managing separate mobile layouts (AMP) and desktop layouts at runtime required custom PHP router query parsing (`?view=amp`).

---

## 🏗️ Astro Static Site Generator (SSG) Design

To eliminate runtime execution compute while preserving the database-free, content-first philosophy, **CMSForNerd2** standardizes on **Astro SSG (Static Site Generator)**.

### 1. Zero Runtime JS Footprint
Astro acts as a compiler rather than a heavy client-side framework. By default, it strips all JavaScript from the final output, producing only pure, pre-rendered HTML5 and CSS3. JavaScript is only bundled if client hydration is explicitly requested, maximizing responsiveness and lowering payload size.

### 2. Pair Logic Replicated via Component-Frontmatter
The legacy PHP CMS used a custom controller pattern where metadata was declared first, loading HTML body fragments next. Astro mirrors this cleanly via **component frontmatter**:

```astro
---
// Build-time execution only
const title = "Clean Architecture";
---
<html lang="en">
  <h1>{title}</h1>
</html>
```

Variables inside the frontmatter code block `---` run purely at build time. The client receives static compiled elements, avoiding any runtime server-side execution.

### 3. Dynamic Dual-View Generation (Standard & AMP)
Rather than executing complex runtime query strings, Astro builds dual outputs statically at compile time:
- Standard desktop files are generated at `dist/[slug]/index.html`.
- Mobile-optimized, strictly-validated Accelerated Mobile Pages (AMP) are compiled to `dist/[slug]/amp/index.html`.

This structure keeps all routes statically accessible offline and allows deployment to zero-compute environments (such as free static CDNs).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
