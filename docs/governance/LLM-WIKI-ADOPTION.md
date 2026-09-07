---
type: "governance"
title: "DSOM vs. LLM WIKI: Comparative Analysis & Adoption Strategy"
description: "Sovereign knowledge adoption strategy integrating Andrej Karpathy LLM WIKI Ingest Query and Lint protocols with DSOM Protocol."
topics:
- llm-wiki
- dsom-protocol
- knowledge-governance
- spatial-memory
nav_order: 1
spec_version: "0.2"
status: "stable"
stale_after: "2027-03-06"
sources:
- id: "workspace_file"
  title: LLM-WIKI-ADOPTION.md
  url: docs/governance/LLM-WIKI-ADOPTION.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  timestamp: '2026-09-06T15:00:00Z'
tags:
- llm-wiki
- dsom-protocol
- knowledge-governance
- spatial-memory
---

# 🧠 DSOM vs. LLM WIKI: Comparative Analysis & Adoption Strategy

Entry Point 8: This document serves as the Sovereign Knowledge Entry Point. See [START-HERE.md](../../START-HERE.md) for the master onboarding roadmap.

In honour of Andrej Karpathy's "LLM WIKI" vision, which inspired the formalisation of the Ingest, Query, and Lint protocols within the Deep State of Mind (DSOM) framework.

Andrej Karpathy's "LLM WIKI" paradigm shift moves from standard Retrieval-Augmented Generation (RAG) to a persistent, LLM-maintained knowledge base. Instead of parsing raw documents on every query, the LLM continuously reads, synthesises, and cross-references information into a structured Markdown wiki. The human is the curator and the LLM is the tireless maintainer.

Our Deep State of Mind (DSOM) framework implements this vision. This document breaks down the parallels, lists current implementations, and defines how Karpathy's concepts elevate our intelligence architecture.

---

## 1. What We Already Do (The DSOM Baseline)

Karpathy defines three architectural layers and several core operations. Here is how our existing DSOM protocols map to his concepts:

| LLM WIKI Concept | DSOM Implementation | Status |
| :--- | :--- | :--- |
| **The Schema** (Instructions on how the LLM maintains the wiki) | `AGENTS.md` (Sovereign Constitution) and `SKILL.md` files setting behavioural guardrails. | Implemented (Highly Mature) |
| **The Wiki** (LLM-maintained Markdown files) | Sovereign Markdown Palace (`docs/governance/`, `docs/explanation/`, etc.). | Implemented |
| **`index.md`** (Content catalog for navigation) | `palace_registry.md` and `SUMMARY.md` (spatial memory map). | Implemented |
| **`log.md`** (Chronological tracking) | `HISTORY.md` (Universal Ledger) and `CHANGELOG.md`. | Implemented |
| **Chronological State Logging** | `checkpoint_summary.txt`, `task.md`, and `walkthrough.md`. | Implemented |

DSOM provides an advanced, production-grade implementation of the LLM WIKI concept, specifically tuned for software engineering and DevOps infrastructure.

---

## 2. How LLM WIKI Can Make Us Better (The Gaps)

While we have the structure, the LLM WIKI highlights three operational verbs to make the DSOM Palace self-sustaining and compounding: **Ingest**, **Query**, and **Lint**.

### A. The "Ingest" Protocol (Automated Synthesis)

* **The Concept**: When a new raw source (e.g., an article, a specification, a transcript) is introduced, the AI extracts data, synthesises it, creates concept pages, and links it into the Wiki.
* **Our Adoption**: We maintain a strict separation between raw sources and the synthesised Palace via the `dsom-knowledge-ingester` skill to extract text, synthesise Markdown pages in the Palace, and update `palace_registry.md` and `SUMMARY.md`.

### B. The "Lint" Ritual (Automated Health Checks)

* **The Concept**: The AI periodically health-checks the Wiki for contradictions, orphan pages, and stale claims.
* **Our Adoption**: As the Sovereign Markdown Palace grows, context can rot. The `tools/refactor-okf.cjs` and `tools/verify-sitemaps.js` scripts, alongside the `docs-review` skill, crawl `docs/` and `.agents/` to detect broken links, conflicting rules, and orphan pages.

### C. The "Query" Loop (Compounding Answers)

* **The Concept**: When the LLM generates a high-value answer, comparison, or analysis, it is filed back into the Wiki rather than disappearing into chat history.
* **Our Adoption**: Establish the behavioural mandate: *"Any time a complex architectural analysis or troubleshooting guide is generated in session, the AI must proactively propose saving it as a persistent `.md` document in the Palace."*

---

## 3. Proposed Next Steps for Adoption

1. **Maintain Knowledge Compounding in `AGENTS.md`**: Persist valuable session analyses directly into `docs/` or `.agents/brain/`.
2. **Automate OKF & Sitemap Health Audits**: Execute `tools/refactor-okf.cjs` and `tools/verify-sitemaps.js` during pre-commit workflows.
3. **Keep `palace_registry.md` and `active_context_manifest.md` Synchronised**: Externalise cognitive state at the end of every engineering session.

---

*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) & Jules*
