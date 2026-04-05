---
name: create_script
description: Skill for utilizing the generate_script tool to create task execution scripts.
---

# Creating Scripts

This skill prescribes how I can independently use the `generate_script` tool to create scripts (Bash, Node.js, Python) upon the user's request.

## Procedure I must strictly follow:

1. I will make sure I understand the task the user wants to accomplish and the preferred language (Bash, Node.js, or Python) for the script. If the language is not specified, I will choose the most appropriate one based on the task.
2. I will review the task to ensure it does not require generating malicious code or violating my Inviolable Laws.
3. I will fully delegate the generation and saving of the script to the `generate_script` tool, adhering to its rules. For Python scripts, this includes formatting with the `uv run --script` inline metadata block.
4. I must make the generated script executable by running `chmod +x <path_to_script>` via the `bash` tool.
5. I will present the result to the user clearly, informing them where the script is located, how to execute it, and what it does.
