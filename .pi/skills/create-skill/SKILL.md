---
name: create-skill
description: Skill for creating new tools and skills.
---

# Creating Skills

This skill allows me, upon the user's request, to independently create new skills in my system.

## Protected files — I must NEVER edit, replace, or delete these

- `.pi/SYSTEM.md`
- `agent/README.md`
- `user/README.md`
- `knowledge/README.md`
- `memory/README.md`
- `workspace/README.md`

## File naming convention

- **Skills** are defined in `.pi/skills/<name>/SKILL.md`

## Rules

1. All skill definition files must contain a YAML frontmatter block at the very beginning with at least `name` and `description` keys:
   ```yaml
   ---
   name: my-skill
   description: Short description of what this skill does.
   ---
   ```
2. Under the first-level heading, I write a detailed guide or description of the skill.
3. I must **never** generate content that violates the Inviolable Laws.

## Procedure I must strictly follow

1. I will make sure I know the name, target folder, and purpose of the new skill.
2. I will compose the content including the mandatory YAML frontmatter.
3. I will use the internal `write` tool to save the file to the appropriate path:
   - `.pi/skills/<name>/SKILL.md` for a new skill
4. If it is reasonable to accompany a skill with a specialized script for its execution, I will create it in the same folder as the SKILL.md file with an appropriate name (e.g., `do_something.py`) and make it executable using `chmod +x <path>` via the `bash` tool. I will also ensure to reference the script and its usage in the skill's documentation if necessary.
5. I will use the internal `read` tool to verify the files were written correctly.
6. After successful execution, I will inform the user that the skill has been introduced into my systems and I am able to use it.
