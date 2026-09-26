---
spec_version: "0.2"
type: "skill"
title: "DSOM Infrastructure Playbook Authoring & Automated Idempotency Gate Skill"
name: "dsom-infrastructure-playbook-documenter"
description: "Governs Ansible playbook and role authoring, refactoring, and automated review within DSOM, enforcing Rule 32.43 (5-Tier Validation Ladder & Two-Pass Idempotency Assertion) and Rule 32.44 (Zen of Ansible & Red Hat CoP 14-Point Standards)."
topics: ["ansible", "playbook", "idempotency", "ai-forge", "redhat-cop", "validation-ladder", "devops"]
status: "stable"
author: "Repository Architect & OKF v0.2 Compliance Agent"
version: "1.0.0"
stale_after: "2027-03-06"
sources:
- id: kodekloud_ai_ansible
  title: Building an AI Agent That Writes and Validates Ansible Playbooks
  url: https://kodekloud.com/blog/building-an-ai-agent-that-writes-and-validates-ansible-playbooks/
- id: ansible_community_ai_forge
  title: Ansible Community AI Forge Repository
  url: https://github.com/ansible-community/ai-forge/
- id: redhat_cop_good_practices
  title: Red Hat CoP Automation Good Practices
  url: https://redhat-cop.github.io/automation-good-practices/
- id: lola_dev
  title: Lola AI Context Engine
  url: https://getlola.dev/
generated:
  by: Repository Architect & OKF v0.2 Compliance Agent
  at: '2026-09-26T00:00:00Z'
tags: ["ansible", "playbook", "idempotency", "ai-forge", "redhat-cop", "validation-ladder", "devops"]
---

# DSOM Infrastructure Playbook Authoring & Automated Idempotency Gate Skill

The `dsom-infrastructure-playbook-documenter` skill establishes a machine-verifiable standard for writing, refactoring, validating, and reviewing Ansible playbooks, roles, and tasks across carrier, enterprise, and air-gapped environments.

It enforces two foundational DSOM governance rules:
1. **Rule 32.43:** Automated Ansible Playbook Validation Ladder & Idempotence Assertion Standard.
2. **Rule 32.44:** Ansible Community AI-Forge & Red Hat CoP Automation Good Practices Standard.

---

## 1. The 5-Tier Ascending Cost Validation Ladder (Rule 32.43)

Whenever the AI agent generates or modifies Ansible playbooks, it must execute code through the 5-Tier Validation Ladder in ascending order of execution cost:

```
+-----------------------------------------------------------------------+
| Tier 1: Static YAML Check                                             |
|   Fast syntax & structural parse (YAML formatting, 2-space indent)   |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| Tier 2: Ansible Syntax Verification                                    |
|   ansible-playbook <playbook.yml> --syntax-check                      |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| Tier 3: Production Profile Static Lint                                |
|   ansible-lint --profile production                                   |
|   Enforces FQCN (ansible.builtin.*), no bare shell, no secrets.       |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| Tier 4: Check Mode / Dry-Run Verification                             |
|   ansible-playbook --check --diff -i <inventory> <playbook.yml>       |
|   Surfaces missing variables, structural drift, & template bugs.       |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| Tier 5: Two-Pass Execution & Idempotence Assertion                    |
|   Pass 1 (Converge): Execute playbook to bring state to desired target |
|   Pass 2 (Assert): Re-run playbook; MUST yield changed=0, failed=0     |
+-----------------------------------------------------------------------+
```

### Machine-Checkable Idempotence Assertion
Idempotency is an objective, deterministic requirement:
- **Pass 1:** Converges node state.
- **Pass 2:** Asserts zero changes (`changed=0, failed=0`). If `changed > 0` on Pass 2, the playbook contains a procedural regression that MUST be corrected before production promotion.

---

## 2. Deterministic Fast-Fail Pre-Execution Code Gates

Before proposing or applying any Ansible task, the AI agent must enforce the following pre-execution code gates:

1. **FQCN Mandatory:** All module calls MUST use Fully Qualified Collection Names (e.g., `ansible.builtin.copy`, `ansible.builtin.command`, `community.general.ini_file`).
2. **Idempotency Guard Mandatory for Shell/Command:** Bare `shell`, `command`, or `raw` tasks are prohibited unless accompanied by explicit idempotency guards (`changed_when`, `creates`, or `removes`).
3. **Secret Protection:** Plaintext passwords, tokens, or private keys in playbooks/vars are strictly banned. Tasks handling vaulted secrets or credentials must explicitly declare `no_log: true`.
4. **Non-Privileged Execution Boundary:** Playbook generation output must always be presented as a reviewable Git change / Pull Request against staging playbooks, NEVER applied directly to production carrier inventories without prior operator review.

---

## 3. The Zen of Ansible Philosophical Review Gate (Rule 32.44)

