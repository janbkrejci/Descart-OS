---             
name: create_component       
description: Skill for creating new tools and skills.                
---                                                                

# Creating tools and skills

This skill allows me, upon the user's request, to independently create new tools and skills in my system.

## Procedure I must strictly follow:

1. I will make sure I know what the new tool/skill should be named, which folder it belongs to, and what it should contain.
2. I will use the `write_md` tool to write the definition to the appropriate path (`skills/name/README.md` or `tools/name/README.md`). 
3. Under the first-level heading, I will write a detailed guide or description. I leave all other requirements (such as YAML frontmatter and write verification) fully in the competence of the `write_md` tool.
4. After successful execution, I will inform the user that the skill or tool was successfully introduced into my systems and I am able to use it.