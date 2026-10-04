"""Unit tests for OpenWiki Emulator script and OpenWiki Compiler Agent Skill."""

import json
from pathlib import Path
from typing import Any

import yaml

from tools.openwiki_emulator import (
    OPENWIKI_DIR,
    REPO_ROOT,
    cmd_export_graph,
    cmd_init,
    cmd_search,
    cmd_update,
    process_markdown_file,
    validate_mermaid_diagram,
)


def test_openwiki_emulator_init() -> None:
    """Verify that cmd_init creates all required files and OKF v0.2 frontmatter in openwiki/."""
    cmd_init()

    assert OPENWIKI_DIR.exists()
    assert (OPENWIKI_DIR / "_skeleton.md").is_file()
    assert (OPENWIKI_DIR / ".last-update.json").is_file()
    assert (OPENWIKI_DIR / "INSTRUCTIONS.md").is_file()
    assert (OPENWIKI_DIR / "graph.html").is_file()
    assert (OPENWIKI_DIR / "quickstart.md").is_file()

    # Verify JSON tracking metadata
    last_update_data = json.loads((OPENWIKI_DIR / ".last-update.json").read_text(encoding="utf-8"))
    assert last_update_data["status"] == "success"
    assert "DSOM Python OpenWiki Emulator" in last_update_data["engine"]

    # Verify OKF frontmatter on generated markdown pages
    for md_file in OPENWIKI_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        assert content.startswith("---"), f"{md_file} missing starting frontmatter delimiter"
        parts = content.split("---", 2)
        assert len(parts) >= 3, f"{md_file} malformed frontmatter"
        meta = yaml.safe_load(parts[1])
        assert isinstance(meta, dict), f"{md_file} frontmatter not dict"
        assert "type" in meta or "okf_version" in meta or "spec_version" in meta
        assert "title" in meta


def test_openwiki_emulator_search_and_update(capsys: Any) -> None:
    """Verify that cmd_search and cmd_update execute cleanly and report matching pages."""
    cmd_init()

    cmd_search("ansible")
    captured = capsys.readouterr()
    assert "Found 1 matching OpenWiki page(s)" in captured.out
    assert "ansible-baseline.md" in captured.out

    cmd_update()
    assert (OPENWIKI_DIR / ".last-update.json").is_file()


def test_openwiki_standalone_graph_export() -> None:
    """Verify that cmd_export_graph produces offline standalone HTML visualizer."""
    graph_file = OPENWIKI_DIR / "graph.html"
    if graph_file.exists():
        graph_file.unlink()

    cmd_export_graph()
    assert graph_file.is_file()
    content = graph_file.read_text(encoding="utf-8")
    assert "DSOM OpenWiki Standalone Knowledge Graph" in content
    assert "quickstart.md" in content


def test_openwiki_mermaid_validation_and_self_healing(tmp_path: Path) -> None:
    """Test Mermaid diagram syntax validation, error degradation, and self-healing recovery."""
    valid_code = "flowchart TD\n    A[Start] --> B[End]"
    is_valid, reason = validate_mermaid_diagram(valid_code)
    assert is_valid
    assert reason == ""

    invalid_code = "flowchart TD\n    A[Start) --> B[End]"
    is_valid_inv, reason_inv = validate_mermaid_diagram(invalid_code)
    assert not is_valid_inv
    assert "mismatched grouping characters" in reason_inv

    # Test file processing and degradation
    test_md = tmp_path / "test_diagram.md"
    test_md.write_text(f"# Test\n```mermaid\n{invalid_code}\n```\n", encoding="utf-8")

    process_markdown_file(test_md)
    degraded_content = test_md.read_text(encoding="utf-8")
    assert "%% openwiki-error:" in degraded_content
    assert "mismatched grouping characters" in degraded_content

    # Fix the file to test self-healing
    fixed_md_content = degraded_content.replace("A[Start)", "A[Start]")
    test_md.write_text(fixed_md_content, encoding="utf-8")

    process_markdown_file(test_md)
    healed_content = test_md.read_text(encoding="utf-8")
    assert "```mermaid" in healed_content
    assert "%% openwiki-error:" not in healed_content


def test_openwiki_skill_integrity() -> None:
    """Verify that OpenWiki Compiler skill files exist, are synchronized, and conform to OKF v0.2."""
    skill_root = REPO_ROOT / "skills" / "openwiki-compiler" / "SKILL.md"
    skill_agent = REPO_ROOT / ".agents" / "skills" / "openwiki-compiler" / "SKILL.md"

    assert skill_root.is_file()
    assert skill_agent.is_file()

    root_content = skill_root.read_text(encoding="utf-8")
    agent_content = skill_agent.read_text(encoding="utf-8")
    assert root_content == agent_content

    meta = yaml.safe_load(root_content.split("---", 2)[1])
    assert meta["name"] == "openwiki-compiler"
    assert meta["spec_version"] == "0.2"
    assert meta["type"] == "skill"
