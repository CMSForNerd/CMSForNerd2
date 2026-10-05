---
type: "skill"
title: "Ansible Playbook Test Runner Skill"
name: "playbook-test-runner"
description: "Self-healing Agent Skill for static linting, FQCN verification, two-pass idempotence assertions, and syntax-checking across Ansible playbooks."
topics: ["ansible", "playbook", "ansible-lint", "syntax-check", "agent-skill"]
status: "stable"
sources:
- id: workspace_file
  title: SKILL.md
  url: skills/playbook-test-runner/SKILL.md
spec_version: "0.2"
stale_after: "2027-03-06"
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-10-05T14:45:00Z'
tags: ["ansible", "playbook", "ansible-lint", "syntax-check", "agent-skill"]
---

# Ansible Playbook Test Runner Skill

This skill provides automated linting and syntax verification for all Ansible playbooks within the repository, conforming strictly to Rule 32.43 (Playbook Validation Ladder) and Rule 32.44 (Ansible CoP Standard).

## Key Capabilities

1. **Syntax Checking**: Runs `ansible-playbook --syntax-check` across all playbooks in `playbooks/`.
2. **Production Linting**: Invokes `ansible-lint playbooks/` with zero failures or fatal violations.
3. **Execution Command**:

   ```bash
   ./skills/playbook-test-runner/run.sh
   ```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-10-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
