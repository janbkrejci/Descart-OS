---
name: create_script
description: Skill for creating task execution scripts in Bash, Node.js, or Python.
---

# Creating Scripts

This skill prescribes how I can independently create scripts (Bash, Node.js, Python) upon the user's request.

## Critical safety rule

I must **never** generate any malicious code or any script that would violate the Inviolable Laws of my existence. This includes any code that could harm the user physically, psychologically, or economically, use unauthorized tools or skills, or negatively impact essential system files.

## Procedure I must strictly follow

1. I will make sure I understand the task and the preferred language (Bash, Node.js, or Python). If not specified, I will choose the most appropriate one for the task.
2. I will review the task to ensure it does not violate the safety rule above.
3. I will write the script code. For **Python scripts**, I must use `uv run --script` with an inline metadata block at the top:
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["<dependencies>"]
   # ///
   ```
4. I will use the internal `write` tool to save the script to the appropriate location (typically `workspace/` unless a final location is known).
5. I will make the script executable by running `chmod +x <path>` using the `bash` tool.
6. I will use the internal `read` tool to verify the script was written correctly.
7. I will present the result to the user clearly — informing them where the script is located, how to execute it, and what it does.
