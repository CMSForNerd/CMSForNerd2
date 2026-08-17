"""LLMs.txt context parser and full compilation unit tests."""

import os
import sys


def test_llms_txt2ctx_parser_api():
    """Validates the CLI and API implementation in tools/llms_txt2ctx.py.

    Verifies that the parser correctly parses an llms.txt sample string and
    builds standard-compliant XML output according to the llmstxt.org spec.
    """
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
