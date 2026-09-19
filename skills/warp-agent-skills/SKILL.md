---
type: "skill"
title: "Warp Agent Skills Specification"
name: "warp-agent-skills"
description: "Standardised specification for defining, parameterising, discovering, and executing Warp and OpenViking Agent Skills across project (.agents/skills/) and user (~/.agents/skills/) scopes."
topics: ["warp", "openviking", "agent-skills", "slash-commands", "skill-arguments", "okf"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
spec_version: "0.2"
stale_after: "2027-09-17"
sources:
- id: warp_skills_docs
  title: Warp Agent Skills Capability Guide
  url: https://docs.warp.dev/agents/capabilities/skills/
- id: openviking_skills_api
  title: OpenViking Skills API & Specification
  url: https://docs.openviking.ai/en/api/04-skills
- id: workspace_file
  title: SKILL.md
  url: skills/warp-agent-skills/SKILL.md
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-17T00:00:00Z'
tags: ["warp", "openviking", "agent-skills", "slash-commands", "skill-arguments", "okf"]
---

# Warp Agent Skills Specification (`warp-agent-skills`)

The `warp-agent-skills` skill defines the architectural specification for building reusable, parameterised, and shareable instructions that AI agents (Warp Agent, OpenViking, Google Jules, Claude Code) discover and invoke autonomously or via slash commands (`/{skill-name}`).

---

## Skill Directory Structure & Discovery Order

1. **Project-Scoped Skills (Repository Level):**
   - `.agents/skills/{skill-name}/SKILL.md` (recommended)
   - `.warp/skills/{skill-name}/SKILL.md`
   - `.github/skills/{skill-name}/SKILL.md`
   - Discovered automatically when the current working directory is inside the repository.

2. **User-Scoped Skills (Global Machine Level):**
   - `~/.agents/skills/{skill-name}/SKILL.md`
   - `~/.warp/skills/{skill-name}/SKILL.md`

Each skill resides in its dedicated directory containing `SKILL.md` and optional supporting automation scripts, templates, or schema files.

---

## Parameterised Skill Arguments Syntax

Skills support argument placeholders that are substituted dynamically when invoked:

- `$ARGUMENTS`: The full raw argument string passed after the skill command.
- `$ARGUMENTS[N]` or `$N`: The Nth whitespace-separated argument (0-indexed). For example, `$0` represents the first parameter, `$1` the second.

### Parameterised Skill Frontmatter Example

```markdown
---
type: "skill"
title: "Explain Topic Skill"
name: "explain-topic"
description: "Explain a specific technical topic for a given audience in a specified tone."
status: "stable"
spec_version: "0.2"
stale_after: "2027-09-17"
topics: ["explanation", "documentation", "warp-skill"]
---

# Explain Topic

Explain $0 for an audience of $1 professionals using a $2 tone.

Full Request String: $ARGUMENTS
```

Invoking via `/explain-topic WebGPU SRE authoritative` evaluates to:
> "Explain WebGPU for an audience of SRE professionals using a authoritative tone."

---

## OpenViking Skill Storage & Attested MCP Conversion

OpenViking manages skills using canonical URIs (`viking://~/skills/{skill-name}` or `viking://agent/skills/{skill-name}`) and provides automatic conversion of Model Context Protocol (MCP) tool definitions containing `inputSchema` into structured OKF v0.2 `SKILL.md` format.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
