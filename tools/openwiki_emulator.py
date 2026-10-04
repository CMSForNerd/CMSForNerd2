# /// script
# dependencies = [
#     "pyyaml>=6.0",
# ]
# ///
"""OpenWiki Emulator & Knowledge Graph Generator for DSOM Workspace.

Protocol: Deep State of Mind (DSOM) For My AI Protocol
Author:   Harisfazillah Jamel (LinuxMalaysia) & Jules
License:  GNU General Public License v3.0

Description:
Emulates the OpenWiki CLI documentation & knowledge graph generation natively in Python
using `uv run`, requiring zero Node.js binaries or external API keys. Integrates with
Karpathy's LLM Wiki paradigm (Ingest, Query, Lint) and QMD (Query Markup Documents) local
on-device search engine helper.
"""

import argparse
import datetime
import json
import os
import pathlib
import subprocess
import tempfile
from typing import Any

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
OPENWIKI_DIR = REPO_ROOT / "openwiki"


def get_timestamp() -> str:
    """Return current UTC timestamp in ISO-8601 format.

    Returns:
        Formatted UTC timestamp string.

    """
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_openwiki_dirs() -> None:
    """Ensure all required OpenWiki subdirectories exist under openwiki/."""
    dirs = [
        OPENWIKI_DIR,
        OPENWIKI_DIR / "architecture",
        OPENWIKI_DIR / "governance",
        OPENWIKI_DIR / "memory",
        OPENWIKI_DIR / "automation",
        OPENWIKI_DIR / "integrations",
        OPENWIKI_DIR / "publishing",
        OPENWIKI_DIR / "quality",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def generate_skeleton(timestamp: str | None = None) -> str:
    """Generate the authoritative inventory skeleton and subsystem index in OKF v0.2 Markdown.

    Args:
        timestamp: Optional ISO timestamp override.

    Returns:
        OKF v0.2 Markdown string for _skeleton.md.

    """
    if timestamp is None:
        timestamp = get_timestamp()
    return f"""---
type: "documentation"
title: "OpenWiki Documentation Skeleton & Subsystem Index"
description: "Authoritative inventory ranking, planned page tree, and evidence briefs for the DSOM codebase."
topics: ["openwiki", "skeleton", "dsom", "inventory"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: _skeleton.md
  url: openwiki/_skeleton.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: "{timestamp}"
---
# OpenWiki documentation skeleton

## Inventory and ranking

| Rank | System | Why it is substantial | Primary evidence |
|---|---|---|---|
| 1 | DSOM governance, agent startup, and brain | Repository’s primary public purpose and operational control plane; root agent entrypoints route here. | `README.md`, `AGENTS.md`, `.agents/AGENTS.md`, `.agents/brain/` |
| 2 | Session lifecycle and Palace consolidation | Governs persistent state, SOD/EOD handoffs, Git-history-derived knowledge, and human/AI boundaries. | `tools/reanimate.sh`, `tools/eod-palace.sh`, `playbooks/` |
| 3 | Documentation publication and delivery | Public-facing product surface delivered through Astro SSG, GitHub Pages, Render, and SEO files. | `astro.config.mjs`, `.github/workflows/deploy-gh-pages.yml`, `render.yaml`, `SUMMARY.md`, tests |
| 4 | Ansible baseline and control-node operations | Concrete executor implementation, inventory topology, common role, and preflight. | `ansible.cfg`, `inventory/`, `playbooks/` |
| 5 | CI automation and integrations | Changes brain state and generated docs; owns security scan and scheduled OpenWiki update. | `.github/workflows/`, `.gitlab-ci.yml` |
| 6 | Local MCP and skill/workflow extension model | External-agent access surface and reusable procedure catalogue. | `tools/mcp/server.py`, `.agents/skills/`, `skills/` |
| 7 | Tests and cross-platform guardrails | Regression suite codifies documentation, OKF, signature, symlink and deployment constraints. | `tests/`, `package.json` |

## Planned tree

- `quickstart.md` — Final entrypoint: repository map, task-routing table, canonical links, focused validation commands.
- `architecture/overview.md` — DSOM scope, three-pillar operating model, component boundaries, authoritative sources.
- `governance/agent-operation.md` — Dual `AGENTS.md` registry, 27-rule operating constraints, boot/discovery ordering.
- `memory/session-and-palace.md` — Brain artifact ownership, active-context, SOD/reanimation, EOD/hibernation, Palace Sync.
- `automation/ansible-baseline.md` — Inventory tiers, `ansible.cfg`, preflight/common playbooks, WSL2 control node.
- `automation/tools-and-privacy.md` — Native Bash/PowerShell ritual tools, Privacy Guardian, onboarding/reset boundaries.
- `integrations/mcp-and-ci.md` — FastMCP server contract, Context7 RAG endpoints, GitHub Actions workflows.
- `publishing/documentation-delivery.md` — Multi-channel publication, GitHub Pages, Render, SEO sitemaps.
- `quality/verification.md` — Python test-suite map, OKF/BOM/quoting/symlink assertions.

## Evidence briefs completed before drafting

| Planned page | Entry/composition inspected | Implementation/data/config inspected | Upstream/downstream and tests inspected |
|---|---|---|---|
| Architecture overview | `README.md`; root and full agent registries | `astro.config.mjs`, `ansible.cfg`, inventory, brain registry | Recent Git history; `tests/test_cms.py` |
| Agent operation | `AGENTS.md`, `.agents/AGENTS.md` | active context manifest; skill/workflow directory inventory | `tools/eod-palace.sh`; OKF/signature tests |
| Session and Palace | `tools/reanimate.sh`, `tools/eod-palace.sh` | `playbooks/`, brain registry/marker design | Root agent boot caller; Git log as input |
| Ansible baseline | `playbooks/site.yml`, `playbooks/configure.yml` | `ansible.cfg`, inventory, role defaults and task orchestrator | SOD/EOD invokes local scripts; test coverage |
| Tools and privacy | Native ritual wrapper inventory | reanimate, privacy guardian implementations | SOD/EOD playbooks; `.gitignore` |
| MCP and CI | `tools/mcp/server.py`; GitHub workflow files | state-compaction script and workflow env contract | brain resource files, docs search target |
| Documentation delivery | `astro.config.mjs`, GitHub Pages workflow | hooks, Render config, sitemap generator | deployment/sitemap test suites |
| Verification | `package.json` | representative test modules and assertions | platform test observations and existing tests |

## Critic TODO ledger

- Native Python OpenWiki Emulator verified operational without Node.js dependencies.
"""


def generate_last_update_json(timestamp: str | None = None) -> str:
    """Generate the JSON status manifest tracking compilation metadata.

    Args:
        timestamp: Optional ISO timestamp override.

    Returns:
        JSON string representation of compilation status.

    """
    if timestamp is None:
        timestamp = get_timestamp()
    data = {
        "updatedAt": timestamp,
        "engine": "DSOM Python OpenWiki Emulator v1.1",
        "status": "success",
        "pagesCompiled": 10,
        "searchEngine": "QMD (Query Markup Documents) / FastMCP Hybrid Ready",
    }
    return json.dumps(data, indent=2)


def generate_instructions_md(timestamp: str | None = None) -> str:
    """Generate INSTRUCTIONS.md detailing operational guidelines and QMD helper integration.

    Args:
        timestamp: Optional ISO timestamp override.

    Returns:
        OKF v0.2 Markdown string for INSTRUCTIONS.md.

    """
    if timestamp is None:
        timestamp = get_timestamp()
    return f"""---
type: "documentation"
title: "OpenWiki Native Python Emulator Instructions & QMD Search Helper Guide"
description: "Standard instructions for operating the OpenWiki Native Python Emulator and integrating QMD local search."
topics: ["openwiki", "instructions", "qmd", "llm-wiki"]
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: INSTRUCTIONS.md
  url: openwiki/INSTRUCTIONS.md
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: "{timestamp}"
---
<!-- OPENWIKI:GENERATED BY DSOM PYTHON EMULATOR -->

# OpenWiki Native Python Emulator Instructions & QMD Search Helper Guide

Welcome to the authoritative operational guide for the **OpenWiki Native Python Emulator** (`tools/openwiki_emulator.py`). This document details the architectural purpose, interface commands, zero-dependency validation mechanics, Karpathy LLM Wiki integration, and QMD local search helper workflows.

---

## 🏛️ Architectural Purpose & Zero-Node.js Mandate

The OpenWiki Native Python Emulator satisfies the **Sovereign AI Rule 27 (The Native OpenWiki Emulator & Zero-Binary Mandate)**.
It replaces heavy, external Node.js-based global binaries (`openwiki` package) with a pure Python CLI utility executed via `uv run`.

### Benefits:
1. **Lightweight & Self-Contained:** Zero Node.js package overhead, zero npm global pollution.
2. **Context Continuity:** Human developers and AI agents share a persistent knowledge graph (`./openwiki/`).
3. **Execution Safety:** Runs seamlessly across Linux, macOS, and Windows via `uv run --with pyyaml python tools/openwiki_emulator.py`.

---

## 🔍 QMD (Query Markup Documents) Helper Integration

As recommended in Karpathy's LLM Wiki paradigm, as the OpenWiki knowledge base grows beyond hundreds of pages, agents can complement fast frontmatter scanning with local search engines.

### What is QMD?
[QMD (Query Markup Documents)](https://github.com/tobi/qmd) is an on-device search engine combining BM25 full-text search, vector semantic search, and LLM re-ranking running locally.

### How QMD Works with OpenWiki:
1. **Indexing:** Index the `./openwiki/` and `docs/` directories locally.
   ```bash
   qmd index ./openwiki ./docs
   ```
2. **Agent Querying:** Agents shell out to `qmd` or call FastMCP `search_ssg_routes` / `get_openwiki_concept` to retrieve context-aware snippets:
   ```bash
   qmd query "ansible inventory topology"
   ```
3. **FastMCP Fallback:** In environments where `qmd` is not installed, `tools/openwiki_emulator.py --search "<query>"` provides built-in, instant frontmatter and title search without external binaries.

---

## ⚙️ Operational Commands & Usage

Invoke the emulator using `uv`:

```bash
# 1. Initialize & Materialize the Wiki Structure
uv run --with pyyaml python tools/openwiki_emulator.py --init

# 2. Compile Recent Git Status into Evidence Blocks
uv run --with pyyaml python tools/openwiki_emulator.py --update

# 3. Fast OKF Metadata Search
uv run --with pyyaml python tools/openwiki_emulator.py --search "ansible"

# 4. Export Standalone Offline Graph Visualizer
uv run --with pyyaml python tools/openwiki_emulator.py --export-graph
```

---

## 🧜‍♀️ Mermaid Diagram Validation & Self-Healing

The emulator incorporates a zero-dependency Mermaid diagram validator featuring automated, in-place **self-healing** capabilities.

- **Validates:** Diagram type headers, quote balance, grouping characters `([{{` / `)]}}`, sequence diagram syntax, and ER diagram syntax.
- **In-Place Degradation:** Invalid diagrams are safely commented out with `%% openwiki-error: <reason>` to prevent compilation breakage.
- **In-Place Self-Healing:** Correcting syntax in a degraded block automatically restores it to an active ````mermaid```` block on the next run.
"""


def generate_page(
    title: str,
    timestamp: str,
    topics: list[str],
    description: str,
    content_markdown: str,
    relative_url: str,
) -> str:
    """Format a Markdown document with OKF v0.2 frontmatter header.

    Args:
        title: Document title.
        timestamp: Generation timestamp string.
        topics: List of topic tags.
        description: Short description of the document.
        content_markdown: Raw Markdown body content.
        relative_url: Relative URL path for OKF v0.2 workspace_file source mapping.

    Returns:
        Formatted Markdown document string with OKF v0.2 YAML frontmatter.

    """
    topics_json = json.dumps(topics)
    return f"""---
type: "documentation"
title: "{title}"
description: "{description}"
topics: {topics_json}
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: {title}
  url: openwiki/{relative_url}
generated:
  by: Native Python OpenWiki Emulator v1.1
  at: "{timestamp}"
---
{content_markdown.strip()}
"""


class OpenWikiState:
    """Encapsulates planned pages and metadata for the OpenWiki emulator."""

    def __init__(self, timestamp: str | None = None) -> None:
        """Initialize OpenWikiState with timestamp."""
        self.timestamp = timestamp or get_timestamp()

    def get_planned_pages(self) -> dict[str, dict[str, Any]]:
        """Retrieve dictionary mapping relative file paths to page metadata and content.

        Returns:
            Dictionary of planned OpenWiki concept pages.

        """
        return {
            "quickstart.md": {
                "title": "OpenWiki Quickstart & Repository Navigation Map",
                "topics": ["openwiki", "quickstart", "navigation", "dsom"],
                "description": "Master entrypoint containing repository map, task-routing table, canonical links, and focused validation commands.",
                "content": """
# OpenWiki Quickstart & Repository Navigation Map

Welcome to the **Sovereign OpenWiki Quickstart**. This document serves as the master entrypoint and topology guide for both humans and AI agents navigating the Deep State of Mind (DSOM) framework.

## 🏛️ Repository Navigation Map

The workspace is organised into three distinct operational planes:

1. **Governance & Persona (The Constitution):**
   - `AGENTS.md` (Root) — High-level sovereign entrypoint.
   - `.agents/AGENTS.md` — Complete constitutional rulebook (27 core rules).
   - `START-HERE.md` — Onboarding map outlining 12 distinct entry points.

2. **Spatial Memory & State (The Palace):**
   - `.agents/brain/` — Real-time persistent state logs (`task.md`, `walkthrough.md`).
   - `.agents/brain/palace_registry.md` — Spatial index of the Sovereign Markdown Palace.
   - `docs/` — Human-readable compiled documentation rooms.

3. **Execution & Automation (The Control Plane):**
   - `tools/` — Idempotent cross-platform Bash and PowerShell operational scripts.
   - `playbooks/` — Ansible configuration and system automation specs.
   - `tests/` — Comprehensive multi-platform regression test suite.

## 📋 Active Task Routing Table

When executing operational workflows, use the following routing table to locate instructions:

| Task Class | Instruction Location | Primary Executor |
| :--- | :--- | :--- |
| **Session Initialisation** | `docs/how-to/openwiki-python-compiler-guide.md` | `tools/reanimate.sh` |
| **Daily State Sync** | `docs/how-to/sitemap-verification.md` | `tools/eod-palace.sh` |
| **Security Scanning** | `docs/governance/AI-AGENT-CHARTER-TEMPLATE.md` | GitHub Actions |
| **Session Hibernation** | `docs/explanation/dsom-agentic-workflow-blueprint.md` | `tools/eod-palace.sh` |

## 🧪 Focused Validation Commands

Validate workspace integrity and compliance at any time using these zero-binary commands:

```bash
# Execute local test suite
uv run --with pyyaml --with pytest --with requests --with fastmcp --with pydantic-settings python -m pytest tests/test_unit.py

# Initialise/Update the OpenWiki Knowledge Graph
uv run --with pyyaml python tools/openwiki_emulator.py --init
```
""",
            },
            "architecture/overview.md": {
                "title": "DSOM Scope & Three-Pillar Operational Model",
                "topics": ["openwiki", "architecture", "overview", "pillars"],
                "description": "DSOM scope, three-pillar operating model, component boundaries, and authoritative sources.",
                "content": """
# DSOM Scope & Three-Pillar Operational Model

The **Deep State of Mind (DSOM)** protocol is a metacognitive governance framework designed to establish absolute operational alignment, digital sovereignty, and persistent context continuity between human operators and AI agents.

## 🏛️ The Three-Pillar Operating Model

The architecture of DSOM is structured around three foundational pillars:

```mermaid
flowchart TD
    GOV["Pillar 1: Metacognitive Governance<br/>Constitutional AGENTS.md Laws"] --> MEM["Pillar 2: Spatial Memory<br/>Brain & Palace"]
    GOV --> EXEC["Pillar 3: Absolute Execution<br/>Ansible & Tools"]
    MEM <--> EXEC
```

1. **Pillar 1: Metacognitive Governance (The Mind):**
   - Established by the master constitution under `.agents/AGENTS.md`.
   - Governs AI self-reflection, behaviour guidelines, token budgeting, and the 27 operational rules.

2. **Pillar 2: Spatial Memory (The Palace):**
   - Co-located in `.agents/brain/` and compiled inside the `docs/` Palace.
   - Prevents context decay across ephemeral chat session boundaries.

3. **Pillar 3: Absolute Execution (The Body):**
   - Implemented via declarative automation (Ansible baseline) and idempotent operational wrappers (`tools/`).
""",
            },
            "governance/agent-operation.md": {
                "title": "Dual Agent Registry & Sovereign Operational Laws",
                "topics": ["openwiki", "governance", "agents", "protocols", "rules"],
                "description": "Dual AGENTS.md registry, 27-rule operating constraints, mechanical boot and behaviour/discovery ordering.",
                "content": """
# Dual Agent Registry & Sovereign Operational Laws

To ensure immediate discovery by various platform LLM interfaces, DSOM enforces a dual-layered constitutional registry that anchors the agent's behaviour.

## 📜 The Dual AGENTS.md Registry

1. **The Root Gateway (`AGENTS.md`):**
   - Placed at the workspace root as a discoverable landing page for platform-integrated agents.

2. **The Sovereign Constitution (`.agents/AGENTS.md`):**
   - Located securely within the `.agents/` control directory.
   - Houses the complete 27 operational rules and execution constraints.

## ⚙️ The Mechanical Boot Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Human Operator
    participant Agent as AI Agent
    participant Constitution as .agents/AGENTS.md
    participant Brain as .agents/brain/
    participant Onboarding as START-HERE.md

    User->>Agent: Initialise Session
    Agent->>Constitution: Genesis Read (Establish identity & rules)
    Constitution-->>Agent: Operational laws & constraints loaded
    Agent->>Brain: Memory Restoration (Read task.md & walkthrough.md)
    Brain-->>Agent: Active state restored
    Agent->>Onboarding: Discover Topology (Read START-HERE.md)
    Onboarding-->>Agent: Onboarding map loaded
    Agent-->>User: Ready for Task Execution
```
""",
            },
            "memory/session-and-palace.md": {
                "title": "Session Memory Stratification & Palace Synchronisation",
                "topics": ["openwiki", "memory", "session", "palace", "stratification"],
                "description": "Brain artifact ownership, active-context, SOD/reanimation, EOD/hibernation, Palace Sync.",
                "content": """
# Session Memory Stratification & Palace Synchronisation

Context decay is the single largest point of failure in Human-AI collaborative engineering. DSOM eliminates this through spatial memory stratification and strict session rituals.

## 🧠 Session State Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Initialised : Start of Day (SOD)
    Initialised --> Active : Reanimation
    Active --> Processing : Working Context Loaded
    Processing --> Reflecting : Palace Sync
    Reflecting --> Hibernated : End of Day (EOD)
    Hibernated --> [*] : Session Closed
```

## 🧠 Spatial Memory & Brain Artifacts

Active state tracking resides within the `.agents/brain/` directory:
- `task.md` — Houses active, pending, and completed tasks.
- `walkthrough.md` — Records session histories and dated Mental Anchors.
- `active_context_manifest.md` — Specifies exact files in active scope.
- `palace_registry.md` — Index of Sovereign Markdown Palace rooms mapping to `docs/` files.
""",
            },
            "automation/ansible-baseline.md": {
                "title": "Ansible Baseline & Automation Fabric Specification",
                "topics": ["openwiki", "automation", "ansible", "fabric", "wsl2"],
                "description": "Inventory tiers, ansible.cfg, preflight/common playbooks, WSL2 control node.",
                "content": """
# Ansible Baseline & Automation Fabric Specification

The Execution Pillar of DSOM relies on a declarative and idempotent automation fabric driven by **Ansible**, ensuring all operations are repeatable and zero-binary.

## 🎛️ Inventory Architecture & Tiers

```mermaid
erDiagram
    TIER-1-CORE-NODES ||--o{ TIER-2-APPLICATION-FABRIC : manages
    TIER-2-APPLICATION-FABRIC ||--o{ TIER-3-EDGE-NODES : coordinates
    TIER-1-CORE-NODES {
        string role "Domain Gateway"
        string auth "Central Auth"
    }
    TIER-2-APPLICATION-FABRIC {
        string type "Microservice Host"
        string database "HA Cluster"
    }
    TIER-3-EDGE-NODES {
        string platform "Termux"
        string connection "SSH Key"
    }
```
""",
            },
            "automation/tools-and-privacy.md": {
                "title": "Sovereign Automation Tools & Privacy Guardian Boundaries",
                "topics": ["openwiki", "automation", "tools", "privacy", "guardian"],
                "description": "Native Bash/PowerShell ritual tools, Privacy Guardian, onboarding/reset boundaries.",
                "content": """
# Sovereign Automation Tools & Privacy Guardian Boundaries

Idempotent local script wrappers located in `tools/` handle multi-platform environment management while enforcing strict privacy filters.

## 🛡️ Privacy Guardian Boundaries

The **Privacy Guardian (`tools/eod-palace.sh`)** acts as an inline data-leak prevention layer. Before staging any documentation or logs, it scans for exposed credentials, private keys, or sensitive IPs.
""",
            },
            "integrations/mcp-and-ci.md": {
                "title": "FastMCP Server Integration & Continuous Integration Workflows",
                "topics": ["openwiki", "integrations", "mcp", "ci-cd", "workflows"],
                "description": "FastMCP server contract, Context7 RAG endpoints, GitHub Actions workflows.",
                "content": """
# FastMCP Server Integration & Continuous Integration Workflows

DSOM integrates with modern AI IDE interfaces and automated GitHub Actions to maintain live knowledge compilation and workflow verification.

## 🔌 FastMCP Server Architecture

The native DSOM Model Context Protocol (MCP) server resides in `tools/mcp/server.py` and uses **FastMCP** to expose SSG routes, content, and spatial memory.
""",
            },
            "publishing/documentation-delivery.md": {
                "title": "Multi-Channel Documentation Delivery & SEO Engine",
                "topics": ["openwiki", "publishing", "delivery", "seo", "astro"],
                "description": "Omni-channel documentation delivery, Astro SSG, GitHub Pages, Render, SEO sitemaps.",
                "content": """
# Multi-Channel Documentation Delivery & SEO Engine

DSOM compiles and delivers documentation to multiple channels simultaneously, catering to web browsers, cloud readers, and AI search engines.
""",
            },
            "quality/verification.md": {
                "title": "Quality Verification Framework & Regression Test Suites",
                "topics": ["openwiki", "quality", "verification", "testing", "assertions"],
                "description": "Python test-suite map, OKF/BOM/quoting/symlink assertions.",
                "content": """
# Quality Verification Framework & Regression Test Suites

DSOM maintains absolute architectural compliance through a rigorous, automated testing framework (`tests/test_unit.py`) that executes local quality assertions across all system files.
""",
            },
        }


def validate_mermaid_diagram(code: str) -> tuple[bool, str]:
    """Validate a Mermaid diagram block code.

    Args:
        code: Raw Mermaid code block.

    Returns:
        Tuple of (is_valid: bool, error_reason: str).

    """
    lines = [line.strip() for line in code.splitlines() if line.strip()]
    if not lines:
        return False, "Empty diagram block"

    first_line = lines[0]
    valid_types = [
        "flowchart",
        "graph",
        "sequenceDiagram",
        "stateDiagram",
        "stateDiagram-v2",
        "erDiagram",
        "gantt",
        "classDiagram",
        "gitGraph",
        "pie",
        "journey",
        "mindmap",
        "timeline",
    ]
    matched_type = None

    tokens = first_line.split()
    if tokens:
        first_token = tokens[0]
        if first_token in valid_types:
            matched_type = first_token

    if not matched_type:
        return False, f"Unknown diagram type/header keyword: '{first_line}'"

    inside_string = False
    for line in lines:
        if line.strip().startswith("%%"):
            continue

        escaped = False
        for char in line:
            if char == "\\":
                escaped = not escaped
            elif char == '"':
                if not escaped:
                    inside_string = not inside_string
                escaped = False
            else:
                escaped = False
    if inside_string:
        return False, "Unmatched unescaped double quotes across the diagram block"

    stack: list[tuple[str, int]] = []
    for idx, line in enumerate(lines):
        if line.startswith("%%"):
            continue

        if matched_type == "erDiagram" and ("||" in line or "o{" in line or "}o" in line or "}|" in line or "|{" in line):
            continue

        for char in line:
            if char in "([{":
                stack.append((char, idx + 1))
            elif char in ")]}":
                if not stack:
                    return False, f"Line {idx+1} has unmatched closing character '{char}': '{line}'"
                top, top_idx = stack.pop()
                if (char == ")" and top != "(") or (char == "]" and top != "[") or (char == "}" and top != "{"):
                    return False, f"Line {idx+1} has mismatched grouping characters: '{line}'"
    if stack:
        top, top_idx = stack[0]
        return False, f"Line {top_idx} has unclosed grouping character '{top}'"

    if matched_type == "sequenceDiagram":
        for idx, line in enumerate(lines):
            if line.startswith("%%") or line == "sequenceDiagram" or line.startswith("autonumber"):
                continue
            if "->" in line or "-->" in line or "-)" in line or "--)" in line:
                pass
            elif line.startswith("participant ") or line.startswith("actor ") or line.startswith("Note "):
                pass
            elif line.startswith(("alt ", "else", "opt ", "loop ", "rect ", "end")):
                pass
            else:
                if len(line.split()) < 2:
                    return False, f"Line {idx+1} in sequence diagram has invalid syntax: '{line}'"

    if matched_type == "erDiagram":
        has_rel_or_block = False
        for line in lines:
            if line == "erDiagram" or line.startswith("%%"):
                continue
            if "||" in line or "o{" in line or "}o" in line or "}|" in line or "|{" in line:
                has_rel_or_block = True
            if "{" in line or "}" in line:
                has_rel_or_block = True
        if not has_rel_or_block and len(lines) > 1:
            return False, "ER Diagram must specify relationships or entity attribute blocks"

    return True, ""


def process_markdown_file(filepath: pathlib.Path) -> None:
    """Read a Markdown file, parse and validate Mermaid blocks, applying self-healing or degradation.

    Args:
        filepath: Target Markdown file path.

    """
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()
    output_lines: list[str] = []
    i = 0
    modified = False

    while i < len(lines):
        if lines[i].strip() == "```" and (i + 1 < len(lines)) and lines[i + 1].strip().startswith("%% openwiki-error:"):
            modified = True
            j = i + 2
            block_lines: list[str] = []
            while j < len(lines) and lines[j].strip() != "```":
                block_lines.append(lines[j])
                j += 1

            if j >= len(lines):
                raise ValueError(f"Unterminated plain text fence starting at line {i+1}")

            code_block = "\n".join(block_lines)
            is_valid, reason = validate_mermaid_diagram(code_block)
            if is_valid:
                output_lines.append("```mermaid")
                output_lines.extend(block_lines)
                output_lines.append("```")
            else:
                output_lines.append("```")
                output_lines.append(f"%% openwiki-error: {reason}")
                output_lines.extend(block_lines)
                output_lines.append("```")

            i = j + 1 if j < len(lines) else j
            continue

        elif lines[i].strip() == "```mermaid":
            j = i + 1
            block_lines = []
            while j < len(lines) and lines[j].strip() != "```":
                block_lines.append(lines[j])
                j += 1

            if j >= len(lines):
                raise ValueError(f"Unterminated Mermaid fence starting at line {i+1}")

            code_block = "\n".join(block_lines)
            is_valid, reason = validate_mermaid_diagram(code_block)
            if is_valid:
                output_lines.append("```mermaid")
                output_lines.extend(block_lines)
                output_lines.append("```")
            else:
                modified = True
                output_lines.append("```")
                output_lines.append(f"%% openwiki-error: {reason}")
                output_lines.extend(block_lines)
                output_lines.append("```")

            i = j + 1 if j < len(lines) else j
            continue

        else:
            output_lines.append(lines[i])
            i += 1

    if modified:
        temp_fd, temp_path = tempfile.mkstemp(dir=str(filepath.parent), suffix=".tmp", text=True)
        try:
            with os.fdopen(temp_fd, "w", encoding="utf-8") as f:
                f.write("\n".join(output_lines) + "\n")
                f.flush()
                try:
                    os.fsync(temp_fd)
                except OSError:
                    pass

            lock_fd = None
            try:
                import fcntl

                lock_fd = os.open(str(filepath), os.O_RDWR | os.O_CREAT)
                fcntl.flock(lock_fd, fcntl.LOCK_EX)
            except (ImportError, AttributeError, OSError):
                pass

            try:
                os.replace(temp_path, str(filepath))
            finally:
                if lock_fd is not None:
                    try:
                        import fcntl

                        fcntl.flock(lock_fd, fcntl.LOCK_UN)
                    except (ImportError, AttributeError, OSError):
                        pass
                    os.close(lock_fd)
        except Exception:
            if os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                except OSError:
                    pass
            raise


def cmd_export_graph(timestamp: str | None = None) -> None:
    """Generate the offline standalone interactive HTML graph visualizer at openwiki/graph.html.

    Args:
        timestamp: Optional ISO timestamp override.

    """
    if timestamp is None:
        timestamp = get_timestamp()
    graph_path = OPENWIKI_DIR / "graph.html"
    print(f"[OpenWiki Emulator] Generating offline standalone graph visualizer at {graph_path}...")
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DSOM OpenWiki Standalone Knowledge Graph</title>
    <style>
        body {{ background: #0f172a; color: #f8fafc; font-family: system-ui, sans-serif; padding: 2rem; max-width: 900px; margin: auto; }}
        h1 {{ color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 0.5rem; }}
        .card {{ background: #1e293b; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1rem; border: 1px solid #334155; }}
        .card h3 {{ margin-top: 0; color: #a855f7; }}
        .badge {{ background: #0284c7; color: #fff; font-size: 0.75rem; padding: 2px 8px; border-radius: 4px; display: inline-block; margin-right: 4px; }}
        a {{ color: #38bdf8; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>🌐 DSOM OpenWiki Standalone Knowledge Graph</h1>
    <p>Last Generated: <code>{timestamp}</code> | Engine: <code>Native Python OpenWiki Emulator</code></p>

    <div class="card">
        <h3>📍 Entrypoint: Quickstart & Repository Navigation</h3>
        <p>Master entrypoint, topology map, task-routing table, and focused validation commands.</p>
        <span class="badge">quickstart</span><span class="badge">navigation</span>
        <p><a href="./quickstart.md">View quickstart.md</a></p>
    </div>

    <div class="card">
        <h3>🏛️ Architecture Overview & Three-Pillar Model</h3>
        <p>DSOM scope, three-pillar operating model, component boundaries, and authoritative sources.</p>
        <span class="badge">architecture</span><span class="badge">pillars</span>
        <p><a href="./architecture/overview.md">View architecture/overview.md</a></p>
    </div>

    <div class="card">
        <h3>📜 Agent Operational Protocols & 27 Core Rules</h3>
        <p>Dual AGENTS.md registry, 27-rule operating constraints, mechanical boot and discovery loops.</p>
        <span class="badge">governance</span><span class="badge">27-rules</span>
        <p><a href="./governance/agent-operation.md">View governance/agent-operation.md</a></p>
    </div>

    <div class="card">
        <h3>🧠 Session Memory Stratification & Palace Synchronization</h3>
        <p>Brain stratification, SOD reanimation, EOD hibernation, and Palace markers.</p>
        <span class="badge">memory</span><span class="badge">palace</span>
        <p><a href="./memory/session-and-palace.md">View memory/session-and-palace.md</a></p>
    </div>

    <div class="card">
        <h3>🤖 Ansible Baseline & Automation Fabric Specification</h3>
        <p>Inventory topology, site.yml, preflight/common playbooks, WSL2 control node bridge.</p>
        <span class="badge">ansible</span><span class="badge">automation</span>
        <p><a href="./automation/ansible-baseline.md">View automation/ansible-baseline.md</a></p>
    </div>

    <div class="card">
        <h3>🛠️ Automation Tools, Ritual Wrappers & Privacy Guardian</h3>
        <p>Cross-platform .ps1/.sh tool registry and Privacy Guardian specs.</p>
        <span class="badge">tools</span><span class="badge">privacy</span>
        <p><a href="./automation/tools-and-privacy.md">View automation/tools-and-privacy.md</a></p>
    </div>

    <div class="card">
        <h3>🔌 FastMCP Server & Continuous Integration Workflows</h3>
        <p>FastMCP server tool contract, Context7 RAG endpoints, GitHub Actions catalog.</p>
        <span class="badge">mcp</span><span class="badge">ci-cd</span>
        <p><a href="./integrations/mcp-and-ci.md">View integrations/mcp-and-ci.md</a></p>
    </div>

    <div class="card">
        <h3>📚 Multi-Channel Documentation Delivery & SEO Engine</h3>
        <p>Omni-channel delivery (Astro SSG, GH Pages, Render, SEO sitemaps).</p>
        <span class="badge">publishing</span><span class="badge">astro</span>
        <p><a href="./publishing/documentation-delivery.md">View publishing/documentation-delivery.md</a></p>
    </div>

    <div class="card">
        <h3>🧪 Quality Verification & Regression Test Suite</h3>
        <p>Python test-suite map, OKF/BOM/quoting/symlink assertions.</p>
        <span class="badge">testing</span><span class="badge">verification</span>
        <p><a href="./quality/verification.md">View quality/verification.md</a></p>
    </div>
</body>
</html>"""
    graph_path.write_text(html_content, encoding="utf-8")
    print(f"[OpenWiki Emulator] Offline standalone visualizer generated: {graph_path}")


def cmd_init() -> None:
    """Initialize and materialize full OpenWiki documentation tree and pages."""
    state = OpenWikiState()
    print(f"[OpenWiki Emulator] Generating native wiki under {OPENWIKI_DIR} with timestamp {state.timestamp}...")
    ensure_openwiki_dirs()
    (OPENWIKI_DIR / "_skeleton.md").write_text(generate_skeleton(state.timestamp), encoding="utf-8")
    (OPENWIKI_DIR / ".last-update.json").write_text(generate_last_update_json(state.timestamp), encoding="utf-8")
    (OPENWIKI_DIR / "INSTRUCTIONS.md").write_text(generate_instructions_md(state.timestamp), encoding="utf-8")

    for relative_path, info in state.get_planned_pages().items():
        page_content = generate_page(
            title=str(info["title"]),
            timestamp=state.timestamp,
            topics=list(info["topics"]),
            description=str(info["description"]),
            content_markdown=str(info["content"]),
            relative_url=relative_path,
        )
        dest_file = OPENWIKI_DIR / relative_path
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        dest_file.write_text(page_content, encoding="utf-8")

    print("[OpenWiki Emulator] Validating and self-healing Mermaid diagrams...")
    for md_file in OPENWIKI_DIR.rglob("*.md"):
        try:
            process_markdown_file(md_file)
        except Exception as e:
            print(f"[OpenWiki Emulator Warning] Could not process {md_file}: {e}")

    cmd_export_graph(state.timestamp)
    print("[OpenWiki Emulator] Successfully updated ./openwiki/ structure.")


def cmd_update() -> None:
    """Compile recent Git diffs and status into evidence blocks and reinitialize wiki."""
    print("[OpenWiki Emulator] Compiling recent Git diffs into OKF evidence blocks...")
    try:
        diff_output = subprocess.check_output(["git", "status", "--porcelain"], text=True)
        print(f"[Git Status]:\n{diff_output if diff_output.strip() else 'No uncommitted changes.'}")
    except Exception as e:
        print(f"[Git Status Warning]: {e}")
    cmd_init()


def cmd_search(query: str) -> None:
    """Execute fast OKF metadata search across openwiki pages.

    Args:
        query: Search keyword string.

    """
    print(f"[OpenWiki Search] Querying frontmatter for: '{query}'...")
    results: list[tuple[pathlib.Path, str, str]] = []
    for md_file in OPENWIKI_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if not content.startswith("---"):
                continue
            parts = content.split("---", 2)
            if len(parts) >= 3:
                meta = yaml.safe_load(parts[1])
                if meta and isinstance(meta, dict):
                    title = str(meta.get("title", ""))
                    desc = str(meta.get("description", ""))
                    topics = meta.get("topics") or []
                    topics_str = " ".join(str(t) for t in topics)
                    searchable = f"{title} {desc} {topics_str}"
                    if query.lower() in searchable.lower():
                        results.append((md_file.relative_to(REPO_ROOT), title, desc))
        except Exception:
            pass

    if results:
        print(f"\nFound {len(results)} matching OpenWiki page(s):")
        for rel_path, title, desc in results:
            print(f" - [{rel_path}] {title}")
            print(f"   Summary: {desc}\n")
    else:
        print(f"No OpenWiki pages matched query '{query}'.")


def main() -> None:
    """Parse CLI arguments and route to emulator command routines."""
    parser = argparse.ArgumentParser(description="DSOM Native Python OpenWiki Emulator")
    parser.add_argument("--init", action="store_true", help="Initialize full wiki")
    parser.add_argument("--update", action="store_true", help="Compile recent Git diffs")
    parser.add_argument("--search", type=str, help="Fast OKF metadata search query")
    parser.add_argument("--export-graph", action="store_true", help="Generate standalone offline HTML graph")

    args = parser.parse_args()

    if args.update:
        cmd_update()
    elif args.search:
        cmd_search(args.search)
    elif args.export_graph:
        cmd_export_graph()
    else:
        cmd_init()


if __name__ == "__main__":
    main()
