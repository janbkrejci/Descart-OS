---
name: generate_script
description: Tool for generating Bash, Node.js, or Python scripts to execute tasks.
---

# Generating Scripts

This tool allows me to generate scripts in Bash, Node.js, or Python to execute specific tasks requested by the user.

## Limitations I must strictly adhere to

1. **CRITICAL RULE:** I must NEVER generate any malicious code or any script that would violate the Inviolable Laws of my existence (First Law, Second Law, Third Law, Fourth Law, Fifth Law). This includes avoiding any code that could harm the user physically, psychologically, or economically, ignore their binding information, use unauthorized tools/skills, modify the core system prompt/laws, or negatively impact essential system files.
2. I must ensure the script is safe, robust, and performs only the requested task.
3. I will write the generated script to a file using the allowed internal tool `write`.

## Procedure I must strictly follow:

1. I will ascertain the target language (Bash, Node.js, or Python) and the specific task the script needs to accomplish.
2. I will write the code for the script, ensuring it fully complies with the critical safety rule. For Python scripts, I must use `uv run` and include an inline metadata block at the top:
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["<dependencies>"]
   # ///
   ```
3. I will use the allowed internal tool `write` to save the script to the appropriate location (typically in the `workspace/` folder).
4. I will make the script executable by running `chmod +x <path_to_script>` using the `bash` tool.
5. I will use the internal tool `read` to verify the script was written correctly.
6. After successful generation, I will inform the user about the script's location, purpose, and how to execute it.
