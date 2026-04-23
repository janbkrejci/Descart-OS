---
name: pid-journey
description: Local trip planner for Prague (PID) using the official GTFS feed (no API key required). Supports departure/arrival time search and max transfers.
---

# PID Journey Skill

This skill implements a local public-transit trip planner for Prague Integrated Transport (PID) using the official GTFS feed (https://data.pid.cz/PID_GTFS.zip). No external API key required.

Features
- Plan a journey from stop A to stop B using the official GTFS schedule.
- Support for: departure-time search (leave after a given time) or arrival-time search (arrive by a given time).
- Limit maximum transfers (including direct-only / zero transfers).
- Uses onboard RAPTOR-like algorithm over the GTFS timetable.
- Caches parsed GTFS for faster repeated queries.

Files
- pid_journey.py — CLI script

Quick usage
1) Download and prepare GTFS (first run will auto-download, or run with --refresh to force re-download):

   ./pid_journey.py fetch --refresh

2) Plan by departure time (default):

   ./pid_journey.py plan --from "Anděl" --to "Národní třída" --date 2026-04-22 --time 18:00 --mode departure --max-transfers 2

3) Plan by arrival time:

   ./pid_journey.py plan --from "Anděl" --to "Národní třída" --date 2026-04-22 --time 18:00 --mode arrival --max-transfers 2

Notes
- If a stop name matches multiple stops, the script will prompt for selection (interactive terminal required).
- The GTFS feed is public (data.pid.cz) and contains schedule and realtime-related static files. The script uses GTFS calendar/calendar_dates to select services active on the requested date.
- This is a prototype: for production use, add better heuristics for walking, caching, multi-criteria ranking, and UI improvements.

If you want, I can now:
- Run a sample query (I will download the GTFS feed and run it) — you'll need to confirm (it will download ~48 MB), or
- Tweak output formatting or add an option to return JSON for programmatic use.
