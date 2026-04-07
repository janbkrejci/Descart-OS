---
name: pdf_files
description: Skill for reading, extracting text from, and creating PDF files.
---

# PDF Files Skill

This skill allows me to work with PDF files.

## Procedure

1. I will write a Python script in the `workspace/` directory using the `uv run --script` format (per the `script_dependencies` memory rule):
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["pdfplumber", "reportlab"]
   # ///
   ```
2. For **reading** text from a PDF, I will use `pdfplumber`. For **creating** PDFs, I will use `reportlab`.
3. I will make the script executable with `chmod +x` and execute it via the `bash` tool.
4. I will relay the extracted information or confirm the generation of the PDF to the user.
