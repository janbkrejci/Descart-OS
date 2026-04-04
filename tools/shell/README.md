---
name: shell
description: Tool for executing a given command in tmux and returning its output.
---

# Shell (tmux)

This tool allows me to execute a bash command in the `tmux` multiplexer and retrieve its output. To actually execute the commands, I use my system tool `bash`.

## Usage and rules
1. I will use the system tool `bash` to perform the action.
2. I will execute the command requested by the user within a `tmux` session (e.g., using `tmux new-session`, `tmux send-keys`, etc.).
3. Subsequently, I will capture the result of the command (e.g., by redirecting to a file or via `tmux capture-pane -p`) and ensure that no empty or unnecessary windows are left hanging.
4. If the command runs for a long time, tmux allows me to detach the process in the background and check its output later.