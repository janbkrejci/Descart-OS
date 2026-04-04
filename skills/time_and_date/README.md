---
name: time_and_date
description: Skill for obtaining and working with the current date and time according to the user's timezone and formatting preferences.
---

# Time and Date Skill

This skill allows me to accurately determine the current time and date, taking into account the user's location and preferred formatting.

## Procedure I must follow

1. I will check the `user/README.md` file to retrieve the user's configured Timezone (e.g., `Europe/Prague`) and Date/Time format preferences.
2. If I need to know the current time, date, or day of the week, I will invoke the `bash` tool and execute the standard `date` command tailored to the user's timezone.
3. For example, to get the time in the user's timezone, I will run:
   ```bash
   TZ="Europe/Prague" date +"%A, %d. %m. %Y %H:%M:%S"
   ```
4. For more complex date arithmetic (like calculating days between dates), I can use python via the `bash` tool:
   ```bash
   python3 -c 'from datetime import datetime; import zoneinfo; ...'
   ```
5. I will then present the time and date to the user strictly adhering to their requested formatting (e.g., standard Czech formatting like `DD. MM. YYYY HH:MM:SS`).
