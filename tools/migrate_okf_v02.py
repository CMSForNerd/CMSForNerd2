#!/usr/bin/env python3
"""OKF v0.2 Migration and Refactoring Utility.

Deeply scans all Markdown (.md) files across the project workspace, migrates legacy
OKF v0.1 frontmatter to OKF v0.2 standard (`spec_version: "0.2"`), populates the five trust
and freshness pillars (`status`, `stale_after`, `sources`, `generated`), wraps special character
strings in double quotes, and invokes markdownlint for Workspace Quality Enforcement.
"""

from pathlib import Path
import subprocess
import yaml

EXCLUDE_DIRS = {"node_modules", ".git", "dist", ".astro", ".pytest_cache"}

def get_markdown_files(root_dir: Path) -> list[Path]:
    """Finds all markdown files in the workspace excluding build and node directories."""
    md_files: list[Path] = []
    for path in root_dir.rglob("*.md"):
        if not any(excluded in path.parts for excluded in EXCLUDE_DIRS):
            md_files.append(path)
    return md_files


def migrate_file(filepath: Path) -> bool:
    """Migrates a single markdown file to OKF v0.2 compliance. Returns True if modified."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    # Check if frontmatter exists starting on line 1, column 1
    if not content.startswith("---"):
        print(f"Adding OKF v0.2 frontmatter to {filepath}")
        stem = filepath.stem.replace("-", " ").replace("_", " ").title()
        frontmatter = f'---\nspec_version: "0.2"\ntype: "documentation"\ntitle: "{stem}"\nstatus: "stable"\nstale_after: "2027-03-06"\nsources:\n  - id: "workspace_root"\n    title: "{filepath.name}"\n    url: "{filepath.name}"\ngenerated:\n  by: "Repository Architect & OKF v0.2 Migration Agent"\n  timestamp: "2026-09-06T23:00:00Z"\ntags: ["documentation"]\n---\n\n'
        filepath.write_text(frontmatter + content, encoding="utf-8")
        return True

    end_idx = content.find("---", 3)
    if end_idx == -1:
        print(f"Unclosed frontmatter in {filepath}")
        return False

    fm_raw = content[3:end_idx].strip()
    body_text = content[end_idx + 3:]

    try:
        fm_data = yaml.safe_load(fm_raw)
    except yaml.YAMLError as e:
        print(f"Invalid YAML in {filepath}: {e}")
        return False

    if not isinstance(fm_data, dict):
        fm_data = {}

    # 1. Enforce spec_version: "0.2"
    if fm_data.get("spec_version") != "0.2":
        fm_data["spec_version"] = "0.2"
        if "okf_version" in fm_data:
            del fm_data["okf_version"]
        if "okf-version" in fm_data:
            del fm_data["okf-version"]

    # 2. Enforce type & title
    if "type" not in fm_data or not fm_data["type"]:
        if "src/content/pages" in str(filepath):
            fm_data["type"] = "content_page"
        elif ".agents/skills" in str(filepath) or "skills/" in str(filepath):
            fm_data["type"] = "skill"
        else:
            fm_data["type"] = "documentation"

    if "title" not in fm_data or not fm_data["title"]:
        fm_data["title"] = filepath.stem.replace("-", " ").replace("_", " ").title()

    # 3. Enforce Trust & Freshness Pillars (status, stale_after, sources, generated)
    if "status" not in fm_data:
        fm_data["status"] = "stable"

    if "stale_after" not in fm_data:
        fm_data["stale_after"] = "2027-03-06"

    if "sources" not in fm_data or not fm_data["sources"]:
        fm_data["sources"] = [{
            "id": "workspace_file",
            "title": filepath.name,
            "url": str(filepath)
        }]

    if "generated" not in fm_data or not fm_data["generated"]:
        timestamp_val = fm_data.get("timestamp", "2026-09-06T23:00:00Z")
        if isinstance(timestamp_val, str) and not timestamp_val.endswith("Z"):
            timestamp_val = "2026-09-06T23:00:00Z"
        fm_data["generated"] = {
            "by": "Repository Architect & OKF v0.2 Compliance Agent",
            "timestamp": str(timestamp_val)
        }

    # 4. Handle topics / tags alignment
    if "topics" in fm_data and "tags" not in fm_data:
        fm_data["tags"] = fm_data["topics"]
    elif "tags" in fm_data and "topics" not in fm_data:
        fm_data["topics"] = fm_data["tags"]
    elif "topics" not in fm_data and "tags" not in fm_data:
        fm_data["tags"] = ["documentation"]
        fm_data["topics"] = ["documentation"]

    # Clean legacy timestamp if superseded by generated
    if "timestamp" in fm_data:
        del fm_data["timestamp"]

    # Re-serialize frontmatter cleanly
    yaml_lines = ["---"]
    for k, v in fm_data.items():
        if k == "spec_version":
            yaml_lines.append('spec_version: "0.2"')
        elif isinstance(v, (dict, list)):
            dumped = yaml.safe_dump({k: v}, sort_keys=False).strip()
            yaml_lines.append(dumped)
        elif isinstance(v, bool):
            yaml_lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, (int, float)):
            yaml_lines.append(f"{k}: {v}")
        else:
            val_str = str(v)
            # Quote if contains special characters
            if any(c in val_str for c in ["🎨", "🧠", "🚀", "🧪", "📋", "🏗️", "🧱", ":", "[", "]", "#", "@", "{", "}", "%"]):
                escaped = val_str.replace('"', '\\"')
                yaml_lines.append(f'{k}: "{escaped}"')
            else:
                yaml_lines.append(f'{k}: "{val_str}"')
    yaml_lines.append("---")

    new_fm = "\n".join(yaml_lines)
    new_content = new_fm + body_text

    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
        print(f"Migrated {filepath} to OKF v0.2")
        return True

    return False


def run_markdownlint(files: list[Path]) -> None:
    """Invokes markdownlint-cli if available to enforce style formatting."""
    print("Executing Workspace Quality Enforcement via markdownlint-cli...")
    file_args = [str(f) for f in files]
    cmd = ["npx", "--no-install", "markdownlint-cli", "--fix"] + file_args
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("markdownlint passed cleanly.")
    else:
        print(f"markdownlint output: {res.stdout}\n{res.stderr}")


def main() -> None:
    root = Path(".")
    md_files = get_markdown_files(root)
    print(f"Found {len(md_files)} markdown files in workspace.")

    migrated_count = 0
    for f in md_files:
        if migrate_file(f):
            migrated_count += 1

    print(f"OKF v0.2 migration complete. Total modified files: {migrated_count}")
    run_markdownlint(md_files)


if __name__ == "__main__":
    main()
