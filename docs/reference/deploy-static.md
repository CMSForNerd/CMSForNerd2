---
okf_version: 0.1
type: "documentation"
title: "deploy-static.sh CLI Reference"
description: "Technical specifications, environment variable overrides, and dual-pathway branching logic for the static deployment orchestrator."
timestamp: "2026-08-01T14:50:00Z"
topics: ["reference", "bash", "ansible", "deployment"]

nav_order: 1
---

# 🏗️ `deploy-static.sh` CLI Reference

The `deploy-static.sh` script is a POSIX-compliant Bash orchestrator that automates static site builds and staging server deployments using dual-pathway environment branching.

---

## ⚙️ Technical Specifications

- **File Path**: `tools/deploy-static.sh`
- **Language**: POSIX-compliant Bash (tested with Bash 4.0+)
- **Dependencies**:
  - Node.js & npm (for workspace builds)
  - Ansible & `ansible-playbook` (optional, required only on Real OS deployments)

---

## 🛠️ Execution Pathways

The script executes a dynamic environmental check to determine available system privileges:

```
                      [START RUN]
                           │
             Is USER == "jules" or JULES_ENV?
              /                         \
            YES                         NO
            /                             \
    [Limited Sandbox]                  [Real OS]
    - npm install                      - Run full Ansible playbook
    - npm run build                    - Set up Nginx config
    - Bypass systemd/root              - Hardened CSP/Security Headers
```

### 1. Limited Sandbox Pathway (Google Jules)
- **Condition**: Automatically activated if `USER` is `'jules'` or the `JULES_ENV` environment variable is defined.
- **Actions**: Bypasses system-wide configurations, executes local workspace dependencies installations (`npm install`), and compiles the Astro SSG files (`npm run build`).

### 2. Real OS Pathway (Production Server)
- **Condition**: Activated if neither conditions are met.
- **Actions**: Verifies Ansible installation, accesses `inventory/hosts.staging.yml`, and triggers the complete playbook `deploy-static.yml` with system administrative privileges to configure web serving.

---

## 📥 Inputs & 📤 Outputs

- **Environment Variables**:
  - `JULES_ENV` (string, optional): If set, forces the orchestrator into Sandbox Mode.
  - `USER` (string, system): Read by the orchestrator to detect unprivileged runtimes.
- **Exit Codes**:
  - `0`: Successful compilation or deployment.
  - `1`: Missing command-line dependencies (such as `ansible-playbook` in Real OS mode).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
