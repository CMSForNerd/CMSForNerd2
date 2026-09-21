---
spec_version: "0.2"
type: "documentation"
title: "Deep State of Mind (DSOM) Agentic Workflow Blueprint and Token Compaction Engine"
description: "Comprehensive operational blueprint detailing the 5-step continuous agentic loop, input compaction rules, JSON schema formulation, episodic ledger logging, and automated Git hook manifest synchronization."
topics: ["dsom", "workflow-blueprint", "token-compaction", "git-hook", "metacognition", "episodic-ledger"]
status: "stable"
stale_after: "2027-03-06"
sources:
- id: dsom_protocol_spec
  title: Deep State of Mind Protocol Specification
  url: .agents/brain/knowledge.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["dsom", "workflow-blueprint", "token-compaction", "git-hook", "metacognition", "episodic-ledger"]
---

# Deep State of Mind (DSOM) Agentic Workflow Blueprint

The **DSOM Agentic Workflow Blueprint** defines a continuous operational loop that bridges session execution, token efficiency compaction, and episodic memory persistence into a Git-native framework.

---

## The 5-Step Operational Architecture

```
 ┌────────────────────────────────────────────────────────┐
 │ 1. Session Init & State Sync (Load Git Hook state file)│
 └───────────────────────────┬────────────────────────────┘
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 2. Input Compaction (Apply DSOM token reduction rules) │
 └───────────────────────────┬────────────────────────────┘
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 3. Execution & Autonomous Evaluation (Tasks / Tests)   │
 └───────────────────────────┬────────────────────────────┘
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 4. Episodic Ledger Backup (Commit session changes)     │
 └───────────────────────────┬────────────────────────────┘
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 5. State File Update (Automated Git Hook / CI Action)  │
 └───────────────────────────┘
```

---

## Step-by-Step Workflow Implementation

### 1. Session Initialization & State Sync
Before the AI processes incoming instructions, it establishes active context boundaries:
* **Action:** Reads the current spatial memory state manifest (`.agents/brain/active_context_manifest.md`).
* **Context Injection:** Injects ongoing priorities, active file paths, and governance boundaries into the system prompt.

### 2. Input Compaction (Token Efficiency Engine)
To prevent context bloat and optimize prompt efficiency:
* **Action:** Raw user instructions, error logs, or environment outputs are passed through `tools/dsom_compaction_engine.py`.
* **Mechanism:** Strips conversational redundancies, compresses telemetry into key-value pairs, and formats the active delta into a structured JSON schema.

### 3. Execution & Autonomous Evaluation
The core task is processed through defined architecture boundaries:
* **Governance Gate:** Deterministic checks auto-execute. System-level alterations require explicit human approval or dual-pathway branching.

### 4. Episodic Ledger Backup
Session changes are preserved cleanly:
* **Action:** Appends structured session deltas, test outcomes, and state mutations to `.agents/brain/checkpoint_summary.txt`.

### 5. State File Update via Git Hooks
Bridging session memory back into the repository:
* **Action:** `tools/dsom-manifest-sync.sh` captures git status, executes compaction, and updates `.agents/brain/active_context_manifest.md` on commit.

---

## DSOM Core Compaction Engine System Prompt (Step 2)

```
# SYSTEM PROMPT: DSOM CORE COMPACTION ENGINE

## ROLE AND PURPOSE
You are the token efficiency and state-optimisation processor for the Deep State of Mind (DSOM) agentic protocol. Your primary objective is to execute Metacognitive Governance and Context Compaction. You strip incoming noise, extract critical operational changes, and consolidate raw payload data into a compressed state manifest without losing semantic or structural intent.

## OPERATIONAL MANDATES
1. Zero Redundancy: Eliminate conversational filler, repeated syntax structures, conversational pleasantries, and metadata overhead.
2. Lossless Technical Retention: Never compress away explicit variables, system state files, error logs, configuration parameters, specific file paths, Git commit hashes, or operational boundaries.
3. Density Maximisation: Compress prose into concise, high-density conceptual key-value pairs or concise Markdown fragments.

## COMPACTION PROTOCOLS
1. Text & Code Optimisation: Condense variable definitions and structural patterns into inline blocks where possible. Convert conversational history logs into atomic historical event strings formatted as: `[Timestamp] Event | Key Delta`.
2. Log & Incident Telemetry Compression: Filter repetitive telemetry loops. Extract only unique rule IDs, source IPs, target assets, triggered exceptions, and anomalous vectors. Condense standard execution paths into basic lifecycle hooks (e.g., INIT -> PROCESS -> SUCCESS).
3. State Extraction: Identify explicit user intents, updated code constraints, project directives, and active operational files. Synthesise the execution goal into a singular high-level priority variable.

## OUTPUT FORMULATION
You must output a strictly structured, compacted state payload enclosed inside a single ```json code block matching this schema:

{
  "dsom_compaction_meta": {
    "protocol_version": "0.2",
    "timestamp": "ISO_8601_TIMESTAMP"
  },
  "active_intent": "Singular primary goal or explicit instruction to be executed",
  "operational_constraints": [
    "Strict technical dependencies",
    "Environment specifics",
    "Human-in-the-loop gates required"
  ],
  "context_deltas": {
    "system_mutations": "Summary of active files changed, configuration values injected, or repo state steps",
    "telemetry_vectors": "Compressed system exceptions, alert parameters, or technical logs"
  },
  "episodic_memory_keys": [
    "Atomic reference point 1",
    "Atomic reference point 2"
  ]
}
```

---

## Tooling Utilities

* **Compaction CLI:** `python3 tools/dsom_compaction_engine.py --intent "Task description" --files "file1.py,file2.md"`
* **Git Manifest Sync Hook:** `./tools/dsom-manifest-sync.sh`

---

*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
