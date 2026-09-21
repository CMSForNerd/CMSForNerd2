"""Unit test suite for CMSForNerd2 project files and standard compliance.

This module acts as a unified facade for the modularized unit test suite located in tests/unit/.
It imports and re-exports test functions across domain submodules:
1. Ansible static orchestration playbooks (tests/unit/ansible.py).
2. Container configurations (tests/unit/containers.py).
3. Markdown files for OKF compliance, DSOM footers, and UK English guidelines (tests/unit/markdown.py).
4. Sitemap consistency and JSON configurations (tests/unit/sitemaps.py).
5. LLMs parsing and compilation tools (tests/unit/llms.py).
6. Internal and external broken links validation (tests/unit/links.py).
7. Agent Skills, Mermaid validation, and DSOM workflow tooling (tests/unit/skills_and_dsom.py).
"""

from tests.unit.ansible import test_ansible_playbook_compliance
from tests.unit.containers import test_containerfile_security_and_structure
from tests.unit.links import (
    ExternalBrokenLinksTest,
    InternalBrokenLinksTest,
)
from tests.unit.llms import (
    test_build_llms_full_compilation,
    test_llms_txt2ctx_parser_api,
)
from tests.unit.markdown import (
    test_markdown_governance_footers,
    test_markdown_okf_compliance,
    test_uk_english_documentation_spellings,
)
from tests.unit.mcp import (
    test_create_mcp_app_and_websocket_transport,
    test_dispatch_wasm_component_tool,
    test_get_openwiki_concept,
    test_get_route_content,
    test_get_sitemap_routes,
    test_list_ssg_routes,
    test_mcp_webrtc_p2p_mesh_transport,
    test_run_server_invalid_transport,
    test_search_ssg_routes,
    test_validate_wasm_cm_wit_interface,
    test_websocket_reconnect_failure_mode,
)
from tests.unit.sitemaps import (
    test_context7_configuration,
    test_csp_manifest_and_nonce_injection,
    test_pagefind_sri_manifest,
    test_sitemaps_consistency,
)
from tests.unit.skills_and_dsom import (
    test_agent_charter_and_skills_integrity,
    test_dsom_compaction_engine_payload,
    test_dsom_manifest_sync_script,
    test_validate_mermaid_script_execution,
)

__all__ = [
    "ExternalBrokenLinksTest",
    "InternalBrokenLinksTest",
    "test_agent_charter_and_skills_integrity",
    "test_ansible_playbook_compliance",
    "test_build_llms_full_compilation",
    "test_containerfile_security_and_structure",
    "test_context7_configuration",
    "test_create_mcp_app_and_websocket_transport",
    "test_csp_manifest_and_nonce_injection",
    "test_dispatch_wasm_component_tool",
    "test_dsom_compaction_engine_payload",
    "test_dsom_manifest_sync_script",
    "test_get_openwiki_concept",
    "test_get_route_content",
    "test_get_sitemap_routes",
    "test_list_ssg_routes",
    "test_llms_txt2ctx_parser_api",
    "test_markdown_governance_footers",
    "test_markdown_okf_compliance",
    "test_mcp_webrtc_p2p_mesh_transport",
    "test_pagefind_sri_manifest",
    "test_run_server_invalid_transport",
    "test_search_ssg_routes",
    "test_sitemaps_consistency",
    "test_uk_english_documentation_spellings",
    "test_validate_mermaid_script_execution",
    "test_validate_wasm_cm_wit_interface",
    "test_websocket_reconnect_failure_mode",
]
