#!/usr/bin/env bash
# ==============================================================================
# Protocol    : Deep State of Mind (DSOM) For My AI Protocol
# Author      : Harisfazillah Jamel (LinuxMalaysia)
# Timestamp   : 2026-09-17
# License     : GNU General Public License v3.0
# Standard    : UK English | DBP-standard Bahasa Melayu Malaysia (Piawai)
# ==============================================================================
# Script Name : dsom-manifest-sync.sh
# Path        : tools/dsom-manifest-sync.sh
# Description : Automated Git Hook & State Manifest Synchronization Script (Step 5).
#               Captures repository state deltas, invokes DSOM compaction,
#               and updates active context manifests and episodic ledgers.
#
# Requirements:
#   - Bash shell (version 4+)
#   - Python 3 & tools/dsom_compaction_engine.py
#   - Git (for workspace status inspection)
#
# Usage Instructions:
#   - Execute on session completion or as post-commit Git hook:
#         ./tools/dsom-manifest-sync.sh
# ==============================================================================

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "🔄 [DSOM Manifest Sync] Synchronizing spatial memory state files..."

# Capture current git status changes
CHANGED_FILES="$(git status --porcelain | head -n 10 | tr '\n' '; ')"
if [ -z "$CHANGED_FILES" ]; then
    CHANGED_FILES="Workspace clean - no uncommitted file modifications"
fi

# Execute compaction engine to generate compressed JSON payload
COMPACTION_OUTPUT="$(python3 tools/dsom_compaction_engine.py \
    --intent "Synchronize active context manifest and episodic ledger" \
    --mutations "$CHANGED_FILES" \
    --telemetry "Pre-commit guardrail verification state nominal" \
    --keys "DSOM_MANIFEST_SYNC,STATE_LEAF_UPDATED")"

TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Update active context manifest (.agents/brain/active_context_manifest.md)
cat <<EOF > .agents/brain/active_context_manifest.md
---
spec_version: "0.2"
type: "documentation"
title: "DSOM Active Context Manifest"
description: "Real-time spatial memory manifest tracking active session intent, system mutations, and operational state."
topics: ["dsom", "manifest", "active-context", "spatial-memory"]
status: "stable"
stale_after: "2027-03-06"
sources:
- id: workspace_file
  title: active_context_manifest.md
  url: .agents/brain/active_context_manifest.md
generated:
  by: "Repository Architect & OKF v0.2 Compliance Agent"
  at: '$TIMESTAMP'
tags: ["dsom", "manifest", "active-context", "spatial-memory"]
---

# DSOM Active Context Manifest

*Last Synchronized:* \`$TIMESTAMP\`

## Active Intent
Maintain 100% OKF v0.2 compliance, agent skill registry synchronization, and DSOM workflow blueprint integration.

## Active Workspace Mutations
\`\`\`
$CHANGED_FILES
\`\`\`

## Latest Compacted JSON Payload
\`\`\`json
$COMPACTION_OUTPUT
\`\`\`

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
EOF

# Append checkpoint entry to episodic ledger (.agents/brain/checkpoint_summary.txt)
echo "[$TIMESTAMP] DSOM Manifest Sync | Mutations: $CHANGED_FILES" >> .agents/brain/checkpoint_summary.txt

echo "✅ [DSOM Manifest Sync] Context manifest and episodic ledger synchronized successfully!"
