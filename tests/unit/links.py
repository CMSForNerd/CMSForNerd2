"""Internal and external broken links unit test suites."""

import os
import re
import unittest

import requests


class InternalBrokenLinksTest(unittest.TestCase):
    """Unit test suite for validating internal relative links across project files."""

    def test_internal_links_exist(self) -> None:
        """Validates that all internal relative links in template and content files exist on disk."""
        target_extensions = (".astro", ".html", ".md", ".mdx", ".ts", ".tsx", ".json")
        excluded_dirs = {"node_modules", ".git", ".astro", "dist", ".pytest_cache", ".venv"}

        files: list[str] = []
        for root, dirs, fnames in os.walk("."):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for fname in fnames:
                if fname.endswith(target_extensions):
                    files.append(os.path.join(root, fname))

        self.assertTrue(len(files) > 0, "No template or content files found to scan for internal links.")

        href_pattern = re.compile(r"""(?:href|src|action)=["\x27]([^"\x27]+)["\x27]""", re.IGNORECASE)
        md_pattern = re.compile(r"""\[(?:[^\]]+)\]\(([^)]+)\)""")

        unresolved_links: list[tuple[str, str]] = []

        for filepath in files:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Strip script, style, pre, and code blocks to prevent code samples and logic matching as links
            clean_content = re.sub(r"<script.*?>.*?</script>", "", content, flags=re.DOTALL | re.IGNORECASE)
            clean_content = re.sub(r"<style.*?>.*?</style>", "", clean_content, flags=re.DOTALL | re.IGNORECASE)
            clean_content = re.sub(r"<pre.*?>.*?</pre>", "", clean_content, flags=re.DOTALL | re.IGNORECASE)
            clean_content = re.sub(r"<code.*?>.*?</code>", "", clean_content, flags=re.DOTALL | re.IGNORECASE)
            clean_content = re.sub(r"```.*?```", "", clean_content, flags=re.DOTALL)
            clean_content = re.sub(r"`.*?`", "", clean_content)

            targets = href_pattern.findall(clean_content) + md_pattern.findall(clean_content)

            for link in targets:
                link = link.strip()

                # Filter out anchors, mailto, javascript, dynamic expressions, and external URLs
                if not link or link.startswith(("#", "mailto:", "javascript:")):
                    continue
                if "{" in link or "}" in link or "$" in link or "import.meta" in link:
                    continue
                if link.startswith(("http://", "https://", "//")):
                    continue

                # Remove query parameters and fragment anchors
                target = link.split("#")[0].split("?")[0].strip()
                if not target:
                    continue

                source_dir = os.path.dirname(filepath)
                clean_target = target.lstrip("/")

                # Generate path candidate locations on disk
                candidates = [
                    os.path.join(source_dir, target),
                    os.path.join(source_dir, target + ".md"),
                    os.path.join(source_dir, target + ".astro"),
                    os.path.join(source_dir, target, "index.md"),
                    os.path.join(source_dir, target, "index.astro"),
                    os.path.join(source_dir, target, "index.html"),
                    target,
                    target + ".md",
                    clean_target,
                    clean_target + ".md",
                    os.path.join("public", clean_target),
                    os.path.join("dist", clean_target),
                    os.path.join("src", clean_target),
                    os.path.join("src/content/pages", clean_target + ".md"),
                    os.path.join("src/pages", clean_target + ".astro"),
                    os.path.join("src/pages", clean_target + ".ts"),
                    os.path.join("src/pages", clean_target + ".xml.ts"),
                    os.path.join("src/pages/[...slug]", clean_target + ".astro"),
                    os.path.join("docs", clean_target),
                    os.path.join("docs", clean_target + ".md"),
                    os.path.join("docs", clean_target, "index.md"),
                ]

                # Special route candidates (e.g. amp routes, root index)
                if clean_target in ("amp", "amp/"):
                    candidates.append("src/pages/[...slug]/amp.astro")
                elif clean_target == "":
                    candidates.append("src/pages/[...slug].astro")

                if not any(os.path.exists(c) for c in candidates):
                    unresolved_links.append((filepath, link))

        failure_msg = "Broken internal links detected:\n" + "\n".join(
            f"  File: {src_f} -> Linked Target: {target}" for src_f, target in unresolved_links
        )
        self.assertEqual(len(unresolved_links), 0, failure_msg)


class ExternalBrokenLinksTest(unittest.TestCase):
    """Unit test suite for validating external HTTP/HTTPS site references."""

    def test_external_links_accessible(self) -> None:
        """Validates that external HTTP/HTTPS links in template files respond successfully and are not broken."""
        target_extensions = (".astro", ".html", ".md", ".mdx", ".ts", ".tsx", ".json")
        excluded_dirs = {"node_modules", ".git", ".astro", "dist", ".pytest_cache", ".venv"}

        files: list[str] = []
        for root, dirs, fnames in os.walk("."):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for fname in fnames:
                if fname.endswith(target_extensions):
                    files.append(os.path.join(root, fname))

        self.assertTrue(len(files) > 0, "No template or content files found to scan for external links.")

        href_pattern = re.compile(r"""(?:href|src)=["\x27]([^"\x27]+)["\x27]""", re.IGNORECASE)
        md_pattern = re.compile(r"""\[(?:[^\]]+)\]\(([^)]+)\)""")

        external_links: set[str] = set()

        for filepath in files:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            targets = href_pattern.findall(content) + md_pattern.findall(content)

            for link in targets:
                link = link.strip()
                if link.startswith("//"):
                    link = "https:" + link
                if link.startswith(("http://", "https://")):
                    external_links.add(link)

        security_payload_patterns = ["evil.com", "example.com", "example.org", "localhost", "127.0.0.1"]
        headers = {"User-Agent": "Mozilla/5.0 (CMSForNerd2 Link Checker)"}

        broken_links: list[tuple[str, str]] = []

        for link in sorted(external_links):
            if any(payload in link for payload in security_payload_patterns):
                continue

            try:
                # Attempt HTTP HEAD request first
                res = requests.head(link, headers=headers, timeout=5, allow_redirects=True)
                if res.status_code in (404, 405, 403):
                    # Fallback to streaming HTTP GET if HEAD is rejected or forbidden
                    res = requests.get(link, headers=headers, timeout=5, allow_redirects=True, stream=True)

                # Consider HTTP 404 or 410 as broken, except CDN domain origins (e.g., dns-prefetch targets without path)
                if res.status_code in (404, 410):
                    # Check if origin-only domain (e.g. https://cdn.ampproject.org) from preconnect/dns-prefetch
                    path = link.split("://", 1)[-1].split("/", 1)
                    if len(path) == 1 or not path[1]:
                        # Origin-only domain prefetch target: verify reachable host via GET options or HEAD
                        continue
                    broken_links.append((link, f"HTTP {res.status_code}"))

            except requests.RequestException as e:
                broken_links.append((link, f"Connection Failure: {type(e).__name__}"))

        failure_msg = "Broken external links detected:\n" + "\n".join(
            f"  URL: {url} -> Reason: {reason}" for url, reason in broken_links
        )
        self.assertEqual(len(broken_links), 0, failure_msg)
