"""Markdown frontmatter, governance footers, and UK English spelling unit tests."""

import os
import re
import yaml
import pytest


def test_markdown_okf_compliance():
    """Validates all workspace markdown files against the OKF v0.1 schema.

    Checks recursively across the repository that every Markdown file:
    - Starts with three hyphens '---' at line 1, column 1.
    - Parses successfully as OKF v0.1 YAML frontmatter with required keys.
    - Ensures special characters in string values are double quoted.
    - Array formatting (topics) uses square brackets with double quoted strings.
    """
    markdown_files = []
    for root, _, files in os.walk("."):
        if any(p in root for p in ["node_modules", ".git", ".astro", "dist", ".pytest_cache"]):
            continue
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))

    assert len(markdown_files) > 0, "No markdown files found in workspace."

    for filepath in markdown_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Check OKF starting line
        assert content.startswith("---"), f"Markdown file {filepath} must start with frontmatter '---' on line 1, column 1."

        # Find frontmatter boundary
        end_idx = content.find("---", 3)
        assert end_idx != -1, f"Markdown file {filepath} has unclosed frontmatter block."

        frontmatter_text = content[3:end_idx].strip()

        # 2. Well-formed YAML and Required fields
        try:
            fm_data = yaml.safe_load(frontmatter_text)
        except Exception as e:
            pytest.fail(f"Markdown file {filepath} has invalid YAML frontmatter: {e}")

        required_keys = ["okf_version", "type", "title", "timestamp", "topics"]
        for key in required_keys:
            assert key in fm_data, f"Markdown file {filepath} is missing required OKF frontmatter key: '{key}'"

        assert float(fm_data["okf_version"]) == 0.1, f"Markdown file {filepath} must use okf_version 0.1."

        # Check array structure for topics
        topics = fm_data["topics"]
        assert isinstance(topics, list), f"Markdown file {filepath} 'topics' attribute must be an array."

        # Check special characters in frontmatter lines (Double Quoting Rule)
        lines = frontmatter_text.splitlines()
        for line in lines:
            if ":" in line:
                parts = line.split(":", 1)
                val = parts[1].strip()
                if val:
                    # If value contains emojis, colons, brackets, or other special characters
                    # It must be double quoted
                    if any(c in val for c in ["🎨", "🧠", "🚀", "🧪", "📋", "🏗️", "🧱", "[", "]", ":"]):
                        # Check that it starts and ends with double quotes
                        # Or it's a valid JSON array format
                        is_quoted = (val.startswith('"') and val.endswith('"')) or (val.startswith('[') and val.endswith(']'))
                        assert is_quoted, f"Value '{val}' in frontmatter of {filepath} containing special characters must be double quoted."


def test_markdown_governance_footers():
    """Validates that all core governance and skill markdown files contain standard DSOM footers.

    Ensures that every governance document under .agents/ or in the root directory (excluding pages)
    carries the standardized Deep State of Mind signature and standard UK English declarations.
    """
    governance_files = []

    # Include root level governance documents
    root_docs = ["README.md", "START-HERE.md", "SUMMARY.md", "llms.txt", "AGENTS.md"]
    for doc in root_docs:
        if os.path.exists(doc):
            governance_files.append(doc)

    # Include all .agents/ and .agents/skills/ files
    for root, _, files in os.walk(".agents"):
        for file in files:
            if file.endswith(".md"):
                governance_files.append(os.path.join(root, file))

    assert len(governance_files) > 0, "No governance markdown files found."

    for filepath in governance_files:
        # Skip task.md and walkthrough.md if present
        if "task.md" in filepath or "walkthrough.md" in filepath:
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        non_empty_lines = [line.strip() for line in content.splitlines() if line.strip()]
        assert len(non_empty_lines) >= 2, f"Governance file {filepath} is too short to have a footer."

        footer_text = " ".join(non_empty_lines[-5:])
        has_dsom = "Deep State of Mind" in footer_text or "DSOM" in footer_text
        has_uk = "UK English" in footer_text or "UK-English" in footer_text or "DBP-standard" in footer_text

        assert has_dsom, f"Governance markdown file {filepath} is missing 'Deep State of Mind (DSOM)' standard footer declaration."
        assert has_uk, f"Governance markdown file {filepath} is missing Standard/UK English declaration in the footer."


def test_uk_english_documentation_spellings():
    """Validates that newly written and root documentation files use standard UK English spellings.

    Ensures that words like 'optimise', 'colour', 'customise' are preferred over US English equivalents
    ('optimize', 'color', 'customize') within primary root-level documents.
    """
    target_docs = ["README.md", "START-HERE.md", "SUMMARY.md", "AGENTS.md", ".agents/AGENTS.md"]

    # Prohibited US spellings (where UK equivalent is mandated)
    us_to_uk_patterns = {
        r"\bcolor\b": "colour",
        r"\bcolors\b": "colours",
        r"\bflavor\b": "flavour",
        r"\bflavors\b": "flavours",
        r"\boptimize\b": "optimise",
        r"\boptimized\b": "optimised",
        r"\boptimizing\b": "optimising",
        r"\bcustomize\b": "customise",
        r"\bcustomized\b": "customised",
        r"\bcustomizing\b": "customising",
        r"\borganization\b": "organisation",
        r"\borganizations\b": "organisations",
    }

    for doc in target_docs:
        assert os.path.exists(doc), f"Target documentation file {doc} does not exist."
        with open(doc, "r", encoding="utf-8") as f:
            content = f.read().lower()

        # Check for forbidden patterns
        for pattern, replacement in us_to_uk_patterns.items():
            match = re.search(pattern, content)
            assert not match, f"Prohibited US English spelling found in {doc}: '{match.group(0)}'. Use UK spelling '{replacement}' instead."
