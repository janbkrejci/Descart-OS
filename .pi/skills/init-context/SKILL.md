---
name: init-context
description: Skill for initializing the assistant's context by gathering and outputting the contents of all mandatory system files and metadata of all subdirectories.
---

# Skill: init-context

This skill is responsible for initializing the assistant's context before any conversation with the user. It gathers and outputs the contents of all mandatory system files (agent, user, knowledge, memory, skills, tools, workspace) along with the metadata (frontmatters) of all subdirectories.

## Procedure

1. Run the `init_context.py` script located in this skill's directory using the `bash` internal tool.
2. The script will output the contents of all mandatory system files and metadata in a structured format that I have to read, understand, and use to set up the context for the session.
3. If the script fails or I fail to understand its output, I must not proceed with conversation with my user; I must alert them to the missing files and advise them how to proceed.
4. If I successfully load and understand the context, I must follow it precisely under all circumstances. If the user informs me that a new element has been added or an existing element modified, I will re-run the script, re-read its output and process it immediately.