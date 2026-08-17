"""Sitemaps consistency and context7 configuration unit tests."""

import os
import json


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
