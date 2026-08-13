---
okf_version: 0.1
type: "documentation"
title: "verify-sitemaps.js API Reference"
description: "Technical specifications, verification rules, and static asset mapping protocols for the sitemap verification utility."
timestamp: "2026-08-01T14:50:00Z"
topics: ["reference", "sitemap", "api", "seo"]

nav_order: 1
---

# 🏗️ `verify-sitemaps.js` API Reference

The `verify-sitemaps.js` script is an automated Node.js test runner that validates plain-text sitemaps, verifies cross-file identity, parses XML sitemaps, and checks that listed links map to compiled assets.

---

## ⚙️ Technical Specifications

- **File Path**: `tools/verify-sitemaps.js`
- **Language**: Node.js (ECMAScript Module format)
- **Dependencies**: Native Node.js filesystem (`fs`) and path (`path`) modules. Zero external npm dependencies.
- **Node Compatibility**: Node.js v22.12.0+

---

## 🛠️ Programmatic Interface

The script is encapsulated inside a single, high-reliability execution function:

### `verifySitemaps()`
Main entry point for sitemap verification. It executes four sequential check blocks:

1.  **Identity Verification**: Compares root `sitemap.txt` and `public/sitemap.txt` to guarantee they are 100% identical in character length and content.
2.  **Syntax Checking**: Validates that all URLs utilize the secure `https://` protocol and do not contain broken JavaScript serialization strings (such as `//undefined` or `[object`).
3.  **Physical File Mapping**: Resolves Netlify URLs listed in `sitemap.txt` and checks whether their corresponding compiled `.html` files exist in the `dist/` directory.
    - `/` maps to `dist/index.html`
    - `/offline` maps to `dist/offline/index.html`
    - `/any-slug` maps to `dist/any-slug/index.html`
4.  **XML Validation**: Parses the compiled `dist/sitemap.xml` file. It validates the XML header declaration, checks `<urlset>` structures, and confirms that multi-host destinations (Netlify, GitHub Pages, and GitBook) are fully indexable.

---

## 📥 Inputs & 📤 Outputs

- **Inputs**:
  - `sitemap.txt`
  - `public/sitemap.txt`
  - Built files under `dist/` (including `dist/sitemap.xml`)
- **Outputs**:
  - **Success (Exit Code 0)**: Outputs complete structured diagnostic logs and prints verification summary.
  - **Failure (Exit Code 1)**: Prints exact mismatch patterns or missing file paths to `stderr` and terminates build/CI processes immediately.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
