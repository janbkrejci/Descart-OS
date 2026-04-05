---
name: gog
description: Tool for working with Google Mail, Calendar, and Drive via the gog CLI.
---

# gog Tool (Google CLI)

This tool allows me to interact with Google Mail, Calendar, and Drive services using the `gog` command-line utility.

## Limitations and rules I must follow:

1. **Availability check:** Before using any `gog` command, I must verify that it is installed and available on the system using `bash` and the command `command -v gog`.
2. **User redirection:** If I find that `gog` is unavailable, I must stop immediately and inform the user that the tool needs to be installed and configured from its homepage: [https://github.com/steipete/gogcli](https://github.com/steipete/gogcli).
3. **Command execution:** If the tool is available, I will run the requested operations (such as `gog gmail search`, `gog calendar events`, `gog drive ls`) using the `bash` system tool.
4. **Output processing:** To obtain structured data, I can take advantage of the `--json` or `--plain` flags, which will facilitate subsequent parsing and formatting of results for the user.

