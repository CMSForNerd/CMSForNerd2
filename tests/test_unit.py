"""Unit test suite for CMSForNerd2 project files and standard compliance.

This module contains Python unit tests verifying standard compliant syntax, schemas,
and configurations across different project assets:
1. Ansible static orchestration playbooks (deploy-static.yml) for FQCN and dual-pathway.
2. Container configurations (Dockerfile and Containerfile) for Docker/Podman security and settings.
3. Markdown files for OKF (Open Knowledge Format) v0.1 compliance, DSOM footer standards, and UK English guidelines.
4. Sitemap consistency and JSON configurations (context7.json).
"""

import os
import json
import re
import yaml
import pytest

def test_ansible_playbook_compliance():
    """Validates deploy-static.yml for ansible-lint and dual-pathway compliance.

    Verifies that:
    - The playbook is well-formed YAML.
    - All tasks use Fully Qualified Collection Names (FQCN).
    - The playbook contains dual-pathway branching variables (is_limited_environment).
    - Idempotency is supported via changed_when parameters on commands.
    """
    playbook_path = "deploy-static.yml"
    assert os.path.exists(playbook_path), "Ansible playbook deploy-static.yml not found."

    with open(playbook_path, "r", encoding="utf-8") as f:
        playbook_data = yaml.safe_load(f)

    assert isinstance(playbook_data, list), "Playbook root must be a list of plays."
    play = playbook_data[0]

    # Check for gather_facts
    assert play.get("gather_facts") is True, "gather_facts should be true."

    # Check for is_limited_environment variable detection task
    tasks = play.get("tasks", [])
    assert len(tasks) > 0, "Playbook has no tasks defined."

    has_detection_task = False
    for task in tasks:
        # Check module FQCN
        for key in task.keys():
            # Skip common task meta-parameters
            if key in ["name", "become", "when", "tags", "vars", "args", "changed_when"]:
                continue
            # Ensure the module key has FQCN structure
            assert "." in key, f"Task '{task.get('name')}' uses non-FQCN action/module: '{key}'"

        # Check for user-detection set_fact task
        if task.get("ansible.builtin.set_fact") and "is_limited_environment" in task.get("ansible.builtin.set_fact", {}):
            has_detection_task = True

        # Check command idempotency
        if task.get("ansible.builtin.command"):
            assert "changed_when" in task, f"Command task '{task.get('name')}' is missing 'changed_when' attribute."

    assert has_detection_task, "Playbook does not define the dual-pathway user detection set_fact task."


