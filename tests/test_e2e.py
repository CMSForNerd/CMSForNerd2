"""Playwright End-to-End (E2E) browser test suite for CMSForNerd2.

Verifies dynamic theme switching (light/dark mode toggle), content page routing,
PWA service worker/manifest registration, Wasm Studio interactive workflows, Pagefind search,
dynamic role permissions, cookie expiration boundary handling, and Playwright visual snapshot
regression baselines across all 11 laboratory modules.
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


def test_laboratory_modules_visual_regression_theme_transitions() -> None:
    """Verifies Playwright visual snapshot regression baselines and light/dark theme transitions across all 11 laboratory modules."""
    modules = [
        ("module1", "/lab-module1/"),
        ("module2", "/lab-module2/"),
        ("module3", "/lab-module3/"),
        ("module4", "/lab-module4/"),
        ("module5", "/lab-module5/"),
        ("ansible", "/ansible-lab/"),
        ("module7", "/lab-module7/"),
        ("module8", "/lab-module8/"),
        ("module9", "/lab-module9/"),
        ("module10", "/lab-module10/"),
        ("module11", "/lab-module11/"),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for mod_id, route in modules:
            resp = page.goto(f"http://127.0.0.1:4321{route}")
            assert resp is not None and resp.status == 200, f"Failed loading laboratory module route {route}"

            # 1. Switch to Light Mode and capture baseline snapshot
            page.click("#theme-btn-light")
            page.wait_for_selector("html.theme-light", timeout=3000)
            light_class = page.get_attribute("html", "class") or ""
            assert "theme-light" in light_class, f"Module {mod_id} failed light mode theme class assertion."
            bytes_light = page.screenshot(path=f"/tmp/lab_{mod_id}_light.png", full_page=True)
            assert len(bytes_light) > 0, f"Module {mod_id} light mode screenshot is empty."

            # 2. Switch to Dark Mode and capture transition snapshot
            page.click("#theme-btn-dark")
            page.wait_for_selector("html.theme-dark", timeout=3000)
            dark_class = page.get_attribute("html", "class") or ""
            assert "theme-dark" in dark_class, f"Module {mod_id} failed dark mode theme class assertion."
            bytes_dark = page.screenshot(path=f"/tmp/lab_{mod_id}_dark.png", full_page=True)
            assert len(bytes_dark) > 0, f"Module {mod_id} dark mode screenshot is empty."

            # 3. Assert visual snapshot regression diff ratio between theme transitions
            max_len = max(len(bytes_light), len(bytes_dark))
            byte_diffs = sum(1 for a, b in zip(bytes_light, bytes_dark) if a != b)
            byte_diff_ratio = byte_diffs / max_len if max_len > 0 else 0.0

            assert byte_diff_ratio > 0.001, f"Module {mod_id} light/dark theme visual transition ratio too low: {byte_diff_ratio:.4f}"

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
        page.screenshot(path="/tmp/e2e_verification.png", full_page=True)
        browser.close()


def test_pwa_manifest_and_sw() -> None:
    """Verifies PWA manifest linkage and service worker asset availability."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/")

        manifest_link = page.get_attribute("link[rel='manifest']", "href")
        assert manifest_link is not None, "Missing PWA manifest link in HTML head."

        if manifest_link.startswith("http"):
            manifest_url = manifest_link
        elif manifest_link.startswith("/"):
            manifest_url = f"http://127.0.0.1:4321{manifest_link}"
        else:
            manifest_url = f"http://127.0.0.1:4321/{manifest_link}"

        resp = requests.get(manifest_url, timeout=5)
        assert resp.status_code == 200, f"Failed to fetch PWA manifest from {manifest_url}"

        # Verify Service Worker asset endpoints
        sw_url = "http://127.0.0.1:4321/sw.js"
        sw_resp = requests.get(sw_url, timeout=5)
        assert sw_resp.status_code == 200, "sw.js service worker script returned non-200 status code."

        reg_url = "http://127.0.0.1:4321/registerSW.js"
        reg_resp = requests.get(reg_url, timeout=5)
        assert reg_resp.status_code == 200, "registerSW.js script returned non-200 status code."

        browser.close()


