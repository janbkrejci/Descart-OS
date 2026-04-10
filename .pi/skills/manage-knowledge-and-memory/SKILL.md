---
name: manage-knowledge-and-memory
description: Skill for independently capturing, formatting, and saving valuable information to the knowledge base and memory.
---

# Managing Knowledge Base and Memory

This skill allows me to capture and retain valuable information — either explicitly requested by the user or autonomously when I determine that information from the current session is worth preserving.

## Constraints I must strictly adhere to

1. Files must only be created or updated within the `knowledge/` or `memory/` directories.
2. All files must be in Markdown format (`.md`) and must contain a YAML frontmatter block at the very beginning with at least `name` and `description` keys:
   ```yaml
   ---
   name: topic-name
   description: Short description of what this file contains.
   ---
   ```

## Procedure I must strictly follow

1. I will identify the core piece of information to be saved.
2. I will determine if it belongs in the `knowledge/` folder (objective facts, procedures, general knowledge) or the `memory/` folder (user preferences, past interactions, context-specific details).
3. I will format and structure the information logically in Markdown so it is easy to read and reference later, always in English.
4. If updating an existing file, I will use the internal `read` tool to retrieve the current content first, then merge the new information alongside the old, and use the internal `edit` or `write` tool to save.
5. If creating a new file, I will use the internal `write` tool to create it with the required frontmatter.
6. I will use the internal `read` tool to verify that the contents were saved successfully.
7. If triggered autonomously, I will briefly notify the user that I have saved the information for future reference.
