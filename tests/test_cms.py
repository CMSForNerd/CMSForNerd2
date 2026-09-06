"""Integration test suite for the CMSForNerd2 static modernisation project.

This module provides automated end-to-end integration tests to verify the correctness
of sitemaps, frontmatter OKF (Open Knowledge Format) v0.1 compliance, and the HTML
rendering of all migrated markdown content pages within the Astro 7.1 SSG framework.
"""

import os
import subprocess

import pytest
import requests

# Find all markdown files in src/content/pages/
CONTENT_DIR = "src/content/pages"
markdown_files = [f for f in os.listdir(CONTENT_DIR) if f.endswith(".md")]

def test_sitemap_verification() -> None:
    """Runs sitemap checks using the custom Node.js verification utility.

    This test executes the 'tools/verify-sitemaps.js' script to systematically validate
    that root sitemaps and public sitemaps are identical, sitemap URL patterns are
    well-formed, and compiled sitemap links have corresponding physical HTML assets
    inside the built 'dist/' directory.
    """
    res = subprocess.run(["node", "tools/verify-sitemaps.js"], capture_output=True, text=True, check=False)
    assert res.returncode == 0
    assert "Verification Script Completed Successfully" in res.stdout

def test_okf_compliance() -> None:
    """Runs frontmatter compliance checks using the OKF refactoring utility.

    This test executes 'tools/refactor-okf.cjs' to recursively crawl, parse, and
    validate the YAML frontmatter of all Markdown files against the strict OKF v0.1 schema.
    """
    res = subprocess.run(["node", "tools/refactor-okf.cjs"], capture_output=True, text=True, check=False)
    assert res.returncode == 0
    assert "Refactoring complete" in res.stdout

@pytest.mark.parametrize("md_file", markdown_files)
def test_page_renders_correctly(md_file: str) -> None:
    """Verifies that each markdown file successfully compiles and renders in the browser.

    Args:
        md_file (str): The filename of the markdown page to test (e.g., 'index.md').

    Raises:
        AssertionError: If the rendered page returns a non-200 HTTP status code or
            fails to contain the expected site identifying text elements.
    """
    # Determine slug based on file name
    slug = md_file[:-3]
    if slug == "index":
        url = "http://127.0.0.1:4321/"
    else:
        url = f"http://127.0.0.1:4321/{slug}/"

    response = requests.get(url, timeout=5)
    assert response.status_code == 200, f"Page {slug} failed to load."
    assert "CMSForNerd2" in response.text or "Astro" in response.text
