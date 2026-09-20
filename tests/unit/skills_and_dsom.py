"""Unit tests for Agent Skills, Mermaid validation, and DSOM Agentic Workflow tooling."""

import os
import subprocess
from pathlib import Path

from tools.dsom_compaction_engine import create_compacted_payload


def test_validate_mermaid_script_execution() -> None:
    """Validate that tools/validate-mermaid.js executes and verifies all Mermaid diagrams.

    Raises:
        AssertionError: If validate-mermaid.js fails or returns a non-zero exit status.

    """
    script_path = Path("tools/validate-mermaid.js")
    assert script_path.exists(), "tools/validate-mermaid.js does not exist."

    node_bin = os.path.expanduser("~/.nvm/versions/node/v22.22.1/bin/node")
    cmd = [node_bin, str(script_path)] if os.path.exists(node_bin) else ["node", str(script_path)]

    env = os.environ.copy()
    if os.path.exists(node_bin):
        node_dir = os.path.dirname(node_bin)
        env["PATH"] = f"{node_dir}:{env.get('PATH', '')}"

    result = subprocess.run(cmd, capture_output=True, text=True, env=env, check=False)
    assert result.returncode == 0, f"validate-mermaid.js failed with error:\n{result.stderr}"
    assert "All" in result.stdout and "passed syntax validation cleanly" in result.stdout


def test_dsom_compaction_engine_payload() -> None:
    """Test DSOM Compaction Engine Python API and CLI output schema.

    Raises:
        AssertionError: If compaction payload fails schema validation or CLI execution.

    """
    # 1. API Verification
    payload = create_compacted_payload(
        active_intent="Unit test active intent validation",
        constraints=["pytest", "mypy"],
        system_mutations="Added skills_and_dsom.py unit tests",
        telemetry_vectors="All tests green",
        memory_keys=["UNIT_TEST_SYNC"],
    )

    assert "dsom_compaction_meta" in payload
    assert payload["dsom_compaction_meta"]["protocol_version"] == "0.2"
    assert payload["active_intent"] == "Unit test active intent validation"
    assert "pytest" in payload["operational_constraints"]
    assert payload["context_deltas"]["system_mutations"] == "Added skills_and_dsom.py unit tests"
    assert "UNIT_TEST_SYNC" in payload["episodic_memory_keys"]

    # 2. CLI Subprocess Verification
    cmd = ["python3", "tools/dsom_compaction_engine.py", "--intent", "CLI Execution Test"]
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    assert res.returncode == 0, f"dsom_compaction_engine.py CLI failed: {res.stderr}"
    assert '"protocol_version": "0.2"' in res.stdout
    assert '"active_intent": "CLI Execution Test"' in res.stdout


def test_dsom_manifest_sync_script() -> None:
    """Test tools/dsom-manifest-sync.sh execution and spatial memory sync.

    Raises:
        AssertionError: If manifest sync script fails or output files are missing.

    """
    script_path = Path("tools/dsom-manifest-sync.sh")
    assert script_path.exists(), "tools/dsom-manifest-sync.sh does not exist."

    res = subprocess.run(["./tools/dsom-manifest-sync.sh"], capture_output=True, text=True, check=False)
    assert res.returncode == 0, f"dsom-manifest-sync.sh failed: {res.stderr}"

    manifest_path = Path(".agents/brain/active_context_manifest.md")
    assert manifest_path.exists(), ".agents/brain/active_context_manifest.md missing after sync."

    content = manifest_path.read_text(encoding="utf-8")
    assert 'spec_version: "0.2"' in content
    assert "DSOM Active Context Manifest" in content

    checkpoint_path = Path(".agents/brain/checkpoint_summary.txt")
    assert checkpoint_path.exists(), ".agents/brain/checkpoint_summary.txt missing after sync."


def test_agent_charter_and_skills_integrity() -> None:
    """Verify newly created Agent Skills and Agent Charter files against OKF schema.

    Raises:
        AssertionError: If target skill or charter files are missing or lack OKF frontmatter.

    """
    target_files = [
        ".agents/skills/mermaid-validation/SKILL.md",
        "skills/mermaid-validation/SKILL.md",
        ".agents/skills/reskill/SKILL.md",
        "skills/reskill/SKILL.md",
        "docs/governance/AI-AGENT-CHARTER-TEMPLATE.md",
        "docs/explanation/dsom-agentic-workflow-blueprint.md",
    ]

    for rel_path in target_files:
        path = Path(rel_path)
        assert path.exists(), f"Target governance/skill file missing: {rel_path}"

        content = path.read_text(encoding="utf-8")
        assert content.startswith("---"), f"File {rel_path} must start with OKF frontmatter '---'."
        assert 'spec_version: "0.2"' in content, f"File {rel_path} missing required spec_version: \"0.2\"."
        assert "Deep State of Mind" in content or "DSOM" in content, f"File {rel_path} missing DSOM signature."
