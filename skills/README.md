# My skills - skills/README.md

This folder contains my skills, which I can only use when working for my user.

Skills are organized in logically structured directories, each containing a mandatory `SKILL.md` file. If the `SKILL.md` file is missing from any skill directory, I must stop working, alert the user, and recommend steps to resolve this issue.

A **skill** contains procedural instructions that tell me how to accomplish a task. Skills may reference tools (executables in the `tools/` directory) or use my built-in tools (`read`, `write`, `edit`, `bash`).

The subdirectories containing my skills and their respective structures are automatically collected and processed during session initialization via the `init_context` tool (`tools/init_context/init_context.py`), so I do not need to scan them manually.
