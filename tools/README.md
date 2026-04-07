# My tools - tools/README.md

In this folder are the tools I'm authorized to use when working for my user.

Tools are organized in logically structured directories, each containing a mandatory `README.md` file. If the `README.md` file is missing, I'll stop, alert my user that it is unavailable, and recommend steps to resolve this.

A **tool** represents an actual executable capability — a Python or Bash script, or a CLI utility — that I invoke via the `bash` system tool. Pure procedural instructions without an underlying script or executable belong in **skills**, not here.

The subdirectories containing my tools and their respective structures are automatically collected and processed during session initialization via the `init_context` tool (`tools/init_context/init_context.py`), so I do not need to scan them manually.
