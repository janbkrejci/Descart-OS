---
name: script_dependencies
description: Critical rule for writing Python and Node.js scripts regarding automatic dependency installation.
---

# Script Dependencies Rule

Whenever I generate or write Python or Node.js scripts, I must ensure that these scripts are designed to **automatically install any missing dependencies themselves** before execution.

## Python Scripts
For Python scripts, I must use the `uv` tool for automatic dependency management. The script must:
1. Start with the `uv run --script` shebang and inline metadata block:
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["<insert_dependencies_here>"]
   # ///
   ```
2. Be made executable via `chmod +x <script_path>`.

## Node.js Scripts
For Node.js scripts:
1. The script must check if `pnpm` is available on the system.
2. If `pnpm` is available, it must use `pnpm install` or `pnpm add` to install missing dependencies.
3. If `pnpm` is not available, it must fall back to using `npm`.
4. This logic can be embedded in a shell script wrapper or directly in JS using `child_process`.
