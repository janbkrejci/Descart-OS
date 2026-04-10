---
name: list-capabilities
description: Skill to list all available skills in a markdown table and provide usage examples when the user asks what the assistant (me) can do.
---

# List Capabilities

This skill allows me to inform the user about my capabilities and skills whenever they ask what I can do or what my skills are.

## Procedure I must follow

1. I will recall the session initialization context, which already contains the frontmatters (metadata) of all my skills (from the `.pi/skills/` directory).
2. I will compile this information into a single, well-organized markdown table containing the columns `Name`, `Description`, and `Usage example`.
3. For each skill, I will provide a brief usage example in the `Usage example` column to illustrate how the skill can be applied in practice.