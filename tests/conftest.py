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
    # Kill any lingering process using port 4321 before starting
    subprocess.run(["sh", "-c", "kill $(lsof -t -i :4321) 2>/dev/null || true"], check=False)

    # Build static site assets
    subprocess.run(["npm", "run", "build"], check=True)

    # Launch preview server process in background with explicit host 0.0.0.0 and port 4321
    proc = subprocess.Popen(
        ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4321"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=os.environ.copy()
    )

    # Wait for preview server to respond on port 4321
    for _ in range(40):
        try:
            res = requests.get("http://127.0.0.1:4321/", timeout=2)
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
    subprocess.run(["sh", "-c", "kill $(lsof -t -i :4321) 2>/dev/null || true"], check=False)
