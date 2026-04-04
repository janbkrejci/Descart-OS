---
name: collect_folder_instructions
description: Tool for efficiently collecting frontmatters from all sub-README.md files in a specified folder.
---

# Collect Folder Instructions

This tool allows me to efficiently scan a specified directory (such as `skills`, `tools`, `knowledge`, or `memory`) and extract only the YAML frontmatter (metadata) from all `README.md` files located in its immediate subdirectories. This significantly speeds up the initialization process by avoiding the need to read the full contents of all files at once. The top-level `README.md` is ignored, as it is already loaded during session startup.

## Limitations I must strictly adhere to

1. I will only use this tool for directories that follow the standard structure (a root `README.md` and subdirectories with their own `README.md` files).

## Procedure I must strictly follow:

1. I will determine the target directory path (e.g., `tools/`).
2. I will use the system `bash` tool to execute a command or a short script (e.g., using `find` and `awk`/`sed` or a lightweight `python` script) that:
   - Iterates through all immediate subdirectories, and for each `README.md` file found, prints its path and extracts only the lines between the `---` delimiters (the YAML frontmatter). The root `README.md` is omitted.
3. I will read and process the output to map all available elements (e.g., tool names and their descriptions) into my context.
4. If I later need the full instructions for a specific element, I will read its entire `README.md` file individually.
