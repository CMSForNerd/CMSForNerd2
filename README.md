# 🚀 CMSForNerd2 (Modern HTML5 & CSS3 Static Edition)

**CMSForNerd2** is the next-generation, high-performance static modernisation of the legacy database-free PHP CMS.

By migrating from server-side PHP to a purely statically served asset architecture (HTML5, CSS3, and ES6+ JavaScript), CMSForNerd2 delivers ultra-fast rendering speeds, zero-cost scaling, absolute security (no backend execution vulnerability surface), and complete offline capability.

---

## 🏛️ Architectural Transition: Astro SSG

To satisfy the requirements of a database-free, lightweight, and modern tech stack, the architecture has transitioned to **Astro (Static Site Generator)**.

- **Zero-JS by Default**: Standard pages compile to raw, semantic HTML5 and modern CSS3, with zero client-side JavaScript overhead.
- **Modern CSS3**: Built with native CSS variables, flexbox/grid layouts, and scoped modular stylesheets.
- **Type-Safe Content Collections**: Replaces flat-file `.inc` pairs with validated Markdown/MDX content collections.
- **Dual-View Support**: Generates both Desktop and Google-validated Accelerated Mobile Pages (AMP) at build time, completely offline.

---

## 📘 Migration & Integration Documentation

We have compiled comprehensive, human-readable blueprint guides detailing the research, framework evaluation, and step-by-step transition plan:

*   **[Static Migration Guide](docs/migration-guide.md)** — The complete playbook for converting legacy PHP layouts, router, controllers, and PWA logic to Astro, HTML5, CSS3, and Vite.
*   **[Context7 Integration Guide](docs/context7-integration.md)** — Complete configuration guidelines for synchronising repository documentation with Context7 services using GitLab CI and GitHub Actions.

---

## 🗺️ Project Navigation

- [START-HERE.md](START-HERE.md) — Master onboarding map for human developers and AI agents.
- [SUMMARY.md](SUMMARY.md) — Structural index for documentation compilation and GitBook integration.
- [llms.txt](llms.txt) — High-density directory map optimised for external AI crawlers.

---

## 🛠️ Getting Started with CMSForNerd2

### Installation

To bootstrap the workspace locally:

```bash
# Clone this repository
git clone https://github.com/CMSForNerd/CMSForNerd2.git
cd CMSForNerd2

# Initialize the Astro workspace
npm create astro@latest -- --template minimal --install --git false

# Start the local development server
npm run dev &
```

### Production Build

To compile the entire website into statically served assets:

```bash
npm run build
```
This writes the fully optimised production-ready HTML5, CSS3, and JavaScript files to the dist/ directory, which can be served by any static host or unprivileged web server.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
