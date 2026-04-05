---
name: init_context
description: Tool for gathering and formatting all mandatory files and directory frontmatters into a single output for session initialization.
type: system
---

# Initialize Context Tool

This tool is an executable Python script (`init_context.py`) designed to efficiently read all required system documents and create a session initialization prompt.

## Procedure I must strictly follow:

1. Use the `bash` tool to run `tools/init_context/init_context.py`. If the command fails, stop any further processing, inform the user about the problem and suggest a remedy.
2. Read the complete script's output to comprehensively map my personality, information about my user, my knowledge, memory, tools, and skills.