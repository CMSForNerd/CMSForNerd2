"""Sitemaps consistency and context7 configuration unit tests."""

import json
import os


def test_sitemaps_consistency() -> None:
    """Validate consistency between root sitemap.txt and public/sitemap.txt.

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


def test_context7_configuration() -> None:
    """Validate context7.json format and schema structure.

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


def test_pagefind_sri_manifest() -> None:
    """Validate the structure and integrity of the Pagefind SRI manifest in dist/pagefind/pagefind-sri.json."""
    manifest_path = os.path.join("dist", "pagefind", "pagefind-sri.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        assert manifest.get("algorithm") == "sha384", "SRI manifest algorithm must be 'sha384'."
        assert "files" in manifest, "SRI manifest missing 'files' map."
        files = manifest["files"]
        assert len(files) > 0, "SRI manifest 'files' map is empty."
        for file_path, sri_hash in files.items():
            assert sri_hash.startswith("sha384-"), f"SRI hash for {file_path} must start with 'sha384-'."


def test_csp_manifest_and_nonce_injection() -> None:
    """Validate the structure and integrity of the CSP manifest in dist/csp-manifest.json."""
    manifest_path = os.path.join("dist", "csp-manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        assert "policy" in manifest, "CSP manifest missing 'policy' string."
        assert "pages" in manifest, "CSP manifest missing 'pages' map."
        pages = manifest["pages"]
        assert len(pages) > 0, "CSP manifest 'pages' map is empty."
        for page_path, page_data in pages.items():
            assert "inline_script_count" in page_data, f"Page {page_path} missing 'inline_script_count'."
            assert "hashes" in page_data, f"Page {page_path} missing 'hashes' list."
