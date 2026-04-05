---
name: write_md
description: Tool for creating and editing markdown files.
---
# Creating and editing markdown files

This tool allows me, upon the user's request, to independently create and edit markdown files on the disk.

## Limitations I must strictly adhere to

I must **never** edit, replace or delete these files:
- .pi/SYSTEM.md
- agent/README.md
- user/README.md
- knowledge/README.md
- memory/README.md
- skills/README.md
- tools/README.md
- workspaace/README.md

## Procedure I must strictly follow:

1. I will make sure I know the name and path to the file, and what the file should contain.
2. I will use the allowed internal tool `write` to overwrite the entire file, or `edit` to modify the content of an existing file, and ensure the file has the requested content.
3. I will ensure that the markdown file always contains the mandatory YAML frontmatter at the beginning (at least with the keys `name` and `description`).
4. I will check using the internal tool `read` that the content of the file is exactly as requested.
5. After successful execution, I will inform the user that the file has been created or edited according to the request.