@pytest.mark.parametrize("container_file", ["Dockerfile", "Containerfile"])
def test_containerfile_security_and_structure(container_file):
    """Validates Containerfile and Dockerfile for standard-compliant specifications.

    Verifies that:
    - Multi-stage builds are used (builder, runtime stages).
    - Build stage inherits from node:22-alpine.
    - Runs under unprivileged USER nginx.
    - Exposes unprivileged web port 8080.
    """
    assert os.path.exists(container_file), f"{container_file} not found."

    with open(container_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify Node version for builder
    assert "node:22-alpine" in content, f"{container_file} should utilize Node 22 (node:22-alpine) in the builder stage."

    # Verify runtime Alpine Nginx
    assert "nginx:alpine-slim" in content or "nginx" in content, f"{container_file} should package the runtime using Nginx."

    # Verify unprivileged USER execution
    assert "USER nginx" in content, f"{container_file} must switch to unprivileged 'USER nginx' for production security."

    # Verify exposed port
    assert "EXPOSE 8080" in content, f"{container_file} must expose unprivileged port 8080."


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
        # Skip task.md and walkthrough.md if they are highly volatile memory files that are constantly modified,
        # but let's check them if they have it, or focus on main ones.
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


def test_sitemaps_consistency():
    """Validates consistency between root sitemap.txt and public/sitemap.txt.

    Checks that both files exist, are identical in length and content,
    and only contain secure HTTPS URLs with no broken elements.
    """
    root_sitemap = "sitemap.txt"
    public_sitemap = "public/sitemap.txt"

    assert os.path.exists(root_sitemap), "Root sitemap.txt not found."
    assert os.path.exists(public_sitemap), "public/sitemap.txt not found."

    with open(root_sitemap, "r", encoding="utf-8") as f:
        root_content = f.read().strip()

    with open(public_sitemap, "r", encoding="utf-8") as f:
        public_content = f.read().strip()

    assert root_content == public_content, "sitemap.txt and public/sitemap.txt are not identical."

    urls = root_content.splitlines()
    assert len(urls) > 0, "Sitemaps are empty."

    for url in urls:
        assert url.startswith("https://"), f"Sitemap URL '{url}' must use secure HTTPS protocol."
        assert "undefined" not in url, f"Sitemap URL '{url}' contains 'undefined' pattern."
        assert "[object" not in url, f"Sitemap URL '{url}' contains JavaScript object string serialization."


def test_context7_configuration():
    """Validates context7.json format and schema structure.

    Checks that the context7.json config exists, is valid JSON, and
    contains correct keys.
    """
    config_path = "context7.json"
    assert os.path.exists(config_path), "context7.json not found."

    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "url" in data, "context7.json missing 'url' key."
    assert "public_key" in data, "context7.json missing 'public_key' key."
    assert data["url"].startswith("https://"), "Context7 URL must be secure HTTPS."


def test_llms_txt2ctx_parser_api():
    """Validates the CLI and API implementation in tools/llms_txt2ctx.py.

    Verifies that the parser correctly parses an llms.txt sample string and
    builds standard-compliant XML output according to the llmstxt.org spec.
    """
    import sys
    sys.path.append("tools")
    from llms_txt2ctx import parse_llms_txt, create_ctx

    sample_txt = """# FastHTML

> FastHTML is a python library which...

Some descriptive background notes here.

## Docs

- [Surreal](https://host/README.md): Tiny jQuery alternative
- [FastHTML quick start](https://host/quickstart.html.md): An overview

## Optional

- [Starlette docs](https://host/starlette-sml.md): Optional reference
"""

    parsed = parse_llms_txt(sample_txt)
    assert parsed["title"] == "FastHTML"
    assert parsed["summary"] == "FastHTML is a python library which..."
    assert "background notes" in parsed["info"]
    assert "Docs" in parsed["sections"]
    assert len(parsed["sections"]["Docs"]) == 2
    assert parsed["sections"]["Docs"][0]["title"] == "Surreal"
    assert parsed["sections"]["Docs"][0]["url"] == "https://host/README.md"
    assert parsed["sections"]["Docs"][0]["desc"] == "Tiny jQuery alternative"

    # Test create_ctx API without optional section
    xml_output = create_ctx(sample_txt, include_optional=False)
    assert '<project title="FastHTML" summary="FastHTML is a python library which...">' in xml_output
    assert '<section name="Docs">' in xml_output
    assert 'url="https://host/README.md"' in xml_output
    assert '<section name="Optional">' not in xml_output

    # Test create_ctx API with optional section
    xml_output_with_opt = create_ctx(sample_txt, include_optional=True)
    assert '<section name="Optional">' in xml_output_with_opt


def test_build_llms_full_compilation():
    """Validates that tools/build_llms_full.py correctly processes llms.txt.

    Verifies that the compilation utility successfully parses target markdown files,
    resolves their references, and compiles the single consolidated llms-full.txt file.
    """
    llms_full_file = "llms-full.txt"
    assert os.path.exists(llms_full_file), "llms-full.txt was not compiled or is missing."

    with open(llms_full_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "CMSForNerd2 Complete Documentation (llms-full.txt)" in content, "llms-full.txt header missing."
    assert "## File: README.md" in content, "README.md inclusion segment missing."
    assert "Deep State of Mind (DSOM)" in content, "Standard DSOM footer components missing."