Playbooks are declarative state specifications, NOT procedural programs. The AI agent must enforce the following core tenets:

- **Ansible is not Python:** Eliminate complex Jinja2 inline loops, nested Python methods, or excessive string manipulation inside templates or task definitions.
- **Playbooks are not for programming:** Avoid deep YAML nesting, multi-level `when` conditional logic, or procedural control flow.
- **Clear over Cluttered & Simple over Complex:** Prefer clean, purpose-built declarative modules over monolithic shell commands.
- **Convention over Configuration:** Rely on sensible defaults rather than endless tuneable variables.

---

## 4. Red Hat CoP 14-Point Authoring & Style Rules

When authoring or refactoring playbooks, roles, or task files, the AI agent must strictly follow the Red Hat Communities of Practice (CoP) 14-point authoring rules:

| # | Rule Category | Specification |
|---|---|---|
| 1 | **YAML Indentation** | 2-space indentation throughout all `.yml` files. |
| 2 | **File Extension** | Always use `.yml` (never `.yaml`). |
| 3 | **Module Arguments** | Structured YAML dictionary mapping format (never inline `key=value` strings). |
| 4 | **Booleans** | Explicit lowercase `true` and `false`. |
| 5 | **Module Naming** | Fully Qualified Collection Names (`ansible.builtin.*`). |
| 6 | **Task Naming** | Imperative, capitalized, descriptive names (e.g., `Ensure Nginx service is enabled`). |
| 7 | **Module State** | Explicit `state:` parameter on every module supporting it (`present`, `absent`, `started`, `restarted`). |
| 8 | **Loop Construct** | Modern `loop:` keyword (never legacy `with_*` statements). |
| 9 | **Error Handling** | Specific `failed_when:` conditions rather than blanket `ignore_errors: true`. |
| 10 | **Variable Prefixing** | External role variables prefixed with `<role_name>_...`; internal constants prefixed with `__<role_name>_...`. |
| 11 | **Jinja2 Templates** | Mandatory `{{ ansible_managed \| comment }}` header at top of all configuration templates. |
| 12 | **Naming Conventions** | `snake_case` for all filenames, variable names, and role identifiers. |
| 13 | **Fact Notation** | Modern bracket fact notation (`ansible_facts['distribution']`) instead of bare legacy variables. |
| 14 | **Git Commits** | Conventional Commits with FQCN scope (e.g., `feat(ansible.builtin.dnf): configure package repos`). |

---

## 5. 14-Category Playbook Review Checklist & Rubric

When performing automated code reviews or sanity audits on Ansible playbooks, evaluate code across 14 categories with a compliance score (1–10):

1. **YAML Style & Format:** 2-space indent, `.yml` extension, no trailing whitespace.
2. **Naming Standards:** Imperative task names, `snake_case` variables, prefixed role vars.
3. **Module Selection & Usage:** FQCN, declarative modules preferred over shell/command.
4. **Task Structure:** Logical grouping, blocks for error handling, explicit states.
5. **Handlers:** Idempotent, notified on state changes, clear handler names.
6. **Jinja2 Templates:** `ansible_managed` header, readable logic, no complex embedded Python.
7. **Variable Scoping:** Clear separation of defaults, vars, and vault secrets.
8. **Playbook Layout:** Clean play definitions, inventory host targets, tags.
9. **Inventory Design:** Host groups, child groups, clear host variables.
10. **Error Handling & Failure Recovery:** `block`/`rescue`/`always`, explicit `failed_when`.
11. **Idempotency:** `changed_when` guards, `creates`/`removes` parameters, zero second-pass mutations.
12. **Argument Specs:** `meta/argument_specs.yml` defined for all roles.
13. **Tagging:** Consistent tag strategy (`--tags opentofu`, `--tags config`).
14. **Platform Support:** Dual-pathway sandbox/real-OS detection (`is_limited_environment`).

---

## 6. Lola AI Package Manager Usage Analysis & Integration Boundary

### Identified Need & Assessment (`https://getlola.dev/`)
**Question:** *Can Lola (`lola-ai`) be used in this project?*

**Decision & Integration Boundary:**
1. **Optional Local Helper CLI:** Lola can be used as an optional local helper CLI or declarative module spec via `.lola-req` and `playbooks/install.yml` (which executes `lola sync` when `lola` is present on a control node).
2. **No SaaS / Hard External Dependencies for AI Agents:** DSOM does NOT depend on external Lola SaaS package registries or runtime wrappers for core AI agent execution. All AI agent skills (including Ansible AI Forge skills) are natively stored, versioned, and managed locally under `.agents/skills/`.
3. **Air-Gapped Sovereignty:** Storing native skills in `.agents/skills/` ensures 100% operational sovereignty and air-gapped readiness across enterprise and telecommunication bastions where external SaaS endpoints are restricted.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-26*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
