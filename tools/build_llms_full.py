#!/usr/bin/env python3
"""build_llms_full.py

This module contains the automation utility for generating the consolidated llms-full.txt file.
It parses markdown link targets defined in llms.txt, resolves them to physical files in the
workspace, and appends their entire contents under a unified structure for LLM ingestion.
"""

import os
import re

def main() -> None:
    """Main execution handler to compile and format llms-full.txt.

    This function reads reference targets from the plain-text llms.txt, crawls
    corresponding files across the docs/ directory and workspace root, consolidates
    the content sections with clear Markdown dividers, and writes the output file.

    Returns:
        None
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    llms_txt_path = os.path.join(root_dir, "llms.txt")
    llms_full_path = os.path.join(root_dir, "llms-full.txt")

    if not os.path.exists(llms_txt_path):
        print("Error: llms.txt not found.")
        return

    with open(llms_txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract unique Markdown link targets in a single O(N) pass with set-based deduplication
    link_pat = r'\[(?P<title>[^\]]+)\]\((?P<url>[^\)]+\.md)\)'
    unique_urls = []
    seen = set()

    for line in content.splitlines():
        for m in re.finditer(link_pat, line):
            target_url = m.group('url')
            if target_url not in seen:
                seen.add(target_url)
                unique_urls.append(target_url)

    print(f"Found {len(unique_urls)} markdown files to consolidate.")

    full_text = []
    full_text.append("# CMSForNerd2 Complete Documentation (llms-full.txt)")
    full_text.append("\n> This single document consolidates the entire documentation suite for CMSForNerd2.")
    full_text.append("\n---\n")

    for url in unique_urls:
        file_path = os.path.join(root_dir, url)
        if not os.path.exists(file_path):
            print(f"Warning: Linked file '{url}' does not exist.")
            continue

        print(f"Processing: {url}")
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

        # Clean YAML frontmatter if desired, but keeping it is good for agent parsing!
        # Let's clean up any excessive trailing lines
        file_content = file_content.strip()

        full_text.append(f"## File: {url}")
        full_text.append("\n")
        full_text.append(file_content)
        full_text.append("\n\n---\n")

    # Append the standard footer
    full_text.append("""
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-01*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
""")

    with open(llms_full_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_text))

    print(f"Successfully compiled: llms-full.txt")

if __name__ == "__main__":
    main()
