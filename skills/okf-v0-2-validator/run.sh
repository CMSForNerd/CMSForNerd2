#!/usr/bin/env bash
# ==============================================================================
# Skill       : okf-v0-2-validator
# Path        : skills/okf-v0-2-validator/run.sh
# Purpose     : Executable runner script for auditing and migrating Markdown assets
#               to Open Knowledge Format (OKF) v0.2 frontmatter trust signals.
# ==============================================================================

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

echo "[INFO] Running OKF v0.2 Frontmatter Validator Skill..."
node tools/refactor-okf.cjs
echo "[SUCCESS] OKF v0.2 Frontmatter validation complete!"
