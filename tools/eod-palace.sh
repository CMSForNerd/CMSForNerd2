#!/usr/bin/env bash
# ==============================================================================
# Protocol    : Deep State of Mind (DSOM) For My AI Protocol
# Author      : Harisfazillah Jamel (LinuxMalaysia)
# Timestamp   : 2026-09-09
# License     : GNU General Public License v3.0
# Standard    : UK English | DBP-standard Bahasa Melayu Malaysia (Piawai)
# ==============================================================================
# Script Name : eod-palace.sh
# Path        : tools/eod-palace.sh
# Description : End-of-Day Spatial Palace & Pre-Commit Quality Guardrail Script.
#               Validates spatial memory brain integrity in .agents/brain/,
#               enforces OKF v0.2 frontmatter compliances, and verifies
#               sitemaps and asset integrity before git commits.
#
# Requirements:
#   - Bash shell (version 4+)
#   - Node.js & NPM (for OKF refactoring and sitemap verification)
#   - Python 3 & Ruff & Mypy (for static linter and type checking guardrails)
#   - Git (for workspace status checks)
#
# Usage Instructions:
#   - Run prior to committing changes or at end-of-day session completion:
#         ./tools/eod-palace.sh
#   - Ensure exit code is 0 before committing to version control.
# ==============================================================================

# Exit immediately if any command in the pipeline fails
set -e

# Output decorative header for guardrail execution log
echo "======================================================================"
echo "🏰 DSOM Spatial Palace & Pre-Commit Guardrail Inspector"
echo "======================================================================"

# Determine workspace root directory relative to the location of this script
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Change active working directory to repository root
cd "$REPO_ROOT"

# 1. SPATIAL BRAIN INTEGRITY CHECK
# Verify that all essential spatial memory brain files exist in .agents/brain/
echo "🧠 [1/4] Checking spatial brain files in .agents/brain/..."
REQUIRED_BRAIN_FILES=(
    ".agents/brain/knowledge.md"
    ".agents/brain/palace_registry.md"
    ".agents/brain/active_context_manifest.md"
    ".agents/brain/checkpoint_summary.txt"
)

# Iterate through required spatial brain files and assert physical existence
for file in "${REQUIRED_BRAIN_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Error: Spatial brain file missing: $file"
        exit 1
    fi
    echo "  ✓ Found $file"
done

# Check for uncommitted drift or modified files in .agents/brain/
if git status --porcelain .agents/brain/ | grep -q 'M'; then
    echo "⚠️ Warning: Uncommitted spatial brain modifications detected in .agents/brain/"
fi

# 2. OKF FRONTMATTER COMPLIANCE CHECK
# Run Node facade script to trigger Python OKF v0.2 migration and validation
echo "📄 [2/4] Validating OKF v0.2 frontmatter compliance..."
if command -v node >/dev/null 2>&1; then
    node tools/refactor-okf.cjs
else
    echo "⚠️ Node.js not found, skipping OKF frontmatter validation."
fi

# 3. SITEMAP & LINK INTEGRITY VERIFICATION
# Verify built dist/ directory sitemap URLs and asset mappings if dist/ exists
echo "🌐 [3/4] Verifying sitemap and physical asset links..."
if [ -d "dist" ] && command -v node >/dev/null 2>&1; then
    node tools/verify-sitemaps.js
else
    echo "ℹ️ Compiled dist/ directory not found or Node missing. Skipping sitemap link check."
fi

# 4. STATIC ANALYSIS & LINTING GUARDRAIL
# Execute Ruff check for code style and Mypy for strict Python type checking
echo "🔍 [4/4] Executing static analysis guardrails (Ruff & Mypy)..."
if command -v ruff >/dev/null 2>&1; then
    ruff check tests/ tools/
fi

if command -v mypy >/dev/null 2>&1; then
    PYTHONPATH=. mypy --explicit-package-bases --strict tests tools
fi

# Log success notification upon completing all pre-commit guardrail steps
echo ""
echo "✅ All DSOM End-of-Day Palace pre-commit guardrails passed successfully!"
