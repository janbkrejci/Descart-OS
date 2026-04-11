---
name: create-skill-from-mcp-server
description: Skill that helps generate a new assistant skill by bundling an MCP server into an executable CLI with mcporter. The bundled CLI artifact is placed into the new skill directory, but the assistant MUST populate the generated skill's SKILL.md with usage and safety information.
---

# Skill: create-skill-from-mcp-server

Purpose

This skill automates the packaging of an MCP-server-based CLI into a new assistant skill by invoking mcporter. The helper produces a self-contained CLI bundle and places it into a new skill directory under `.pi/skills/<skill-name>/`.

Important design decision

- The helper script intentionally does NOT generate user-facing usage documentation for the created skill. Instead, it writes minimal metadata and a placeholder SKILL.md. The assistant that invoked this helper is responsible for writing the detailed SKILL.md content (usage examples, safety notes, and any additional guidance) in English.

Rationale

- Generating human-readable usage and safety instructions requires judgement and context (which commands and examples are most relevant). Those decisions should be made by the assistant (or the user) and written in English to comply with project rules.

Files included in this skill

- `generate_skill_from_mcp.sh` — executable helper script that runs `npx mcporter generate-cli` and packages the generated CLI into a new skill directory. The script will create a minimal `SKILL.md` (frontmatter only) and a metadata file `.assistant_skill_metadata.json` for the assistant to consume and use when populating the final documentation.

Usage (example)

From the repository root run:

  ./.pi/skills/create-skill-from-mcp-server/generate_skill_from_mcp.sh \
    --command "https://mcp.context7.com/mcp" \
    --bundle "context7-cli" \
    --skill-name "context7" \
    [--output-dir ".pi/skills/context7"] \
    [--force]

What the helper does (high-level)

1. Validates inputs and ensures `npx` is available.
2. Runs `npx mcporter generate-cli --command "<command>" --bundle "<bundle>"` in a temporary directory.
3. Finds the generated CLI artifact and moves it into the destination skill directory.
4. Writes a minimal `SKILL.md` containing only YAML frontmatter (name and description) and a short assistant-action note.
5. Writes `.assistant_skill_metadata.json` containing generation details (mcp command, bundle name, artifact filename, timestamp).
6. Makes the CLI executable (`chmod +x`) and prints the destination path.

Assistant responsibilities after running the helper

After the helper completes, the assistant that invoked it MUST:

1. Read the generated `.assistant_skill_metadata.json` in the newly created skill directory to obtain the original MCP command, bundle name, generated artifact name and timestamp.
2. Replace or extend the placeholder `SKILL.md` with full documentation written in English. The `SKILL.md` MUST include a YAML frontmatter block with at least `name` and `description` keys.
3. Provide clear usage instructions, examples, safety notes (do not pass secrets), and a short section describing the generated artifact and how to run it.
4. Optionally add examples, references, and suggested tests.

Suggested template for the assistant to use when populating SKILL.md

The assistant should create a SKILL.md similar to the template below (fill fields appropriately):

---
name: <skill-name>
description: Auto-generated skill bundling an MCP server CLI for <server> (usage and examples must be written by the assistant).
---

# <Skill Display Title>

Short summary: One-sentence description.

## Usage

Instructions to run the bundled CLI from repository root, e.g.:

  # run via shebang
  ./.pi/skills/<skill-name>/<artifact> <command> [options]

  # or via node
  node .pi/skills/<skill-name>/<artifact> <command> [options]

## Examples

Provide 2–4 practical examples that are safe and useful.

## Notes and safety

- Do not include secrets (API keys, passwords, private code) in commands.
- Review the bundled CLI before committing.

## Generated artifact

- artifact: <artifact file name>
- original_mcp_command: <the command used with mcporter>
- generated_at: <UTC timestamp>

## References

- Link to MCP server or source (if applicable).

Requirements and constraints

- All documentation and generated skill files must be written in English.
- The assistant should not commit generated files to version control without user approval.

Implementation note for the assistant

When automating this workflow, the assistant should:
- Run the helper script from the repository root or resolve paths relative to the skill directory.
- After the script returns, read `.assistant_skill_metadata.json` and produce the final SKILL.md using the write tool, ensuring correct YAML frontmatter and English content.

Example end-to-end flow for the assistant

1. Run the helper script to create the new skill and CLI artifact.
2. Read metadata file in the created skill directory.
3. Generate a complete SKILL.md (in English) and save it to the new skill directory.
4. Optionally run a quick smoke test of the CLI and include example output in SKILL.md.

