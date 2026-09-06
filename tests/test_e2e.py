"""Playwright End-to-End (E2E) browser test suite for CMSForNerd2.

Verifies dynamic theme switching (light/dark mode toggle), content page routing,
PWA service worker/manifest registration, and captures screenshot artifacts.
"""

import requests

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None  # type: ignore[assignment]


def test_theme_switching() -> None:
    """Verifies dynamic theme switching between light and dark modes."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/")

        # Click Dark mode button
        page.click("#theme-btn-dark")
        html_class = page.get_attribute("html", "class") or ""
        assert "theme-dark" in html_class, "HTML element missing 'theme-dark' class."
        theme_val = page.evaluate("localStorage.getItem('theme')")
        assert theme_val == "dark", f"Expected localStorage theme 'dark', got '{theme_val}'"

        # Click Light mode button
        page.click("#theme-btn-light")
        html_class = page.get_attribute("html", "class") or ""
        assert "theme-light" in html_class, "HTML element missing 'theme-light' class."
        theme_val = page.evaluate("localStorage.getItem('theme')")
        assert theme_val == "light", f"Expected localStorage theme 'light', got '{theme_val}'"

        browser.close()


def test_route_navigation() -> None:
    """Verifies navigation across dynamic content routes in Astro SSG."""
    test_routes = [
        "/about/",
        "/lab-manual/",
        "/pwa-architecture/",
        "/sitemap-page/",
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for route in test_routes:
            response = page.goto(f"http://127.0.0.1:4321{route}")
            assert response is not None
            assert response.status == 200, f"Route {route} failed with status {response.status}"
            assert page.title() != "", f"Page {route} is missing a title."

        # Take visual verification screenshot
        page.screenshot(path="e2e_verification.png", full_page=True)
        browser.close()


def test_pwa_manifest_and_sw() -> None:
    """Verifies PWA manifest linkage and service worker asset availability."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:4321/")

        manifest_link = page.get_attribute("link[rel='manifest']", "href")
        assert manifest_link is not None, "Missing PWA manifest link in HTML head."

        manifest_url = f"http://127.0.0.1:4321{manifest_link}"
        resp = requests.get(manifest_url, timeout=5)
        assert resp.status_code == 200, f"Failed to fetch PWA manifest from {manifest_url}"

        # Verify Service Worker asset endpoints
        sw_resp = requests.get("http://127.0.0.1:4321/sw.js", timeout=5)
        assert sw_resp.status_code == 200, "sw.js service worker script returned non-200 status code."

        reg_resp = requests.get("http://127.0.0.1:4321/registerSW.js", timeout=5)
        assert reg_resp.status_code == 200, "registerSW.js script returned non-200 status code."

        browser.close()
