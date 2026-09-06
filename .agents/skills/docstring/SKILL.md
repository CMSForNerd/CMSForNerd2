---
spec_version: "0.2"
type: "skill"
skill_id: "docstring"
name: "docstring"
title: "Docstring and API Reference Standard Skill"
description: "Provides structured guidelines for writing PEP-257 Google-style Python docstrings and detailed JSDoc comments."
version: "1.1.0"
timestamp: "2026-09-06T00:00:00Z"
author: "AI Workspace Assistant"
tags: ["docstring", "jsdoc", "pep257", "google-style", "python", "typescript"]
status: "stable"
sources:
  - id: "pytorch_docstring"
    title: "PyTorch Docstring Guidelines"
    url: "https://github.com/pytorch/pytorch"
  - id: "google_python_styleguide"
    title: "Google Python Style Guide"
    url: "https://google.github.io/styleguide/pyguide.html"
inputs:
  code_snippet:
    type: "string"
    description: "Function, class, or module code requiring docstring or JSDoc annotation."
outputs:
  documented_code:
    type: "string"
    description: "Code updated with standardized PEP-257 or JSDoc documentation blocks."

okf_version: "0.1"
---

# Docstring & API Reference Standard Skill (`docstring`)

The `docstring` skill enforces function-level, module-level, and API reference documentation standards across Python, JavaScript, and TypeScript codebases.

## Operational Standards

1. **Python Docstrings (PEP-257 & Google Style)**:
   - Include raw strings (`r"""..."""`) when LaTeX math or backslashes are present.
   - Every public module, function, and class must declare `Args`, `Returns`, `Raises`, and `Example` sections where appropriate.
   - Explain function intent, contracts, side effects, and failure modes rather than repeating code line-by-line.

2. **TypeScript & JavaScript JSDoc Comments**:
   - Provide file header `@file` overview JSDoc comments for all scripts.
   - Annotate all exported functions with `@param`, `@returns`, and `@throws`.

3. **Code Example Hygiene**:
   - Ensure provided docstring code examples are tested, valid, and reproducible.

## FAQs

### When should raw docstrings (`r"""..."""`) be used?
Use raw triple-quoted strings whenever docstrings contain backslashes, regular expressions, or LaTeX notation.

### Can this skill be used for non-PyTorch / non-Python languages?
Yes, while inspired by PyTorch and Google Python conventions, the core principles apply to JSDoc (JavaScript/TypeScript) and function comment standards.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-06*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
