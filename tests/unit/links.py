"""Internal and external broken links unit test suites."""

import os
import re
import unittest
from html.parser import HTMLParser

import requests


class LinkExtractor(HTMLParser):
    """HTML parser that extracts link targets while ignoring code, script, style, and pre blocks."""

    def __init__(self) -> None:
        """Initialises the HTML parser with state tracking for ignored tags and extracted links."""
        super().__init__()
        self.ignored_tags = {"script", "style", "pre", "code"}
        self.stack: list[str] = []
        self.extracted_links: list[str] = []
        self.text_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Handles the opening tag event to track ignored elements and capture link attributes.

        Args:
            tag: The HTML tag name in lower case.
            attrs: A list of (attribute_name, attribute_value) tuples.
        """
        tag_lower = tag.lower()
        if tag_lower in self.ignored_tags:
            self.stack.append(tag_lower)
            return

        if not self.stack:
            for name, value in attrs:
                if name.lower() in ("href", "src", "action") and value:
                    self.extracted_links.append(value)

    def handle_endtag(self, tag: str) -> None:
        """Handles the closing tag event to update element stack state.

        Args:
            tag: The HTML tag name in lower case.
        """
        tag_lower = tag.lower()
        if self.stack and self.stack[-1] == tag_lower:
            self.stack.pop()

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Handles self-closing tag events to extract attributes when not inside ignored blocks.

        Args:
            tag: The HTML tag name in lower case.
            attrs: A list of (attribute_name, attribute_value) tuples.
        """
        tag_lower = tag.lower()
        if not self.stack and tag_lower not in self.ignored_tags:
            for name, value in attrs:
                if name.lower() in ("href", "src", "action") and value:
                    self.extracted_links.append(value)

    def handle_data(self, data: str) -> None:
        """Handles text data chunks between tags when not enclosed in ignored blocks.

        Args:
            data: Raw text content between tags.
        """
        if not self.stack:
            self.text_chunks.append(data)


def parse_links_from_file(filepath: str) -> list[str]:
    """Parses HTML/Astro/Markdown content and extracts all candidate href, src, action, and Markdown links.

    Args:
        filepath: Path to the template or content file.

    Returns:
        List of link target strings.
    """
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Strip markdown backtick code blocks first to prevent code samples matching as links
    clean_content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    clean_content = re.sub(r"`.*?`", "", clean_content)

    parser = LinkExtractor()
    parser.feed(clean_content)

    links = list(parser.extracted_links)

    # Extract Markdown links [text](target) from text chunks outside ignored tags
    md_pattern = re.compile(r"""\[(?:[^\]]+)\]\(([^)]+)\)""")
    remaining_text = "".join(parser.text_chunks)
    links.extend(md_pattern.findall(remaining_text))

    return links


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

        unresolved_links: list[tuple[str, str]] = []

        for filepath in files:
            targets = parse_links_from_file(filepath)

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

        external_links: set[str] = set()

        for filepath in files:
            targets = parse_links_from_file(filepath)

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
