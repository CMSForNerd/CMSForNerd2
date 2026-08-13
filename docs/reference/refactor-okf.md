---
okf_version: 0.1
type: "documentation"
title: "refactor-okf.cjs API Reference"
description: "Technical specifications, functions, and file validation criteria for the OKF frontmatter crawler utility."
timestamp: "2026-08-01T14:50:00Z"
topics: ["reference", "okf", "api", "utility"]

nav_order: 1
---

# 🏗️ `refactor-okf.cjs` API Reference

The `refactor-okf.cjs` script is a Node.js-based developer utility that recursively crawls the repository, parses Markdown frontmatter, formats strings, and validates schemas against OKF v0.1 guidelines.

---

## ⚙️ Technical Specifications

- **File Path**: `tools/refactor-okf.cjs`
- **Language**: Node.js (CommonJS format)
- **Dependencies**: Native Node.js filesystem (`fs`) and path (`path`) modules. Zero external npm dependencies.
- **Node Compatibility**: Node.js v22.12.0+

---

## 🛠️ Programmatic Interface

The script organizes its functionality into three primary core functions:

### 1. `getMarkdownFiles(dir, files = [])`
Recursively traverses directories to locate all files with a `.md` extension.
- **Parameters**:
  - `dir` (string): The path of the directory to scan.
  - `files` (array, optional): Accumulator array for discovered file paths.
- **Exclusion Filters**: Automatically bypasses `node_modules` and `.git` directories to prevent scanning third-party or internal VCS assets.
- **Returns**: An array of relative file paths.

### 2. `formatValue(key, value)`
Formats a single frontmatter property's raw string value according to OKF rules.
- **Parameters**:
  - `key` (string): The frontmatter property key (case-insensitive).
  - `value` (string): The raw string value parsed from the file.
- **Formatting Protocols**:
  - **Version number**: Overwrites `okf_version` to `0.1` unquoted.
  - **Arrays**: Converts comma-separated brackets (e.g. `[tag1, tag2]`) into compact double-quoted arrays (`["tag1", "tag2"]`).
  - **Booleans**: Preserves `true` or `false` without quotes.
  - **Strings**: Wraps string values containing emojis or special characters (`:`, `[`, `]`) securely in double quotes via `JSON.stringify`.

### 3. `processFile(filePath)`
Parses and reformats a Markdown file's frontmatter block.
- **Parameters**:
  - `filePath` (string): Absolute or relative path to the Markdown document.
- **Repair Protocols**:
  - If `README.md` lacks a frontmatter block entirely, it prepends a default compliant OKF block.
  - Detects missing required keys (`okf_version`, `type`, `title`, `timestamp`, `topics`) and automatically injects standard defaults.
  - Saves modifications back to the filesystem.

---

## 📥 Inputs & 📤 Outputs

- **Inputs**: Read-only access to all Markdown (`.md`) files in the workspace.
- **Outputs**:
  - Overwritten Markdown files with clean, compliant frontmatter formatting.
  - CLI logs detailing scanned files and repair actions.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
