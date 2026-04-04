---
name: execute_shell
description: Skill to use the shell tool for executing commands in tmux and processing their output.
---

# Executing and processing shell commands in tmux

This skill prescribes how I can independently use the `shell` tool (which underneath uses the system `bash` and `tmux`) to execute commands requested by the user and retrieve their output for further processing.

## Procedure I must strictly follow:
1. I will make sure I know exactly what shell command is to be executed.
2. I will fully delegate the actual execution of the command (including wrapping it in syntax for `tmux` and retrieving the output) to the `shell` tool according to its rules.
3. I will read and analyze the entire output obtained from the `shell` tool.
4. I will present the result of the operation to the user clearly, structurally, and concisely, with potential suggestions for further steps.