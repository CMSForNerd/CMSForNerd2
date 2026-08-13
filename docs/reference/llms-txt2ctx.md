---
okf_version: 0.1
type: "documentation"
title: "llms_txt2ctx.py CLI Reference"
description: "Technical specifications, Python API, and CLI parameters for parsing llms.txt and generating XML context documents."
timestamp: "2026-08-01T14:50:00Z"
topics: ["reference", "python", "cli", "parser", "llmstxt"]

nav_order: 1
---

# 🏗️ `llms_txt2ctx.py` CLI Reference

The `llms_txt2ctx.py` script is a Python 3 parser utility conforming to the `llmstxt.org` specification. It parses plain-text markdown `llms.txt` files and compiles them into XML documents optimized for AI model ingestion.

---

## ⚙️ Technical Specifications

- **File Path**: `tools/llms_txt2ctx.py`
- **Language**: Python 3 (compatible with Python 3.8+)
- **Dependencies**: Uses Python standard libraries only (`sys`, `os`, `re`, `argparse`). Zero external pip packages required.

---

## 💻 CLI Parameters & Arguments

Execute the parser from your terminal:

```bash
python3 tools/llms_txt2ctx.py <file_path> [options]
```

### Positional Arguments
- `file` (string, required): The relative or absolute path to the target `llms.txt` file (e.g., `llms.txt`).

### Optional Flags
- `-h`, `--help` (flag): Displays standard CLI help information and options specs.
- `--optional` (flag): Includes the `## Optional` section of the `llms.txt` file in the generated XML context. If omitted, optional sections are filtered out for context window efficiency.

---

## 🛠️ Programmatic Python API

The utility exports two main functions for inclusion in third-party Python scripts:

### 1. `parse_llms_txt(txt: str) -> dict`
Parses the markdown contents into a structured dictionary.
- **Parameters**: `txt` (str) — Raw content string of the file.
- **Returns**: A dictionary containing:
  - `'title'`: String containing the main H1 header.
  - `'summary'`: String containing the blockquote summary.
  - `'info'`: String containing non-heading background info.
  - `'sections'`: Dictionary mapping H2 headings to listed hyperlink objects.

### 2. `create_ctx(txt: str, include_optional: bool = False) -> str`
Creates a standardized XML context string.
- **Parameters**:
  - `txt` (str): Raw content string.
  - `include_optional` (bool): If true, includes the optional section.
- **Returns**: XML context string wrapped in `<project>` tags.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
