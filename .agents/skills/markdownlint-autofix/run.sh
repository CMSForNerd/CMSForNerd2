#!/usr/bin/env bash
# ==============================================================================
# Skill       : markdownlint-autofix
# Path        : .agents/skills/markdownlint-autofix/run.sh
# Purpose     : Executable runner script for markdownlint inspection and auto-correction.
# ==============================================================================

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$REPO_ROOT"

echo "[INFO] Running Markdown Sanitation & Autofix Skill..."
npx markdownlint-cli --fix "**/*.md" --ignore "node_modules" --ignore ".git" --ignore "dist" --ignore ".astro"
echo "[SUCCESS] Markdown sanitation complete!"
