#!/usr/bin/env python3
"""llms_txt2ctx.py

A Python CLI and API utility to parse an llms.txt file and create an XML context document
suitable for LLMs, in strict compliance with the llmstxt.org specification.

Usage (CLI):
    python3 tools/llms_txt2ctx.py llms.txt [--optional] > llms-full.txt
"""

import sys
import os
import re
import argparse

def parse_llms_txt(txt: str) -> dict:
    """Parses an llms.txt file content into a structured dictionary.

    Args:
        txt (str): Content of the llms.txt file.

    Returns:
        dict: A dictionary containing 'title', 'summary', 'info', and 'sections'.
    """
    # Clean and split into sections
    txt = txt.strip()

    # 1. Parse H1 title and summary/info block
    # Start split at first H2 heading
    parts = re.split(r'^##\s*(.*?)$', txt, flags=re.MULTILINE)
    start = parts[0].strip()

    title = ""
    summary = ""
    info = ""

    # Extract Title (H1)
    title_match = re.search(r'^#\s*(.+?)$', start, flags=re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()

    # Extract Summary (blockquote under H1)
    summary_match = re.search(r'^>\s*(.+?)$', start, flags=re.MULTILINE)
    if summary_match:
        summary = summary_match.group(1).strip()

    # Info is anything else in the start block
    # Strip H1 and blockquote lines
    info_lines = []
    for line in start.splitlines():
        trimmed = line.strip()
        if trimmed.startswith('#') or trimmed.startswith('>'):
            continue
        info_lines.append(line)
    info = "\n".join(info_lines).strip()

    # 2. Parse H2 sections
    sections = {}
    if len(parts) > 1:
        rest = parts[1:]
        # Group H2 titles and their content blocks in pairs
        for i in range(0, len(rest), 2):
            sec_title = rest[i].strip()
            sec_content = rest[i+1].strip() if i+1 < len(rest) else ""

            # Parse links in lists
            links = []
            link_pat = r'-\s*\[(?P<title>[^\]]+)\]\((?P<url>[^\)]+)\)(?::\s*(?P<desc>.*))?'
            for line in sec_content.splitlines():
                line_trimmed = line.strip()
                if not line_trimmed:
                    continue
                m = re.search(link_pat, line_trimmed)
                if m:
                    links.append(m.groupdict())
            sections[sec_title] = links

    return {
        'title': title,
        'summary': summary,
        'info': info,
        'sections': sections
    }

def create_ctx(txt: str, include_optional: bool = False) -> str:
    """Creates an XML context document for an LLM from an llms.txt string.

    Args:
        txt (str): Content of the llms.txt file.
        include_optional (bool): Whether to include the 'Optional' section.

    Returns:
        str: XML structured string.
    """
    parsed = parse_llms_txt(txt)

    xml = []
    xml.append(f'<project title="{parsed["title"]}" summary="{parsed["summary"]}">')

    if parsed["info"]:
        xml.append('<notes>')
        xml.append(parsed["info"])
        xml.append('</notes>')

    for sec_name, links in parsed["sections"].items():
        # Skip optional sections if include_optional is False
        if sec_name.lower() == 'optional' and not include_optional:
            continue

        xml.append(f'<section name="{sec_name}">')
        for link in links:
            desc_attr = f' description="{link["desc"].strip()}"' if link.get("desc") else ""
            xml.append(f'  <link title="{link["title"]}" url="{link["url"]}"{desc_attr} />')
        xml.append('</section>')

    xml.append('</project>')
    return "\n".join(xml)

def main():
    """Main CLI entrypoint.
    """
    parser = argparse.ArgumentParser(description="Parse llms.txt and create an XML context document.")
    parser.add_argument("file", help="Path to the llms.txt file")
    parser.add_argument("--optional", action="store_true", help="Include optional sections")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    xml_output = create_ctx(content, include_optional=args.optional)
    print(xml_output)

if __name__ == "__main__":
    main()