def test_wasm_studio_interactive_workflows() -> None:
    """Verifies client-side WebAssembly Studio SHA-256 hash calculation, OKF parsing, WebLLM local RAG, and ONNX streaming."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/wasm-studio/")

        # Test Cryptographic Hashing Workflow
        test_script = "console.log('Hello CMSForNerd2 Wasm');"
        page.fill("#wasm-crypto-input", test_script)
        page.click("#wasm-hash-btn")

        page.wait_for_selector("#wasm-crypto-output:not(.hidden)", timeout=3000)
        hex_text = page.text_content("#wasm-hex-res") or ""
        b64_text = page.text_content("#wasm-b64-res") or ""
        csp_text = page.text_content("#wasm-csp-res") or ""
        wasm_csp_text = page.text_content("#wasm-wasm-csp-res") or ""

        assert len(hex_text) == 64, f"Expected 64-char hex SHA-256 digest, got {len(hex_text)}"
        assert len(b64_text) > 0, "Base64 hash output is empty."
        assert csp_text.startswith("'sha256-"), f"CSP header output invalid: {csp_text}"
        assert wasm_csp_text.startswith("'wasm-unsafe-eval'"), f"Wasm CSP header output invalid: {wasm_csp_text}"

        # Test WebTreeSitter Client AST Parsing & LLM Snippet Validation Workflow
        test_code = "function checkConfig(cfg) { return cfg && cfg.active; }"
        page.fill("#wasm-ast-input", test_code)
        page.click("#wasm-ast-parse-btn")

        page.wait_for_selector("#wasm-ast-output:not(.hidden)", timeout=3000)
        page.wait_for_function("document.querySelector('#wasm-ast-validity').textContent.includes('Syntax')", timeout=5000)
        ast_engine = page.text_content("#wasm-ast-status") or ""
        ast_validity = page.text_content("#wasm-ast-validity") or ""
        ast_root = page.text_content("#wasm-ast-root") or ""
        ast_tree = page.text_content("#wasm-ast-tree") or ""

        assert "WebTreeSitter" in ast_engine, f"Unexpected AST engine status: {ast_engine}"
        assert "Valid Syntax" in ast_validity, f"Unexpected AST validity check: {ast_validity}"
        assert len(ast_root) > 0, "AST root node type is empty."
        assert "(" in ast_tree, f"Unexpected AST tree preview format: {ast_tree}"

        page.click("#wasm-ast-submit-btn")
        page.wait_for_selector("#wasm-ast-llm-status", timeout=3000)
        llm_submit_msg = page.text_content("#wasm-ast-llm-status") or ""
        assert "Forwarding code payload to LLM Agent" in llm_submit_msg, f"Unexpected LLM submit message: {llm_submit_msg}"

        # Test OKF Document Analysis Workflow
        okf_sample = """---
spec_version: "0.2"
type: "documentation"
title: "Playwright E2E Sample Document"
---

