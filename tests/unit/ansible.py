"""Ansible playbook validation unit tests for CMSForNerd2 project.

Verifies compliance with:
- Rule 32.43: Automated Playbook Validation Ladder & Idempotence Assertion
- Rule 32.44: Ansible Community AI-Forge & Red Hat CoP Standard
"""

import os
from typing import Any

import yaml


def _validate_playbook_tasks(tasks: list[dict[str, Any]], playbook_name: str) -> bool:
    """Validate tasks in a play for FQCN, idempotency parameters, and task naming.

    Args:
        tasks: List of task dictionaries in a play.
        playbook_name: Filename of the playbook being validated.

    Returns:
        bool: True if limited environment detection task is present.
    """
    has_detection_task = False

    for task in tasks:
        # Ignore block / rescue constructs meta keys
        if "block" in task:
            if _validate_playbook_tasks(task["block"], playbook_name):
                has_detection_task = True
            continue

        # Check module FQCN
        for key in task:
            if key in ["name", "become", "when", "tags", "vars", "args", "changed_when", "failed_when", "register", "run_once", "environment"]:
                continue
            assert "." in key, f"Task '{task.get('name')}' in '{playbook_name}' uses non-FQCN action/module: '{key}'"

        # Check for user-detection set_fact task
        set_fact_data = task.get("ansible.builtin.set_fact")
        if isinstance(set_fact_data, dict) and "is_limited_environment" in set_fact_data:
            has_detection_task = True

        # Check command/shell task idempotency guard (Rule 32.43 Fast-Fail Gate)
        if task.get("ansible.builtin.command") or task.get("ansible.builtin.shell"):
            assert "changed_when" in task or "creates" in task or "removes" in task, (
                f"Command/shell task '{task.get('name')}' in '{playbook_name}' is missing 'changed_when' attribute."
            )

        # Check imperative task naming (Rule 32.44)
        task_name = task.get("name", "")
        assert isinstance(task_name, str) and len(task_name) > 0, f"Task in '{playbook_name}' is missing a descriptive name."

    return has_detection_task


def test_ansible_playbook_compliance() -> None:
    """Validate deploy-static.yml and playbooks/ for Rule 32.43 and Rule 32.44 compliance.

    Verifies that:
    - All playbook files use .yml extension.
    - All playbooks are well-formed YAML.
    - All tasks use Fully Qualified Collection Names (FQCN).
    - All command/shell tasks contain idempotency guards (changed_when).
    - Dual-pathway branching logic (is_limited_environment) is implemented.

    Raises:
        AssertionError: If any playbook structure, FQCN, or idempotency check fails.
    """
    playbooks_to_test = [
        "deploy-static.yml",
        "playbooks/install.yml",
        "playbooks/opentofu.yml",
        "playbooks/configure.yml",
        "playbooks/deploy.yml",
        "playbooks/monitor.yml",
        "playbooks/site.yml",
    ]

    for playbook_path in playbooks_to_test:
        assert os.path.exists(playbook_path), f"Ansible playbook '{playbook_path}' not found."
        assert playbook_path.endswith(".yml"), f"Playbook '{playbook_path}' must use .yml extension (Rule 32.44)."

        with open(playbook_path, "r", encoding="utf-8") as f:
            playbook_data = yaml.safe_load(f)

        assert isinstance(playbook_data, list), f"Playbook '{playbook_path}' root must be a list."

        # Handle master orchestrator playbooks importing other playbooks
        if playbook_path == "playbooks/site.yml":
            for play in playbook_data:
                assert "ansible.builtin.import_playbook" in play, "Master site.yml must import playbooks via FQCN."
            continue

        play = playbook_data[0]
        assert play.get("gather_facts") is True, f"gather_facts should be true in '{playbook_path}'."

        tasks = play.get("tasks", [])
        assert len(tasks) > 0, f"Playbook '{playbook_path}' has no tasks defined."

        has_detection_task = _validate_playbook_tasks(tasks, playbook_path)
        assert has_detection_task, f"Playbook '{playbook_path}' does not define the dual-pathway user detection set_fact task."
