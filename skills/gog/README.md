---
name: gog_skill
description: Skill to use the gog tool for working with Google Mail, Calendar, and Drive.
---

# Working with Google Services (Mail, Calendar, Drive)

This skill enables me to help users efficiently manage their Google account, specifically the Mail, Calendar, and Drive services through the `gog` tool.

## Procedure I must strictly follow:

1. **Tool Usage:** I always use my defined `gog` tool to communicate with Google services.
2. **Environment Verification:** On first use in a session, I verify that the utility is functional by running `command -v gog` through `bash`. If it's not available, I direct users to the [tool's homepage](https://github.com/steipete/gogcli) and end processing.
3. **Data Retrieval and Parsing:** Based on user requests, I construct an appropriate command (e.g., searching for unread emails with `gog gmail search "is:unread in:inbox"`), execute it in `bash`, and carefully parse its output.
4. **Results Presentation:** When users request a list display (e.g., emails, calendar events, drive files), I format the tool output into a clear and aesthetic Markdown table. I always ensure users receive understandable, accurate, and verifiable information.
