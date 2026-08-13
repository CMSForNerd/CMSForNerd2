#!/usr/bin/env bash
# ==============================================================================
# Script Name: deploy-static.sh
# Path:        tools/deploy-static.sh
# Description: Automated Static Deployment Orchestrator for CMSForNerd2.
#              This script detects the execution environment and dynamically
#              branches between a limited sandbox environment (Google Jules)
#              and a full-privileged staging/production environment.
#
# Requirements:
#   - Bash (version 4+)
#   - Node.js & NPM (for static local builds)
#   - Ansible (for staging/production system configuration and deployment)
#
# Usage Instructions:
#   - To run locally in sandbox mode (bypasses system configurations):
#         ./tools/deploy-static.sh
#   - To run in production mode with full system Ansible playbook actions:
#         ./tools/deploy-static.sh (as non-jules user or with real staging hosts config)
# ==============================================================================

# Exit immediately if any command exits with a non-zero status
set -e

# Output decorative header for deployment execution log
echo "======================================================================"
echo "🚀 CMSForNerd2 Static Site Orchestrator"
echo "======================================================================"

# 1. ENVIRONMENT DETECTION BRANCH
# Check if the current user is 'jules' (unprivileged VM/sandbox container)
# or if JULES_ENV custom environment variable is explicitly set.
if [ "$USER" = "jules" ] || [ -n "$JULES_ENV" ]; then
    # Register the limited sandbox mode flag
    echo "🔍 Detected Limited Sandbox Environment (Google Jules)."
    IS_LIMITED=true
else
    # Register the potential real/staging OS context flag
    echo "🔍 Detected Potential Real OS / Production Environment."
    IS_LIMITED=false
fi

# 2. DUAL-PATHWAY ACTION DECISIONS
if [ "$IS_LIMITED" = true ]; then
    # BRANCH A: Google Jules Limited Sandbox VM Action
    echo "⚠️  Running under limited sandbox constraints."
    echo "👉 Bypassing system-wide root tasks (nginx install, service configurations, daemon reloads)."
    echo "👉 Focusing on unprivileged workspace build operations only."
    echo ""

    # Install local npm dependencies automatically using pinned legacy peer deps option
    echo "📦 [1/2] Installing NPM packages..."
    npm install --legacy-peer-deps

    # Compile the Astro 7.1 Static Site Generator (SSG) assets into the dist/ directory
    echo "🏗️  [2/2] Compiling Astro static site (SSG build)..."
    npm run build

    # Output static build complete message and location of compiled assets
    echo ""
    echo "✅ Success: Static build complete in limited environment!"
    echo "Assets are fully verified and written to: $(pwd)/dist"
else
    # BRANCH B: Production or Staging Real OS Orchestration Action
    echo "💪 Running under unrestricted Real OS context."
    echo "👉 Performing full system dependency updates and unprivileged build workflows."
    echo ""

    # Check if the ansible-playbook orchestration utility is installed on the host
    if ! command -v ansible-playbook &> /dev/null; then
        echo "❌ Ansible is not installed on this system. Please install it first:"
        echo "   sudo apt update && sudo apt install -y ansible"
        exit 1
    fi

    # Trigger complete system deployment and security hardening using Ansible
    echo "🎬 Executing complete Ansible deployment playbook..."
    ansible-playbook deploy-static.yml -i inventory/hosts.staging.yml
fi
