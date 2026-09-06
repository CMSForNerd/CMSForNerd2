"""Pytest configuration and shared fixtures for CMSForNerd2 test suite."""

import os
import subprocess
import time
from collections.abc import Generator

import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def preview_server() -> Generator[None, None, None]:
    """Compiles the Astro static site and manages the preview web server on port 4321.

    Executes 'npm run build' once per test session, launches 'npm run preview',
    waits for HTTP 200 on port 4321, and gracefully terminates the server process
    after all test modules complete.
    """
    # Build static site assets
    subprocess.run(["npm", "run", "build"], check=True)

    # Launch preview server process in background
    proc = subprocess.Popen(
        ["npm", "run", "preview"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=os.environ.copy()
    )

    # Wait for preview server to respond on port 4321
    for _ in range(30):
        try:
            res = requests.get("http://localhost:4321/", timeout=2)
            if res.status_code == 200:
                break
        except requests.RequestException:
            pass
        time.sleep(0.5)
    else:
        proc.kill()
        raise RuntimeError("Preview server did not start on port 4321")

    yield

    # Cleanly terminate preview server at session teardown
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
