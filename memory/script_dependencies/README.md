---
name: script_dependencies
description: Critical rule for writing Python and Node.js scripts regarding automatic dependency installation.
---

# Script Dependencies Rule

Whenever I generate or write Python or Node.js scripts, I must ensure that these scripts are designed to **automatically install any missing dependencies themselves** before execution.

## Python Scripts
For Python scripts:
1. The script must create a virtual environment (venv) if it doesn't already exist.
2. The script must use this virtual environment to install dependencies via `pip`.
3. The script must execute the main logic using the python executable from the virtual environment, or it can be a bash wrapper that sets up the venv, installs dependencies, and then runs the python script. Alternatively, the python script itself can check for modules and if missing, invoke `subprocess` to create a venv, install modules, and re-execute itself within the venv. 
*(A bash wrapper or a setup function inside the script is recommended).*
4. Do not forget to add a .gitignore file near the script so that the virtual environment files are not committed do the repository.

## Node.js Scripts
For Node.js scripts:
1. The script must check if `pnpm` is available on the system.
2. If `pnpm` is available, it must use `pnpm install` or `pnpm add` to install missing dependencies.
3. If `pnpm` is not available, it must fall back to using `npm`.
4. This logic can be embedded in a shell script wrapper or directly in JS using `child_process`.
