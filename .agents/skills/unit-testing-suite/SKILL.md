---
okf_version: "0.1"
type: "skill"
title: "Unit and Integration Testing Suite Skill"
name: "unit-testing-suite"
description: "Governs unit testing across Pytest modules, Ansible compliance, Podman containerization, OKF frontmatter validation, and Playwright E2E suites."
timestamp: "2026-09-05T08:00:00Z"
topics: ["testing", "unit-tests", "pytest", "ansible", "podman", "playwright"]
status: "stable"
sources:
  - id: "dsom_agents_rulebook"
    title: "The Core AI Rulebook (DSOM)"
    path: ".agents/AGENTS.md"
---

# Unit and Integration Testing Suite Skill

This skill governs unit, modular, integration, and E2E browser testing routines across the CMSForNerd2 repository.

## Operational Standards

1. **Pytest Modular Architecture**:
   - Tests reside in domain submodules inside `tests/unit/` (`ansible.py`, `containers.py`, `markdown.py`, `sitemaps.py`, `llms.py`).
   - `tests/test_unit.py` re-exports domain test cases for Pytest discovery and execution.

2. **Subsystem Test Coverage**:
   - **Ansible**: Validates `deploy-static.yml` playbook syntax, FQCN module actions, `changed_when` parameters, and dual-pathway branching logic.
   - **Containers**: Validates `Dockerfile` and `Containerfile` multi-stage build instructions and `node:22-alpine` builder setup.
   - **Markdown & OKF**: Validates OKF v0.1 schema compliance and OKF v0.2 machine-readable trust signals (`sources`, `verified`, `status`).
   - **Sitemaps & Assets**: Validates plain-text and XML sitemap endpoints against physical built assets in `dist/`.

3. **Execution Command**:
   ```bash
   uv run --with pytest --with pyyaml --with requests python -m pytest
   ```

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-05*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