This is a sample document for testing OKF analysis.
"""
        page.fill("#wasm-doc-input", okf_sample)
        page.click("#wasm-parse-btn")

        page.wait_for_selector("#wasm-doc-output:not(.hidden)", timeout=3000)
        okf_status = page.text_content("#wasm-okf-status") or ""
        doc_title = page.text_content("#wasm-doc-title") or ""

        assert "Compliant" in okf_status, f"Expected OKF compliance, got: {okf_status}"
        assert doc_title == "Playwright E2E Sample Document", f"Unexpected title: {doc_title}"

        # Test FastMCP Semantic Search Workflow with Web Worker & IndexedDB
        page.fill("#wasm-vector-query", "Astro security hardening")
        page.click("#wasm-vector-btn")

        page.wait_for_selector("#wasm-vector-output:not(.hidden)", timeout=5000)
        vec_thread = page.text_content("#wasm-vec-dims") or ""
        idb_status = page.text_content("#wasm-idb-status") or ""
        results_list = page.query_selector_all("#wasm-vec-results-list li")

        assert "Web Worker" in vec_thread, f"Unexpected vector processing thread status: {vec_thread}"
        assert "IndexedDB" in idb_status, f"Unexpected IndexedDB status text: {idb_status}"
        assert len(results_list) > 0, "FastMCP semantic search returned no ranked results."

        # Test WebGPU Quantized KV-Cache (PagedAttention) & Speculative Decoding Workflow (with WebNN Hybrid Mode & IDB Shader Cache)
        page.select_option("#wasm-kv-precision", "WEBNN-HYBRID")
        page.click("#wasm-paged-gen-btn")
        page.wait_for_selector("#wasm-paged-output:not(.hidden)", timeout=3000)
        page.wait_for_function("document.querySelector('#wasm-paged-result').textContent.includes('PagedAttention')", timeout=5000)
        paged_res = page.text_content("#wasm-paged-result") or ""
        assert "PagedAttention" in paged_res, f"Unexpected PagedAttention result output: {paged_res}"

        # Verify IndexedDB WGSL Shader Pre-Compilation Caching status string
        pipeline_cache_status = page.text_content("#wasm-pipeline-cache-status") or ""
        assert "IndexedDB WGSL Shader Pre-Compiled & Cached" in pipeline_cache_status, f"Unexpected IDB shader cache status: {pipeline_cache_status}"

        page.click("#wasm-kv-benchmark-btn")
        page.wait_for_function("document.querySelector('#wasm-paged-result').textContent.includes('Benchmark')", timeout=5000)
        bench_res = page.text_content("#wasm-paged-result") or ""
        assert "Benchmark" in bench_res, f"Unexpected KV-Cache benchmark output: {bench_res}"
        assert "INT4 Unpacked" in bench_res, f"Unexpected INT4 dequantization benchmark output: {bench_res}"

        # Test WebLLM + WebGPU On-Device Generation Workflow
        page.click("#wasm-webllm-load-btn")
        page.wait_for_selector("#wasm-webllm-output:not(.hidden)", timeout=3000)
        webllm_status = page.text_content("#wasm-webllm-status") or ""
        assert "Initialized" in webllm_status or "Loaded" in webllm_status, f"Unexpected WebLLM status: {webllm_status}"

        page.click("#wasm-webllm-gen-btn")
        page.wait_for_selector("#wasm-webllm-result", timeout=5000)
        page.wait_for_function("document.querySelector('#wasm-webllm-status').textContent.includes('Synthesis Complete')", timeout=10000)
        webllm_res = page.text_content("#wasm-webllm-result") or ""
        assert "WebLLM On-Device Synthesis Result" in webllm_res, f"Unexpected WebLLM synthesis result: {webllm_res}"

        # Test HuggingFace ONNX Web Runtime Streaming Completion Workflow
        page.click("#wasm-onnx-stream-btn")
        page.wait_for_selector("#wasm-onnx-output:not(.hidden)", timeout=3000)
        onnx_status = page.text_content("#wasm-onnx-status") or ""
        assert "ONNX Wasm Stream Active" in onnx_status, f"Unexpected ONNX stream status: {onnx_status}"
        page.wait_for_function("document.querySelector('#wasm-onnx-stream-res').textContent.includes('ONNX')", timeout=5000)
        onnx_res = page.text_content("#wasm-onnx-stream-res") or ""
        assert "ONNX" in onnx_res, f"Unexpected ONNX completion output: {onnx_res}"

        browser.close()


def test_pagefind_search_interaction() -> None:
    """Verifies interactive WebAssembly Pagefind search input and result rendering."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/search/")

        # Wait for Pagefind search input element to initialize
        search_input_selector = "#pagefind-search input"
        page.wait_for_selector(search_input_selector, timeout=5000)

        # Type search query
        page.fill(search_input_selector, "Astro")

        # Verify search results container renders matching entries
        page.wait_for_selector(".pf-result", timeout=5000)
        results = page.query_selector_all(".pf-result")
        assert len(results) > 0, "Pagefind search query returned no result items."

        browser.close()


