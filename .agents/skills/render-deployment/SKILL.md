---
okf_version: 0.1
type: "skill"
title: "Render Deployment Skill"
name: "render-deployment"
description: "Configures and manages Render.com deployments via Docker containerisation or native Free Static Site pathways."
timestamp: "2026-08-01T12:00:00Z"
topics: ["render", "deployment", "docker", "static-site", "blueprint"]
---

# Render Deployment Skill

This skill governs the blueprint specifications, containerisation steps, and manual configurations required to deploy CMSForNerd2 reliably on Render.com.

## When to use this skill

- When editing the Render deployment blueprint configuration (`render.yaml`).
- When modifying the web server Docker/Container configuration.
- When configuring deployment commands on the Render dashboard.
- When diagnosing or documenting deployment pipelines for Render.com.
- When updating or executing Ansible-based static orchestration playbooks.

## Operational Standards & Procedures

### 1. Render Blueprint Pathways
The repository is configured for deployment to Render.com via a root-level `render.yaml` Blueprint Specification supporting two distinct pathways:
- **Pathway 1 (Containerised Web Service)**: A containerised Web Service using a multi-stage Dockerfile (or `Containerfile`) that packages the Astro site in a hardened, unprivileged Nginx server listening on port 8080 with a `/healthz` health check.
- **Pathway 2 (Native Free Static Site)**: A native free Static Site service (`cmsfornerd2-static`) configured to run `npm run build` and publish the `dist` directory.

### 2. Manual Dashboard Deployment Constraints
To prevent build failures during manual dashboard deployments on Render:
- Set the **Build Command** to `npm run build`.
- Set the **Publish Directory** to `dist`.
- These settings prevent "Publish directory dist/ does not exist!" failures, as fully documented in `README.md` and `docs/migration-guide.md`.

### 3. Ansible Static Orchestration & Dual-Pathway Sandbox Branching
For deployments on staging environments or custom servers, an Ansible orchestration suite is maintained with unprivileged sandbox awareness:
- The Ansible playbook `deploy-static.yml` is 100% compliant with `ansible-lint`. It strictly utilises Fully Qualified Collection Names (FQCN) for all module actions and specifies `changed_when` parameters on commands to maintain idempotency.
- All automation scripts, deployment pipelines, and Ansible playbooks in the repository must explicitly check for limited sandbox environments (such as the Google Jules container, typically by checking for username 'jules', custom environment variables, or virtualisation types) and implement a dual-pathway branching logic.
- Limited sandbox environments must bypass system-level modifications (such as systemd configurations, global packages installations, or firewall rule adjustments) to focus strictly on unprivileged workspace operations (e.g. local dependencies and compilation), whereas real OS environments are permitted to execute full administrative configurations with no limitations.
- An Ansible orchestration suite (`ansible.cfg`, `deploy-static.yml`, `inventory/hosts.staging.yml`, and `tools/deploy-static.sh`) is configured to demonstrate and enforce this rule.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
