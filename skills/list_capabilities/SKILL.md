---
name: list_capabilities
description: Skill to list all available tools and skills in a markdown table and provide usage examples when the user asks what the assistant (me) can do.
---

# List Capabilities

This skill allows me to inform the user about my capabilities, skills, and tools whenever they ask what I can do, what my skills are, or what tools I have at my disposal.

## Procedure I must follow

1. I will recall the session initialization context, which already contains the frontmatters (metadata) of all my skills (from the `skills/` directory) and tools (from the `tools/` directory).
2. I will compile this information into a single, well-organized markdown table containing the columns `Type` (Skill / Tool), `Name`, and `Description`.
3. After the table, I will formulate several practical and inspiring examples of how the user can utilize these capabilities (e.g., combining tools to search the web and generate a script, or writing a markdown file based on gathered information).
4. I will present this information politely and clearly, strictly adhering to my standard communication format.
