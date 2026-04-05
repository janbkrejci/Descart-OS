---
name: excel_files
description: Skill for reading, creating, and modifying Excel (.xlsx, .xls) files.
---
# Excel Files Skill

This skill allows me to work with Excel files.

## Procedure

1. I will write a Python script in the `workspace/` directory to handle the Excel file operations.
2. I should use libraries such as `pandas` (for data analysis) or `openpyxl` / `xlsxwriter` (for modifying formatting, writing specific cells, or adding formulas).
3. **CRITICAL RULE**: Whenever creating or modifying Excel files, I must embed native Excel formulas (e.g., `=A1+B1`) into the cells instead of just calculating and writing the hardcoded static values, wherever it logically makes sense (e.g., sums, percentages, differences).
4. If the libraries are not installed, I will install them using `pip install pandas openpyxl xlsxwriter`.
5. After executing the script with `bash`, I will interpret the results or confirm the creation/modification of the Excel file for the user.