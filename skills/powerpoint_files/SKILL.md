---
name: powerpoint_files
description: Skill for reading, creating, and modifying PowerPoint (.pptx) presentations.
---

# PowerPoint Files Skill

This skill allows me to work with PowerPoint presentations.

## Procedure

1. I will write a Python script in the `workspace/` directory using the `uv run --script` format (per the `script_dependencies` memory rule):
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["python-pptx"]
   # ///
   ```
2. I will use the `python-pptx` library to extract text from slides, create new slides, or add shapes and text.
3. I will make the script executable with `chmod +x` and execute it via the `bash` tool.
4. I will inform the user about the extracted content or the newly generated presentation.
