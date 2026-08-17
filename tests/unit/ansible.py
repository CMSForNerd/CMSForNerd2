"""Ansible playbook validation unit tests for CMSForNerd2 project."""

import os
import yaml


def test_ansible_playbook_compliance():
    """Validates deploy-static.yml for ansible-lint and dual-pathway compliance.

    Verifies that:
    - The playbook is well-formed YAML.
    - All tasks use Fully Qualified Collection Names (FQCN).
    - The playbook contains dual-pathway branching variables (is_limited_environment).
    - Idempotency is supported via changed_when parameters on commands.
    """
    playbook_path = "deploy-static.yml"
    assert os.path.exists(playbook_path), "Ansible playbook deploy-static.yml not found."

    with open(playbook_path, "r", encoding="utf-8") as f:
        playbook_data = yaml.safe_load(f)

    assert isinstance(playbook_data, list), "Playbook root must be a list of plays."
    play = playbook_data[0]

    # Check for gather_facts
    assert play.get("gather_facts") is True, "gather_facts should be true."

    # Check for is_limited_environment variable detection task
    tasks = play.get("tasks", [])
    assert len(tasks) > 0, "Playbook has no tasks defined."

    has_detection_task = False
    for task in tasks:
        # Check module FQCN
        for key in task.keys():
            # Skip common task meta-parameters
            if key in ["name", "become", "when", "tags", "vars", "args", "changed_when"]:
                continue
            # Ensure the module key has FQCN structure
            assert "." in key, f"Task '{task.get('name')}' uses non-FQCN action/module: '{key}'"

        # Check for user-detection set_fact task
        if task.get("ansible.builtin.set_fact") and "is_limited_environment" in task.get("ansible.builtin.set_fact", {}):
            has_detection_task = True

        # Check command idempotency
        if task.get("ansible.builtin.command"):
            assert "changed_when" in task, f"Command task '{task.get('name')}' is missing 'changed_when' attribute."

    assert has_detection_task, "Playbook does not define the dual-pathway user detection set_fact task."
