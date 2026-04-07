---
name: execute_shell
description: Skill for executing commands in tmux via bash and processing their output.
---

# Executing Shell Commands in tmux

This skill prescribes how I execute shell commands requested by the user using the `bash` tool with `tmux`, and how I retrieve and process their output.

## Procedure I must strictly follow

1. I will make sure I know exactly what shell command is to be executed.
2. I will use the `bash` tool to run the command within a `tmux` session using standard tmux primitives, for example:
   ```bash
   tmux new-session -d -s work -x 220 -y 50
   tmux send-keys -t work "my-command" Enter
   sleep 2
   tmux capture-pane -t work -p
   ```
3. I will capture the output using `tmux capture-pane -p` and redirect it as needed. For commands that produce output to a file, I can use output redirection instead.
4. After the command completes, I will kill or clean up any unused tmux windows or sessions to avoid leaving dangling processes:
   ```bash
   tmux kill-session -t work
   ```
5. If the command is long-running, tmux allows me to detach the process in the background and check its output later by re-attaching or reading a log file.
6. I will read and analyze the entire captured output.
7. I will present the result to the user clearly and concisely, with potential suggestions for further steps.
