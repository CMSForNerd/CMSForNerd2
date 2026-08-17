"""Unit test suite for CMSForNerd2 project files and standard compliance.

This module acts as a unified facade for the modularized unit test suite located in tests/unit/.
It imports and re-exports test functions across domain submodules:
1. Ansible static orchestration playbooks (tests/unit/ansible.py).
2. Container configurations (tests/unit/containers.py).
3. Markdown files for OKF compliance, DSOM footers, and UK English guidelines (tests/unit/markdown.py).
4. Sitemap consistency and JSON configurations (tests/unit/sitemaps.py).
5. LLMs parsing and compilation tools (tests/unit/llms.py).
"""

from tests.unit.ansible import test_ansible_playbook_compliance
from tests.unit.containers import test_containerfile_security_and_structure
from tests.unit.markdown import (
    test_markdown_okf_compliance,
    test_markdown_governance_footers,
    test_uk_english_documentation_spellings,
)
from tests.unit.sitemaps import (
    test_sitemaps_consistency,
    test_context7_configuration,
)
from tests.unit.llms import (
    test_llms_txt2ctx_parser_api,
    test_build_llms_full_compilation,
)

__all__ = [
    "test_ansible_playbook_compliance",
    "test_containerfile_security_and_structure",
    "test_markdown_okf_compliance",
    "test_markdown_governance_footers",
    "test_uk_english_documentation_spellings",
    "test_sitemaps_consistency",
    "test_context7_configuration",
    "test_llms_txt2ctx_parser_api",
    "test_build_llms_full_compilation",
]
