---
okf_version: 0.1
type: documentation
title: "CMSForNerd2 Master Onboarding Map"
timestamp: "2026-07-30T12:00:00Z"
description: "Master entry-point and mapping directory for developers and AI agents onboarding onto CMSForNerd2."
topics: [onboarding, navigation, structure, dsom]
---

# 🗺️ CMSForNerd2: Master Onboarding Map

Welcome to the **CMSForNerd2** static workspace. This document serves as the spatial registry and onboarding guide for human architects and AI agents (such as Google Jules).

---

## 🧭 Navigational Layer Directory

To prevent orphaned assets and guarantee immediate discovery across all platforms, the workspace is partitioned into several key layers:

| Target Layer | Purpose | File/Directory Path |
| :--- | :--- | :--- |
| **Project Entrance** | Root introduction and development quickstart. | [README.md](README.md) |
| **Migration Protocol** | Comprehensive architectural blueprint and SSG comparison. | [docs/migration-guide.md](docs/migration-guide.md) |
| **GitBook Summary** | Linear table of contents for documentation pipelines. | [SUMMARY.md](SUMMARY.md) |
| **AI Crawler Sitemap** | High-density context document optimized for LLMs. | [llms.txt](llms.txt) |
| **Agent Rulebook** | Digital Sovereignty Operational Model (DSOM) constitution. | [AGENTS.md](AGENTS.md) / [.agents/AGENTS.md](.agents/AGENTS.md) |

---

## 🏛️ Spatial Organization

By keeping the repository root immaculately clean, we preserve architectural purity.

```
CMSForNerd2/
├── .agents/                    # Sovereign AI Agent spatial memory
│   ├── AGENTS.md               # Full DSOM rulebook constitution
│   └── brain/                  # Cognitive state (tasks, active context)
├── docs/                       # Project documentation
│   └── migration-guide.md      # The master PHP-to-Static migration guide
├── README.md                   # Project landing page
├── START-HERE.md               # This onboarding map
├── SUMMARY.md                  # Compilation registry
└── llms.txt                    # LLM-specific crawler sitemap
```

---

## 🧠 Running in DSOM Mode

With this framework active, both human operators and AI agents operate under the **Deep State of Mind (DSOM)** protocols:

1.  **Read Rulebook first**: Before executing any code logic, read `.agents/AGENTS.md` and `AGENTS.md`.
2.  **Maintain OKF Frontmatter**: All newly created markdown documents MUST carry OKF v0.1 YAML frontmatter headers.
3.  **Strict UK English**: All documentation, comments, and commit messages must strictly conform to UK English standards (e.g., *colour*, *customise*, *optimisation*).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
