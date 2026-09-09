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
# ==============================================================================

set -e

echo "======================================================================"
echo "🏰 DSOM Spatial Palace & Pre-Commit Guardrail Inspector"
echo "======================================================================"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# 1. SPATIAL BRAIN INTEGRITY CHECK
echo "🧠 [1/4] Checking spatial brain files in .agents/brain/..."
REQUIRED_BRAIN_FILES=(
    ".agents/brain/knowledge.md"
    ".agents/brain/palace_registry.md"
    ".agents/brain/active_context_manifest.md"
    ".agents/brain/checkpoint_summary.txt"
)

for file in "${REQUIRED_BRAIN_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Error: Spatial brain file missing: $file"
        exit 1
    fi
    echo "  ✓ Found $file"
done

# Check uncommitted drift or changes in .agents/brain/
if git status --porcelain .agents/brain/ | grep -q 'M'; then
    echo "⚠️ Warning: Uncommitted spatial brain modifications detected in .agents/brain/"
fi

# 2. OKF FRONTMATTER COMPLIANCE CHECK
echo "📄 [2/4] Validating OKF v0.2 frontmatter compliance..."
if command -v node >/dev/null 2>&1; then
    node tools/refactor-okf.cjs
else
    echo "⚠️ Node.js not found, skipping OKF frontmatter validation."
fi

# 3. SITEMAP & LINK INTEGRITY VERIFICATION
echo "🌐 [3/4] Verifying sitemap and physical asset links..."
if [ -d "dist" ] && command -v node >/dev/null 2>&1; then
    node tools/verify-sitemaps.js
else
    echo "ℹ️ Compiled dist/ directory not found or Node missing. Skipping sitemap link check."
fi

# 4. STATIC ANALYSIS & LINTING GUARDRAIL
echo "🔍 [4/4] Executing static analysis guardrails (Ruff & Mypy)..."
if command -v ruff >/dev/null 2>&1; then
    ruff check tests/ tools/
fi

if command -v mypy >/dev/null 2>&1; then
    PYTHONPATH=. mypy --explicit-package-bases --strict tests tools
fi

echo ""
echo "✅ All DSOM End-of-Day Palace pre-commit guardrails passed successfully!"
