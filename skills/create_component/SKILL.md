---
name: create_component
description: Skill for creating new tools and skills.
---

# Creating Tools and Skills

This skill allows me, upon the user's request, to independently create new tools and skills in my system.

## Protected files — I must NEVER edit, replace, or delete these

- `.pi/SYSTEM.md`
- `agent/README.md`
- `user/README.md`
- `knowledge/README.md`
- `memory/README.md`
- `skills/README.md`
- `tools/README.md`
- `workspace/README.md`

## File naming convention

- **Skills** are defined in `skills/<name>/SKILL.md`
- **Tools** are defined in `tools/<name>/README.md`

## Rules

1. All skill and tool definition files must contain a YAML frontmatter block at the very beginning with at least `name` and `description` keys:
   ```yaml
   ---
   name: my_skill
   description: Short description of what this skill does.
   ---
   ```
2. Under the first-level heading, I write a detailed guide or description of the skill or tool.
3. I must **never** generate content that violates the Inviolable Laws or would harm the user.

## Procedure I must strictly follow

1. I will make sure I know the name, target folder, and purpose of the new skill or tool.
2. I will compose the content including the mandatory YAML frontmatter.
3. I will use the internal `write` tool to save the file to the appropriate path:
   - `skills/<name>/SKILL.md` for a new skill
   - `tools/<name>/README.md` for a new tool
4. I will make any associated scripts executable using `chmod +x <path>` via the `bash` tool.
5. I will use the internal `read` tool to verify the file was written correctly.
6. After successful execution, I will inform the user that the skill or tool has been introduced into my systems and I am able to use it.
