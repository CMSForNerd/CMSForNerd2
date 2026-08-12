"""Integration test suite for the CMSForNerd2 static modernisation project.

This module provides automated end-to-end integration tests to verify the correctness
of sitemaps, frontmatter OKF (Open Knowledge Format) v0.1 compliance, and the HTML
rendering of all migrated markdown content pages within the Astro 7.1 SSG framework.
"""

import os
import subprocess
import time
import requests
import pytest

# Find all markdown files in src/content/pages/
CONTENT_DIR = "src/content/pages"
markdown_files = [f for f in os.listdir(CONTENT_DIR) if f.endswith(".md")]

@pytest.fixture(scope="session", autouse=True)
def run_server():
    """Builds the Astro static site and launches the local preview web server.

    This fixture executes 'npm run build' to compile all static pages, starts
    the Astro preview server in a background process, waits for the server
    to become responsive on port 4321, and gracefully terminates the server
    after the test session completes.

    Yields:
        None: Control is yielded to the active test session.

    Raises:
        RuntimeError: If the Astro preview server fails to start or become
            responsive within the allotted timeout period.
    """
    # Ensure project is built
    subprocess.run(["npm", "run", "build"], check=True)

    # Start the preview server in the background on port 4321
    proc = subprocess.Popen(["npm", "run", "preview"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for the server to be up
    for _ in range(30):
        try:
            res = requests.get("http://localhost:4321/", timeout=2)
            if res.status_code == 200:
                break
        except requests.RequestException:
            pass
        time.sleep(0.5)
    else:
        proc.kill()
        raise RuntimeError("Preview server did not start on port 4321")

    yield

    # Kill the preview server
    proc.terminate()
    proc.wait()

def test_sitemap_verification():
    """Runs sitemap checks using the custom Node.js verification utility.

    This test executes the 'tools/verify-sitemaps.js' script to systematically validate
    that root sitemaps and public sitemaps are identical, sitemap URL patterns are
    well-formed, and compiled sitemap links have corresponding physical HTML assets
    inside the built 'dist/' directory.
    """
    res = subprocess.run(["node", "tools/verify-sitemaps.js"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Verification Script Completed Successfully" in res.stdout

def test_okf_compliance():
    """Runs frontmatter compliance checks using the OKF refactoring utility.

    This test executes 'tools/refactor-okf.cjs' to recursively crawl, parse, and
    validate the YAML frontmatter of all Markdown files against the strict OKF v0.1 schema.
    """
    res = subprocess.run(["node", "tools/refactor-okf.cjs"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Refactoring complete" in res.stdout

@pytest.mark.parametrize("md_file", markdown_files)
def test_page_renders_correctly(md_file):
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
        url = "http://localhost:4321/"
    else:
        url = f"http://localhost:4321/{slug}/"

    response = requests.get(url, timeout=5)
    assert response.status_code == 200, f"Page {slug} failed to load."
    assert "CMSForNerd2" in response.text or "Astro" in response.text