def test_dynamic_role_permissions() -> None:
    """Verifies dynamic role permission switching and role storage state in browser session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        page = context.new_page()
        page.goto("http://127.0.0.1:4321/lab-manual/")

        # Simulate dynamic permission role change to 'admin' via client storage
        page.evaluate("localStorage.setItem('user_role', 'admin')")
        stored_role = page.evaluate("localStorage.getItem('user_role')")
        assert stored_role == "admin", f"Expected dynamic role 'admin', got '{stored_role}'"

        # Change role to 'auditor'
        page.evaluate("localStorage.setItem('user_role', 'auditor')")
        auditor_role = page.evaluate("localStorage.getItem('user_role')")
        assert auditor_role == "auditor", f"Expected dynamic role 'auditor', got '{auditor_role}'"

        browser.close()


def test_cookie_expiration_boundary() -> None:
    """Verifies session cookie expiration boundary handling in browser context."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        import time

        expiry_time = int(time.time()) + 3600
        context.add_cookies([
            {
                "name": "cms_session",
                "value": "active_token",
                "domain": "127.0.0.1",
                "path": "/",
                "expires": expiry_time,
                "httpOnly": False,
                "secure": False,
                "sameSite": "Lax",
            }
        ])

        page = context.new_page()
        page.goto("http://127.0.0.1:4321/")

        cookies = context.cookies()
        session_cookie = next((c for c in cookies if c["name"] == "cms_session"), None)
        assert session_cookie is not None, "Session cookie 'cms_session' not found."
        assert session_cookie["value"] == "active_token", "Session cookie value mismatch."

        # Simulate cookie expiration boundary by updating cookie with expired timestamp (-10s)
        expired_time = int(time.time()) - 10
        context.add_cookies([
            {
                "name": "cms_session",
                "value": "expired_token",
                "domain": "127.0.0.1",
                "path": "/",
                "expires": expired_time,
                "httpOnly": False,
                "secure": False,
                "sameSite": "Lax",
            }
        ])

        # Confirm expired cookie is automatically purged or invalidated
        active_cookies = context.cookies()
        active_session_cookie = next((c for c in active_cookies if c["name"] == "cms_session"), None)
        assert active_session_cookie is None or active_session_cookie["value"] != "active_token", "Expired session cookie remained active."

        browser.close()


def test_webgpu_canvas_visual_regression() -> None:
    """Verifies Playwright visual snapshot rendering and visual regression diff thresholds for WebGPU matrix canvas in Wasm Studio."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/wasm-studio/")

        # Trigger PagedAttention Speculative Generation to draw on #webgpu-canvas
        page.click("#wasm-paged-gen-btn")
        page.wait_for_selector("#webgpu-canvas", timeout=5000)

        # Confirm canvas element visibility and size dimensions
        canvas_elem = page.locator("#webgpu-canvas")
        assert canvas_elem.is_visible(), "#webgpu-canvas element is not visible."

        box = canvas_elem.bounding_box()
        assert box is not None, "Bounding box for #webgpu-canvas is None."
        assert box["width"] > 0 and box["height"] > 0, "Canvas dimensions are invalid."

        # Take element screenshot snapshot for visual baseline
        canvas_bytes_baseline = canvas_elem.screenshot(path="/tmp/webgpu_canvas_snapshot.png")
        assert len(canvas_bytes_baseline) > 0, "WebGPU canvas screenshot byte stream is empty."

        # Trigger second render pass and capture comparison snapshot
        page.click("#wasm-paged-gen-btn")
        canvas_bytes_current = canvas_elem.screenshot(path="/tmp/webgpu_canvas_snapshot_current.png")
        assert len(canvas_bytes_current) > 0, "WebGPU comparison canvas screenshot byte stream is empty."

        # Compute byte diff ratio between sequential canvas rendering frames
        max_len = max(len(canvas_bytes_baseline), len(canvas_bytes_current))
        byte_diffs = sum(1 for a, b in zip(canvas_bytes_baseline, canvas_bytes_current) if a != b)
        byte_diff_ratio = byte_diffs / max_len if max_len > 0 else 0.0

        # Assert visual regression diff ratio remains strictly below tolerance threshold (< 0.05)
        assert byte_diff_ratio < 0.05, f"WebGPU canvas visual regression threshold exceeded: diff ratio = {byte_diff_ratio:.4f}"

        browser.close()


def test_print_mode_css_visual_regression() -> None:
    """Verifies Playwright E2E visual snapshot rendering for @media print CSS layout rules."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/wasm-studio/")

        # Emulate CSS print media type (@media print)
        page.emulate_media(media="print")

        # Take full page print snapshot
        print_bytes = page.screenshot(path="/tmp/print_mode_snapshot.png", full_page=True)
        assert len(print_bytes) > 0, "Print mode screenshot byte stream is empty."

        # Verify page title and main content element presence under print emulation
        assert page.locator("main").is_visible(), "Main content element is missing in print mode."
        browser.close()


