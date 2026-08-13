---
okf_version: 0.1
type: "documentation"
title: "Ansible Deployment How-To Guide"
description: "A comprehensive guide on deploying CMSForNerd2 using the Ansible static orchestration suite with dual-pathway branching logic."
timestamp: "2026-08-01T14:45:00Z"
topics: ["how-to", "ansible", "deployment", "orchestration", "security"]

nav_order: 1
---

# 📋 How to Deploy with Ansible Static Orchestration

This guide explains how to execute the Ansible static orchestration playbook to compile and configure CMSForNerd2 across unprivileged container sandboxes and production server environments.

---

## 🎯 Prerequisite Actions

Before running deployments, verify your Ansible installation:

```bash
ansible --version
```

Verify that `deploy-static.yml` and `inventory/hosts.staging.yml` are present in your workspace.

---

## 🏗️ Step-by-Step Directions

### Step 1: Understand Dual-Pathway Branching Logic
Because systems like Google Jules or local test Docker containers are restricted, system-wide adjustments (such as configuring Nginx, restarting firewalls, or reloading systemd) will fail. To address this, our Ansible orchestration implements **Dual-Pathway Branching**:
- **Limited Sandbox VM Pathway**: Detects if the user is unprivileged (e.g., `jules`), bypasses all administrative actions, and performs local workspace builds (`npm install` and `npm run build`).
- **Real OS Pathway**: Performs standard unprivileged workspace actions and then runs root-level security hardening, Nginx configuration setup, and daemon management.

### Step 2: Run the Deployment Orchestrator
To deploy using the automated orchestrator script, run:

```bash
./tools/deploy-static.sh
```

If run within a limited sandbox (e.g. Google Jules), it outputs:
```text
🔍 Detected Limited Sandbox Environment (Google Jules).
⚠️  Running under limited sandbox constraints.
👉 Bypassing system-wide root tasks.
👉 Focusing on unprivileged workspace build operations only.
📦 [1/2] Installing NPM packages...
🏗️  [2/2] Compiling Astro static site (SSG build)...
✅ Success: Static build complete in limited environment!
```

If executed on a standard system or virtual machine, the script automatically triggers the full Ansible orchestration playbook:

```bash
ansible-playbook deploy-static.yml -i inventory/hosts.staging.yml
```

### Step 3: Run Staging Verification Tests
To verify that the deployed site renders correctly and matches high-performance criteria, run the integration test suite:

```bash
python3 -m pytest tests/test_cms.py
```

Expected output:
```text
tests/test_cms.py ..............................                         [100%]
============================= 30 passed in 6.50s =============================
```

---

## 🔒 Security Hardening Policies

When deploying onto a Real OS, the Ansible orchestration playbook applies the following OWASP-aligned standards:
1.  **Strict Security Headers**: Integrates defensive headers in `/etc/nginx/nginx.conf` (HSTS, CSP whitelists, X-Frame-Options: DENY, and X-Content-Type-Options: nosniff).
2.  **Unprivileged Execution**: Enforces Nginx worker operations to execute purely under the unprivileged `USER nginx` on unprivileged port `8080`.
3.  **Clean URLs Routing**: Formulates clean static pathways (omitting `.html` from browser location paths).

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
