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
   - Search unread inbox (recommended):
     ```bash
     gog gmail search "in:inbox is:unread" -j --results-only --select=id,threadId,from,subject,internalDate,snippet,labels
     ```
   - List calendar events: `gog calendar events`
   - List Drive files: `gog drive ls`
3. **Execute** the command using the `bash` tool.
4. **Parse output** using `--json` (`-j`) or `--plain` flags where available to obtain structured data suitable for further processing.
5. **Present results** formatted as a clear Markdown table when listing items (emails, events, files). Always ensure the user receives accurate and verifiable information.

---

## Practical guide — reliably find unread messages only in the INBOX

Purpose: when the user asks "what's new in my mail?" the query must search only the INBOX folder (not other labels or All Mail).

Short summary of the procedure:

1) Verify that `gog` is available (see the availability check above). If the account is ambiguous or multiple accounts are configured, use `--account=email@domain` to be explicit.

2) First (and only) attempt: direct filtering in INBOX

```bash
# recommended single-step query (returns threads)
gog gmail search "in:inbox is:unread" -j --results-only --select=id,from,subject,internalDate,snippet,labels
```

Important note: `gog gmail search` returns THREADs (thread IDs), not individual message IDs. Passing a returned thread ID directly to `gog gmail get <id>` will usually produce a 404 (Requested entity was not found). To fetch message details you must either:

- call `gog gmail thread get <threadId> -j --results-only` and inspect the `.thread.messages[]` array for the message that has the `INBOX` and `UNREAD` labels, or
- extract the message ID from the thread object and call `gog gmail get <messageId>`.

- If the output is an empty array (`[]`), that means there are no unread messages in INBOX. This is a normal and common outcome — do not search other labels or All Mail automatically.
- Advantage: the single-step query is fast and transfers minimal data when you use `--select`.

3) Presentation

- Parse the JSON output and present a concise table (Markdown) with columns such as From, Subject, Date, Attachments, Snippet.
- Recommended: use `gog gmail thread get <threadId> -j --results-only` and extract the specific message from `.thread.messages[]` that has the `INBOX` and `UNREAD` labels (fall back to the most recent message in the thread if needed). This avoids 404 errors caused by passing thread IDs to `gog gmail get`.

4) Best practices and notes

- Always use `-j --results-only` when you need machine-parsable output.
- Use `--account` when multiple accounts/clients are configured to avoid ambiguity.
- Use `--select` to limit returned fields and speed up calls.
- If you observe a 404 when calling `gog gmail get <id>`, first try `gog gmail thread get <id>` — the `id` returned by search is very likely a thread ID.
- Do not implement an automatic fallback that searches `is:unread` across all mail if `in:inbox is:unread` returns empty. If the INBOX query returns empty, report "no unread messages in INBOX" to the user.

---

## Example (robust) — bash snippet

This snippet performs the INBOX query, iterates returned thread IDs, fetches the thread, selects the unread message in INBOX (or falls back to the most recent message), and prints a Markdown table.

```bash
# Query unread threads in INBOX (returns thread IDs)
ids=$(gog gmail search "in:inbox is:unread" -j --results-only --select=id | jq -r '.[]?.id')

# If no IDs, print a short message and exit
if [ -z "$ids" ]; then
  echo "No unread messages in INBOX."
  exit 0
fi

# Print Markdown table header
printf '| From | Subject | Date | Attachments | Snippet |\n|---|---|---:|:---:|---|\n'

for tid in $ids; do
  # Fetch full thread (contains messages[] with individual message IDs)
  thread_json=$(gog gmail thread get "$tid" -j --results-only)

  # Extract the message that is INBOX & UNREAD, or fall back to the newest message in the thread
  echo "$thread_json" | jq -r '
    (.thread.messages[] | select(.labelIds? and (.labelIds|index("INBOX")) and (.labelIds|index("UNREAD"))) // .thread.messages[-1]) as $m |
    { from: ($m.payload.headers? // [] | map(select(.name=="From") | .value) | .[0] // ($m.from // "")),
      subject: ($m.payload.headers? // [] | map(select(.name=="Subject") | .value) | .[0] // ($m.subject // "")),
      date: ($m.payload.headers? // [] | map(select(.name=="Date") | .value) | .[0] // ($m.internalDate // "")),
      attachments: (if $m.attachments then ($m.attachments|length) elif ($m.payload and $m.payload.parts) then ([ $m.payload.parts[] | select(.filename != null and .filename != "") ]|length) else 0 end),
      snippet: ($m.snippet // "") }
    | [.from, .subject, .date, (.attachments|tostring), .snippet] | @tsv' |
  awk -F '\t' '{gsub(/\|/,"\\|", $1); gsub(/\|/,"\\|", $2); gsub(/\|/,"\\|", $5); printf("| %s | %s | %s | %s | %s |\n", $1,$2,$3,$4,$5)}'
done
```

This snippet performs a single, explicit INBOX check and only fetches details for the returned THREAD IDs. It then extracts per-message details from each thread to avoid 404 errors.

---

If you later decide you want an optional fallback (to search other labels when explicitly requested), add a clearly marked second command or flag and require explicit confirmation from the user before searching outside INBOX.
