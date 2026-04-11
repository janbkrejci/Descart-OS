---
name: read-docs
description: Skill for fetching and reading library documentation using the bundled context7-cli.
---

# Skill: read-docs

This skill provides an interface to search and retrieve up-to-date library documentation via the bundled context7-cli tool included with this skill.

Script location:
- context7-cli: .pi/skills/read-docs/context7-cli (executable Node bundle)

Recommended usage:
1. First call "resolve-library-id" to obtain a Context7 libraryId:
   node .pi/skills/read-docs/context7-cli resolve-library-id --query "<your query>" --library-name "<library name>" --output json

2. Then call "query-docs" with the returned libraryId:
   node .pi/skills/read-docs/context7-cli query-docs --library-id "/org/project" --query "<specific question>" --output markdown

Examples:
- node .pi/skills/read-docs/context7-cli resolve-library-id --query "how to use effect.ts" --library-name "effect-ts"
- node .pi/skills/read-docs/context7-cli query-docs --library-id "/effect-ts/effect" --query "basic usage and examples" --output markdown

Important limitations and recommendations:
- Do not include sensitive information (API keys, passwords, personal data, or proprietary code) in queries.
- Context7 recommends not calling "query-docs" more than 3× per single user question (see the tool's built-in guidance).
- The script is a bundled Node program and requires Node.js available in PATH; it contains a shebang (#!/usr/bin/env node) and is executable.
- When the skill uses relative paths, they are resolved relative to the skill directory (.pi/skills/read-docs).

Implementation note for the assistant:
- This skill was created by moving an existing context7-cli bundle from the workspace to this skill directory per the user's request.
- All skill content and related scripts must be maintained in English in accordance with repository language rules.

