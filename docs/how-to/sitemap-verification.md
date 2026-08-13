---
okf_version: 0.1
type: "documentation"
title: "Sitemap Verification How-To Guide"
description: "Instructions on how to verify root and public plain-text sitemaps, built multi-host XML sitemaps, and static file mapping."
timestamp: "2026-08-01T14:45:00Z"
topics: ["how-to", "sitemap", "verification", "seo"]

nav_order: 1
---

# 📋 How to Verify Sitemaps and Link Consistency

This guide details how to execute our automated Node.js validation script to test that compiled sitemaps map correctly to physical HTML pages inside the built `dist/` folder.

---

## 🎯 Prerequisite Actions

Ensure you have run the production build before verifying sitemaps so that compiled static files and `dist/sitemap.xml` exist:

```bash
npm run build
```

---

## 🏗️ Step-by-Step Directions

### Step 1: Run the Sitemap Verification Script
Execute the Node.js validation script from the repository root:

```bash
node tools/verify-sitemaps.js
```

Expected output:
```text
===================================================
🧪 Verifying Sitemap Structure and Links
===================================================
✅ Root and public TXT sitemaps are identical and contain 30 URLs.
✅ All URL patterns in TXT sitemaps are valid (HTTPS and well-formed).
🔍 Validating Netlify URLs against compiled static assets in dist/...
✅ All Netlify URLs successfully mapped to physical built HTML assets in dist/ directory!
🔍 Validating built sitemap.xml...
✅ Built sitemap.xml has valid structure and successfully includes all multi-host publishing destinations!
===================================================
🎉 Verification Script Completed Successfully!
===================================================
```

### Step 2: Validate Multi-Host Targets
The verification engine scans `dist/sitemap.xml` to confirm that it dynamically builds links for three critical multi-host publishing targets:
- **Netlify**: `https://cmsfornerd2.netlify.app/`
- **GitHub Pages**: `https://cmsfornerd.github.io/CMSForNerd2/`
- **GitBook**: `https://cmsfornerd.gitbook.io/cmsfornerd2/`

Verify that all three target strings are reported as successful in your terminal logs.

### Step 3: Verify via Integration Test Suite
To run this verification as part of our automated end-to-end integration test suite, execute the integration test:

```bash
python3 -m pytest tests/test_cms.py -k "test_sitemap_verification"
```

Expected output:
```text
tests/test_cms.py .                                                      [100%]
=========================== 1 passed in 4.50s ===========================
```

---

## 🔍 Troubleshooting Anomalies

### Sitemaps Not Identical
If `sitemap.txt` (root) and `public/sitemap.txt` diverge, the script exits immediately with:

```text
❌ Error: root sitemap.txt and public/sitemap.txt are not identical.
```

**Resolution**: Keep both files perfectly synchronized. Run this bash command to overwrite the public file with the root version:

```bash
cp sitemap.txt public/sitemap.txt
```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
