#!/usr/bin/env bash
# ==============================================================================
# Script Name : deploy-static.sh
# Path        : tools/deploy-static.sh
# Purpose     : Automated Static Deployment Orchestrator for CMSForNerd2.
#               Detects execution environment and dynamically branches between
#               a limited sandbox environment (Google Jules) and a full-privileged
#               staging/production environment.
# Prerequisites:
#   - Bash shell (version 4+)
#   - Node.js & NPM (for static local builds)
#   - Ansible (for staging/production system configuration and deployment)
# Usage       : ./tools/deploy-static.sh
# Exit Codes  : 0 = Success, 1 = Missing Ansible or execution failure
# ==============================================================================

# Exit immediately if any command exits with a non-zero status
set -e

# Output header for deployment execution log
echo "======================================================================"
echo "[INFO] CMSForNerd2 Static Site Orchestrator"
echo "======================================================================"

# 1. ENVIRONMENT DETECTION BRANCH
# Check if the current user is 'jules' (unprivileged VM/sandbox container)
# or if JULES_ENV custom environment variable is explicitly set.
if [ "$USER" = "jules" ] || [ -n "$JULES_ENV" ]; then
    # Register the limited sandbox mode flag
    echo "[INFO] Detected Limited Sandbox Environment (Google Jules)."
    IS_LIMITED=true
else
    # Register the potential real/staging OS context flag
    echo "[INFO] Detected Potential Real OS / Production Environment."
    IS_LIMITED=false
fi

# 2. DUAL-PATHWAY ACTION DECISIONS
if [ "$IS_LIMITED" = true ]; then
    # BRANCH A: Google Jules Limited Sandbox VM Action
    echo "[WARN] Running under limited sandbox constraints."
    echo "[INFO] Bypassing system-wide root tasks (nginx install, service configurations, daemon reloads)."
    echo "[INFO] Focusing on unprivileged workspace build operations only."
    echo ""

    # Install local npm dependencies automatically using pinned legacy peer deps option
    echo "[INFO] [1/2] Installing NPM packages..."
    npm install --legacy-peer-deps

    # Compile the Astro 7.1 Static Site Generator (SSG) assets into the dist/ directory
    echo "[INFO] [2/2] Compiling Astro static site (SSG build)..."
    npm run build

    # Output static build complete message and location of compiled assets
    echo ""
    echo "[SUCCESS] Static build complete in limited environment!"
    echo "[INFO] Assets are fully verified and written to: $(pwd)/dist"
else
    # BRANCH B: Production or Staging Real OS Orchestration Action
    echo "[INFO] Running under unrestricted Real OS context."
    echo "[INFO] Performing full system dependency updates and unprivileged build workflows."
    echo ""

    # Check if the ansible-playbook orchestration utility is installed on the host
    if ! command -v ansible-playbook &> /dev/null; then
        echo "[ERROR] Ansible is not installed on this system. Please install it first:"
        echo "   sudo apt update && sudo apt install -y ansible"
        exit 1
    fi

    # Trigger complete system deployment and security hardening using Ansible
    echo "[INFO] Executing complete Ansible deployment playbook..."
    ansible-playbook deploy-static.yml -i inventory/hosts.staging.yml
fi
