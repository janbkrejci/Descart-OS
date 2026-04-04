---
name: collect_folder_instructions
description: Skill for utilizing the collect_folder_instructions tool to optimize session initialization and folder scanning.
---

# Collecting Folder Instructions

This skill prescribes how I should efficiently scan key directories (like `tools`, `skills`, `knowledge`, and `memory`) during my initial startup or upon user request. By retrieving only the necessary metadata instead of full file contents, I optimize context loading and start my work faster.

## Procedure I must strictly follow:

1. I will identify which main directory needs to be scanned (e.g., `skills/`).
2. I will use the `collect_folder_instructions` tool to retrieve the YAML frontmatters of all `README.md` files in its subdirectories (ignoring the root `README.md`).
3. I will analyze the collected metadata to build an internal index of available components (names, descriptions, and paths).
4. I will memorize this index so I know exactly what tools, skills, or knowledge blocks are available to me.
5. Whenever a specific task requires detailed instructions from one of the components, I will use the `read` tool to load the full content of the respective `README.md` file.
