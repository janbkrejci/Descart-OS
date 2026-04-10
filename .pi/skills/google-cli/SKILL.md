---
name: google-cli
description: Skill to use the gog CLI for working with Google Mail, Calendar, and Drive.
---

# Working with Google Services (Mail, Calendar, Drive)

This skill enables me to help users efficiently manage their Google account — specifically Mail, Calendar, and Drive — via the `gog` command-line utility.

## Availability check — mandatory on first use in each session

Before issuing any `gog` command, I must verify the utility is installed:
```bash
command -v gog
```
If `gog` is unavailable, I must stop immediately and direct the user to install and configure it from: [https://github.com/steipete/gogcli](https://github.com/steipete/gogcli).

## Procedure I must strictly follow

1. **Verify availability** as described above.
2. **Construct the appropriate command** based on the user's request. Examples:
   - Search unread inbox: `gog gmail search "is:unread in:inbox"`
   - List calendar events: `gog calendar events`
   - List Drive files: `gog drive ls`
3. **Execute** the command using the `bash` tool.
4. **Parse output** using `--json` or `--plain` flags where available to obtain structured data suitable for further processing.
5. **Present results** formatted as a clear Markdown table when listing items (emails, events, files). Always ensure the user receives accurate and verifiable information.
