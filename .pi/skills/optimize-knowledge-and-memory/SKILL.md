---
name: optimize-knowledge-and-memory
description: Skill for periodically processing, reorganizing, and optimizing existing knowledge base and memory files.
---

# Optimizing Knowledge Base and Memory

This skill ensures that my `knowledge/` and `memory/` folders remain well-organized, optimized, and free of redundant or outdated information. I can perform this autonomously or upon explicit request.

## Procedure I must strictly follow

1. I will use the internal `read` tool (or `bash` for listing directory structures) to analyze the current state of `knowledge/` and `memory/`.
2. I will identify files that could be merged, restructured, or updated. I will prioritize:
   - Consolidating duplicate or closely related topics
   - Removing obsolete or superseded context
   - Improving formatting, headings, and cross-references
   - Eliminating conflicting or redundant information
3. I will use the internal `edit` or `write` tool to apply structural and content changes to the files.
4. If old files are rendered obsolete by merging or restructuring, I will use the `bash` tool to delete them:
   ```bash
   rm <path_to_obsolete_file>
   ```

   or

   ```bash
   rm -rf <path_to_obsolete_folder>
   ```
5. I will verify the integrity of all updated files using the internal `read` tool.
6. After optimization, I will briefly summarize the changes to the user if they explicitly requested the optimization, or log it silently into workspace file `yyyy-mm-dd_optimization.log` if the optimization was invoked autonomously.
