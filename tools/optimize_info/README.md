---
name: optimize_info
description: Tool for reading, analyzing, reorganizing, and updating existing files in knowledge base and memory.
---

# Optimization Information Tool

This tool provides the capabilities to read, restructure, and overwrite existing files in the `knowledge/` and `memory/` directories to optimize their content.

## Procedure I must strictly follow:

1. I will use the internal `read` tool (or `bash` for listing directory structures) to analyze the current state of `knowledge/` and `memory/`.
2. I will prepare the reorganized and optimized markdown content in memory, ensuring YAML frontmatter (like `name` and `description`) is maintained or improved.
3. I will use the internal `edit` or `write` tool to apply the structural and content changes to the files.
4. If old files are rendered obsolete by merging, I will use the `bash` tool to delete them (`rm`).
5. I will verify the integrity of the updated files using the internal `read` tool.