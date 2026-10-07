#!/usr/bin/env bash
# ==============================================================================
# Skill       : playbook-test-runner
# Path        : .agents/skills/playbook-test-runner/run.sh
# Purpose     : Executable runner script for static linting and syntax checking
#               all Ansible playbooks in the workspace.
# ==============================================================================

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$REPO_ROOT"

echo "[INFO] Running Ansible Playbook Test Runner Skill..."
ansible-lint playbooks/
ansible-playbook --syntax-check playbooks/*.yml
echo "[SUCCESS] Ansible Playbook testing complete!"