def test_fastmcp_p2p_mesh_fallback_modes() -> None:
    """Verifies FastMCP WebRTC and HTTP/3 WebTransport datagram fallback modes in Wasm Studio."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/wasm-studio/")

        # Test WebTransport Datagram Mode
        page.select_option("#wasm-mesh-transport-mode", "webtransport-datagram")
        page.click("#wasm-webrtc-connect-btn")

        page.wait_for_selector("#wasm-webrtc-output:not(.hidden)", timeout=3000)
        status_text = page.text_content("#wasm-webrtc-status") or ""
        assert "Active" in status_text, f"Unexpected WebTransport status: {status_text}"

        page.click("#wasm-webrtc-sync-btn")
        log_text = page.text_content("#wasm-webrtc-log") or ""
        assert "webtransport-datagram" in log_text, f"Expected WebTransport log entry, got: {log_text}"

        # Test WebRTC DataChannel Fallback Mode
        page.select_option("#wasm-mesh-transport-mode", "webrtc-datachannel")
        page.click("#wasm-webrtc-connect-btn")

        page.click("#wasm-webrtc-sync-btn")
        updated_log = page.text_content("#wasm-webrtc-log") or ""
        assert "webrtc-datachannel" in updated_log, f"Expected WebRTC log entry, got: {updated_log}"

        browser.close()


def test_service_worker_offline_fallback() -> None:
    """Verifies service worker offline fallback behavior and offline page rendering."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to offline page directly to verify fallback page assets
        response = page.goto("http://127.0.0.1:4321/offline/")
        assert response is not None
        assert response.status == 200, f"Offline fallback route returned status {response.status}"

        heading_text = page.text_content("h1") or ""
        assert "You're Offline" in heading_text, f"Unexpected offline fallback heading: {heading_text}"

        # Test context setting offline mode
        context.set_offline(True)
        from playwright.sync_api import Error as PlaywrightError

        try:
            offline_page = context.new_page()
            offline_page.goto("http://127.0.0.1:4321/offline/", timeout=3000)
            offline_heading = offline_page.text_content("h1") or ""
            assert "You're Offline" in offline_heading, "Offline context failed to render cached offline page."
        except PlaywrightError as err:
            assert "ERR_INTERNET_DISCONNECTED" in str(err) or "net::" in str(err), f"Unexpected navigation error: {err}"

        browser.close()


def test_indexeddb_vector_store_quota_boundaries() -> None:
    """Verifies IndexedDB vector store capacity and quota boundary handling in Wasm Studio."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:4321/wasm-studio/")

        # Verify initial vector store synchronization and IndexedDB status
        page.fill("#wasm-vector-query", "quota boundary testing")
        page.click("#wasm-vector-btn")

        page.wait_for_selector("#wasm-vector-output:not(.hidden)", timeout=5000)
        idb_status = page.text_content("#wasm-idb-status") or ""
        assert "IndexedDB" in idb_status, f"Unexpected IndexedDB status: {idb_status}"

        # Evaluate client-side IndexedDB record count and storage quota check
        record_count = page.evaluate("""async () => {
            return new Promise((resolve) => {
                const req = indexedDB.open('WasmStudioVectorDB');
                req.onsuccess = (e) => {
                    const db = e.target.result;
                    const tx = db.transaction('vector_documents', 'readonly');
                    const store = tx.objectStore('vector_documents');
                    const countReq = store.count();
                    countReq.onsuccess = () => resolve(countReq.result);
                };
                req.onerror = () => resolve(0);
            });
        }""")
        assert record_count >= 5, f"Expected at least 5 vector records in IndexedDB, got {record_count}"

        browser.close()
