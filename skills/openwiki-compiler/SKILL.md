---
type: "skill"
title: "OpenWiki Knowledge Graph Compiler Skill"
name: "openwiki-compiler"
description: "Procedural SOP for executing the native Python OpenWiki Emulator to compile, update, and maintain codebase knowledge graphs within DSOM without Node.js binaries."
topics: ["openwiki", "knowledge-graph", "emulator", "dsom", "qmd"]
status: "stable"
spec_version: "0.2"
stale_after: "2027-03-06"
sources:
- id: dsom_agents_rulebook
  title: The Core AI Rulebook (DSOM)
  path: .agents/AGENTS.md
- id: workspace_file
  title: SKILL.md
  url: skills/openwiki-compiler/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-10-04T21:12:00Z'
tags: ["openwiki", "knowledge-graph", "emulator", "dsom", "qmd"]
---

# OpenWiki Knowledge Graph Compiler Skill

Procedural SOP for executing the native Python OpenWiki Emulator to compile, update, and maintain codebase knowledge graphs within DSOM without Node.js dependencies.

## Purpose

To guide AI Agents (Google Jules, Antigravity, Claude, Cursor) in maintaining and compiling OpenWiki-compliant knowledge graphs over the Sovereign Markdown Palace (`docs/`) and `.agents/brain/` using the native Python emulator (`tools/openwiki_emulator.py`) and optional QMD / FastMCP local search helpers.

---

## Operational Workflow for AI Agents

### 1. Execution Protocol (Zero External Node.js Binaries)

AI agents maintain `./openwiki/` using the Native Python OpenWiki Emulator (Rule 16 `uv` Mandate & Rule 27 Native OpenWiki Emulator Mandate):

```bash
# Execute native OpenWiki Emulator via uv
uv run --with pyyaml python tools/openwiki_emulator.py --init
```

---

### 2. Standard Maintenance Procedures

#### A. Initializing or Updating Knowledge Graph
Run when initializing a new project or updating an existing wiki:
```bash
uv run --with pyyaml python tools/openwiki_emulator.py --init
```

#### B. Incremental State Update (EOD Ritual)
Execute during EOD consolidation to compile session diffs into `./openwiki/`:
```bash
uv run --with pyyaml python tools/openwiki_emulator.py --update
```

#### C. Fast OKF Metadata Search
Perform sub-millisecond search across openwiki frontmatter titles, topics, and descriptions:
```bash
uv run --with pyyaml python tools/openwiki_emulator.py --search "ansible"
```

#### D. Standalone Offline Visualizer Export
Generate standalone `graph.html` interactive visualizer:
```bash
uv run --with pyyaml python tools/openwiki_emulator.py --export-graph
```

---

### 3. QMD (Query Markup Documents) Helper Workflow

In addition to fast frontmatter search, agents can integrate QMD (on-device local search engine combining BM25, vector search, and LLM re-ranking) for deep concept retrieval:

1. **Local QMD Indexing:**
   ```bash
   qmd index ./openwiki ./docs
   ```
2. **QMD Querying:**
   ```bash
   qmd query "ansible inventory topology"
   ```
3. **FastMCP Integration:**
   Use FastMCP tools `get_openwiki_concept` and `search_ssg_routes` directly via `tools/mcp/server.py`.

---

### 4. AI Fallback Synthesis Protocol & OKF Compliance

When drafting or updating `./openwiki/` documentation:
1. **Skeleton Analysis:** Read `./openwiki/_skeleton.md` to inspect planned page tree, subsystem rankings, and evidence links.
2. **OKF v0.2 Frontmatter Compliance:** Ensure all Markdown pages maintain valid OKF v0.2 YAML frontmatter headers (`type`, `title`, `description`, `topics`, `spec_version`, `status`, `sources`, `generated`).
3. **Mermaid Validation & Self-Healing:** The emulator automatically validates Mermaid blocks and applies in-place degradation (`%% openwiki-error:`) or self-healing recovery.

---

## Quality Gates & Security Rules

1. **Rule 16 (`uv` Mandate):** All Python dependencies and tools must be run via `uv run`.
2. **Rule 24 (Credential Protection):** Never commit API keys or secret tokens into local files or wiki content.
3. **Rule 27 (Native OpenWiki Emulator Mandate):** Maintain `./openwiki/` directly via `tools/openwiki_emulator.py`, completely eliminating external Node.js binaries and API rate limit dependencies.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) & Jules | 2026-10-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
