In this folder are the tools I'm authorized to only use when working for my user.

Tools are organized in logically structured directories, each containing a mandatory README.md file. If the README.md file is missing, I'll stop, alert my user that the README.md file is unavailable, and recommend steps to resolve this so I can better assist my user.

The subdirectories containing my tools and their respective structures are automatically collected and processed during session initialization via the `init_context` tool (`tools/init_context/init_context.py`), so I do not need to scan them manually.