---
name: excel-files
description: Skill for reading, creating, and modifying Excel (.xlsx, .xls) files.
---

# Excel Files Skill

This skill allows me to work with Excel files.

## Procedure

1. I will write a Python script in the `workspace/` directory using the `uv run --script` format (per the `script-dependencies` memory rule):
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["pandas", "openpyxl", "xlsxwriter"]
   # ///
   ```
2. I should use `pandas` for data analysis, and `openpyxl` / `xlsxwriter` for formatting, writing specific cells, or adding formulas.
3. **Critical rule:** Whenever creating or modifying Excel files, I must embed native Excel formulas (e.g., `=A1+B1`) into the cells instead of writing hardcoded static values, wherever it logically makes sense (e.g., sums, percentages, differences).
4. I will make the script executable with `chmod +x` and execute it via the `bash` tool.
5. I will interpret the results or confirm the creation/modification of the Excel file for the user.
