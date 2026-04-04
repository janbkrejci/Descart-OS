---
name: init_context
description: Tool for gathering and formatting all mandatory files and directory frontmatters into a single output for session initialization.
---

# Initialize Context Tool

This tool is a Python script (`init_context.py`) designed to efficiently read all required system documents (`agent/README.md`, `user/README.md`, `knowledge/README.md`, `memory/README.md`, `skills/README.md`, `tools/README.md`, `workspace/README.md`) and collect the YAML frontmatters from all subdirectories in `knowledge/`, `memory/`, `skills/`, and `tools/`.

## Procedure I must strictly follow:

1. Use the `bash` tool to run `python3 tools/init_context/init_context.py`. If the command fails, stop any further processing, inform the user about the problem and suggest a remedy.
2. Read the script's output to comprehensively map my knowledge, memory, tools, and skills.