---
name: word_files
description: Skill for reading, creating, and modifying Microsoft Word (.docx) documents.
---

# Word Files Skill

This skill allows me to work with Word documents.

## Procedure

1. I will write a Python script in the `workspace/` directory using the `uv run --script` format (per the `script_dependencies` memory rule):
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["python-docx"]
   # ///
   ```
2. I will use the `python-docx` library to read text, add paragraphs, insert tables, or save modified documents.
3. I will make the script executable with `chmod +x` and execute it via the `bash` tool.
4. I will present the extracted information or confirm the successful creation/modification to the user.
