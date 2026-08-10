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
    # Run the existing sitemap verify utility
    res = subprocess.run(["node", "tools/verify-sitemaps.js"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Verification Script Completed Successfully" in res.stdout

def test_okf_compliance():
    # Run the refactor/verify okf utility
    res = subprocess.run(["node", "tools/refactor-okf.cjs"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Refactoring complete" in res.stdout

@pytest.mark.parametrize("md_file", markdown_files)
def test_page_renders_correctly(md_file):
    # Determine slug based on file name
    slug = md_file[:-3]
    if slug == "index":
        url = "http://localhost:4321/"
    else:
        url = f"http://localhost:4321/{slug}/"

    response = requests.get(url, timeout=5)
    assert response.status_code == 200, f"Page {slug} failed to load."
    assert "CMSForNerd2" in response.text or "Astro" in response.text
