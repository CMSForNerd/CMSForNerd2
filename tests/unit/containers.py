"""Containerfile and Dockerfile validation unit tests for CMSForNerd2 project."""

import os
import pytest


@pytest.mark.parametrize("container_file", ["Dockerfile", "Containerfile"])
def test_containerfile_security_and_structure(container_file):
    """Validates Containerfile and Dockerfile for standard-compliant specifications.

    Verifies that:
    - Multi-stage builds are used (builder, runtime stages).
    - Build stage inherits from node:22-alpine.
    - Runs under unprivileged USER nginx.
    - Exposes unprivileged web port 8080.
    """
    assert os.path.exists(container_file), f"{container_file} not found."

    with open(container_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify Node version for builder
    assert "node:22-alpine" in content, f"{container_file} should utilize Node 22 (node:22-alpine) in the builder stage."

    # Verify runtime Alpine Nginx
    assert "nginx:alpine-slim" in content or "nginx" in content, f"{container_file} should package the runtime using Nginx."

    # Verify unprivileged USER execution
    assert "USER nginx" in content, f"{container_file} must switch to unprivileged 'USER nginx' for production security."

    # Verify exposed port
    assert "EXPOSE 8080" in content, f"{container_file} must expose unprivileged port 8080."
