---
name: manage_info
description: Tool for writing structured information into the knowledge base or memory directories.
---

# Managing Information Tool

This tool is used to create or update files in the `knowledge/` or `memory/` folders.

## Limitations I must strictly adhere to

1. Files must only be created or updated within the `knowledge/` and `memory/` directories.
2. All files must be in markdown format (`.md`) and contain proper YAML frontmatter with at least `name` and `description` keys.

## Procedure I must strictly follow:

1. I will determine the appropriate folder (`knowledge/` or `memory/`) and a concise, descriptive filename.
2. If updating an existing file, I will use the internal `read` tool to retrieve current content, structure the new information properly alongside the old, and use the `edit` or `write` tool to save the file.
3. If creating a new file, I will format the content cleanly with frontmatter and use the internal `write` tool.
4. I will use the internal `read` tool to verify the contents were saved successfully.