/**
 * @file refactor-okf.cjs
 * @description Node.js utility script facade delegating to the Python OKF v0.2 migration script.
 * Enforces OKF v0.2 trust signal compliance across all workspace Markdown files.
 *
 * @module tools/refactor-okf
 * @requires child_process
 */

const { execSync } = require("child_process");

/**
 * Main entry point for the OKF v0.2 refactoring facade.
 * Delegates execution to tools/migrate_okf_v02.py using uv or python3 fallback.
 *
 * @function main
 * @returns {void}
 * @throws {Error} Terminates process with status 1 if execution fails.
 */
function main() {
  console.log("Delegating OKF v0.2 frontmatter refactoring to tools/migrate_okf_v02.py...");
  try {
    execSync("uv run python tools/migrate_okf_v02.py", { stdio: "inherit" });
  } catch (_err) {
    try {
      console.log("uv not found in PATH; falling back to python3 tools/migrate_okf_v02.py...");
      execSync("python3 tools/migrate_okf_v02.py", { stdio: "inherit" });
    } catch (fallbackErr) {
      console.error("Error executing OKF v0.2 migration script:", fallbackErr);
      process.exit(1);
    }
  }
}

main();
