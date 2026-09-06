"""Pytest configuration and shared fixtures for CMSForNerd2 test suite."""

import os
import signal
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
    # Force base path to '/' for test session execution to ensure consistent root preview serving across environments
    env = os.environ.copy()
    env["GITHUB_ACTIONS"] = "false"

    # Build static site assets
    subprocess.run(["npm", "run", "build"], env=env, check=True)

    # Launch preview server process in its own process group (start_new_session=True)
    proc = subprocess.Popen(
        ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4321"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
        start_new_session=True,
    )

    # Wait for preview server to respond on port 4321
    for _ in range(120):
        try:
            res = requests.get("http://127.0.0.1:4321/", timeout=2)
            if res.status_code == 200:
                break
        except requests.RequestException:
            pass
        time.sleep(0.5)
    else:
        if proc.poll() is None:
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            except OSError:
                pass
        raise RuntimeError("Preview server did not start on port 4321")

    yield

    # Cleanly terminate preview server process group at session teardown
    if proc.poll() is None:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            proc.wait(timeout=5)
        except (subprocess.TimeoutExpired, OSError):
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            except OSError:
                pass
