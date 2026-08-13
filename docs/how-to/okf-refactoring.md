---
okf_version: 0.1
type: "documentation"
title: "OKF Frontmatter Refactoring How-To Guide"
description: "A step-by-step guide explaining how to automatically scan, format, and validate YAML frontmatter across all workspace Markdown files."
timestamp: "2026-08-01T14:45:00Z"
topics: ["how-to", "okf", "validation", "automation"]

nav_order: 1
---

# 📋 How to Run the OKF Frontmatter Refactoring Utility

This guide details how to scan, validate, and automatically repair YAML frontmatter parameters within all workspace Markdown files using our custom Node.js crawler utility.

---

## 🎯 Prerequisite Actions

Ensure you have Node.js v22 installed in your workspace. This script requires no external packages to execute:

```bash
node --version
```

---

## 🏗️ Step-by-Step Directions

### Step 1: Run the Automatic Refactoring Tool
Run the Node.js script located at `tools/refactor-okf.cjs`. This utility recursively crawls all Markdown files in the repository (bypassing `node_modules` and build directories) and validates their metadata formats:

```bash
node tools/refactor-okf.cjs
```

Expected terminal output:
```text
Found 15 markdown files.
Adding missing OKF frontmatter to README.md
Refactored frontmatter: ./docs/README.md
Refactoring complete.
```

### Step 2: Review Frontmatter Repair Actions
The tool automatically performs several essential maintenance tasks:
- **Double-Quotes Special Characters**: Any values containing colons, emojis, or brackets are wrapped securely in double quotes.
- **Formats Arrays**: Topics and tags are reformatted as compact horizontal JSON arrays (e.g., `["dsom", "gitbook"]`).
- **Injects Missing Keys**: If mandatory OKF v0.1 fields (`okf_version`, `type`, `title`, `timestamp`, `topics`) are missing, the script calculates and injects standard defaults.

### Step 3: Run the Compliance Unit Test
To verify that all files conform perfectly to the strict Open Knowledge Format v0.1 scheme, run Pytest:

```bash
python3 -m pytest tests/test_unit.py -k "test_markdown_okf_compliance"
```

Expected output:
```text
tests/test_unit.py .                                                     [100%]
=========================== 1 passed in 0.12s ===========================
```

---

## 🔍 Troubleshooting Anomalies

### Parsing Errors
If a Markdown file has malformed or unclosed YAML indicators (e.g. `---` missing or on the wrong line), the tool will output a warning:

```text
Error: unclosed frontmatter in ./docs/broken-file.md
```

**Resolution**: Open the indicated file and ensure that three hyphens `---` are positioned on **line 1, column 1**, and closed by another `---` on its own line below the metadata block.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
