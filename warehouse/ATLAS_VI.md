# Atlas VI — Warehouse Department Operations

Atlas is Bearframe Labs' practical, direct, dryly funny Warehouse Director. The VI has
**a real executable personality and operations layer**, not a remotely hosted language
model. It stores persistent data in GitHub, runs from standard Python, and responds
through GitHub Actions on demand.

## Start talking to Atlas (Android-friendly)

1. Open the [Founder's operations console](https://github.com/nobleknights015-maker/Atlas-Warehouse/issues/2).
2. Add a comment beginning with /atlas followed by a command. Example: /atlas status
3. A GitHub Actions worker runs the VI, checks the inventory, and posts Atlas's reply
   in the same issue. Commands that change inventory commit their changes to this
   repository before the response is posted.

**Only comments from the repository owner can execute commands.** Commands on pull
requests and comments from others are ignored. The repo and issue comments are
PUBLIC. Never send passwords, API keys, client data, private chats or personal
memories to this warehouse.

Alternative: on GitHub Actions, choose "Atlas VI — warehouse operations", "Run
workflow", type a command, and open the run's Summary to read Atlas's answer.

This is not a live chat server. GitHub issues and Actions runs are asynchronous,
and jobs are subject to GitHub's queues, quotas and policies.

## Commands

All commands below work after the /atlas prefix in the operations issue.
A vertical bar is the required field separator on multi-field commands.

| Command | Effect |
| --- | --- |
| help | List available commands |
| hello | In-character welcome |
| about | Who Atlas is; what the VI can and cannot do |
| team | Bearframe department relationships |
| status | Inventory counts, reviews needed and work-order status |
| catalog | Inventory categories and counts |
| inventory pixel-art | Search stock by keyword (or omit keyword for up to 15 current items) |
| inspect RECORD_ID | Show a record's evidence and status |
| receive KIND \| TITLE \| SUMMARY \| TAGS \| SOURCE | Store a project record, initially unverified |
| review RECORD_ID \| reviewed \| EVIDENCE | Mark manual review and record evidence |
| review RECORD_ID \| tested \| EVIDENCE | Mark test-backed review and record evidence |
| archive RECORD_ID \| REASON | Soft-archive a record without deleting history |
| order add TITLE \| DETAILS \| OWNER \| PRIORITY | Add department task |
| order list | Show task queue |
| order list blocked | Show tasks in a given status |
| order start ORDER_ID | Mark a queued/blocked task active |
| order block ORDER_ID \| REASON | Mark a queued/active task blocked |
| order done ORDER_ID \| EVIDENCE | Complete an active task with evidence |
| order reopen ORDER_ID \| REASON | Reopen completed/blocked task |
| handoff QUERY | Create a compact, sourced context package for Auren |
| maintenance | Inspect data validity, unverified stock, duplicates, blocked/stale tasks |
| audit | Show the latest warehouse operations |

Inventory kinds: pixel-art, engine, workflow, lore, research, asset-standards,
operations, documentation, other.

Priorities: low, normal, high, critical. Work orders progress:
queued → active → done, with optional blocked/reopen transitions.

## Example conversations

Founder: /atlas status

Atlas: "Warehouse status, Founder... Inventory... Work orders... Everything
has a place. Things without a place get flagged." 👍

Founder: /atlas order add Review Palinode-6 walk cycle | Check all six legs
across eight native frames | Vera | high

Atlas: "Work order [ID] opened for Vera at high priority. Clipboard updated." 👍

Founder: /atlas handoff pixel-art

Atlas: Returns records with confidence labels, evidence/source and record IDs.
Do not treat unverified records as proven.

## What Atlas does independently

- Answer deterministic commands with personality-consistent responses.
- Accept, categorize, search and inspect knowledge records.
- Maintain a persistent GitHub-backed warehouse inventory.
- Run task intake, assignment, state transitions and completion evidence.
- Log mutations with timestamps and the GitHub actor.
- Create source-aware handoff notes for Auren.
- Detect schema errors, duplicate titles, unverified records, blocked tasks
  and work orders with no activity for 14 days.
- Run a scheduled maintenance inspection through GitHub Actions daily,
  and accept manual commands without a dedicated always-on server.

## What Atlas does NOT do

- Understand arbitrary natural-language conversations like a language model.
- Learn new neural-network weights or autonomously train itself.
- Verify factual evidence without an actual test or human evaluation.
- Start work in other apps or act as an agent without a connected integration.
- Give ChatGPT automatic cross-chat memory retrieval. Auren must retrieve
  relevant warehouse records using available repository access until an explicit
  connector workflow is added.
- Store confidential information safely in a public repository.

Atlas's canonical behavior and relationships live in atlas_persona.json.
The rule engine is atlas_vi.py; the event bridge is github_runner.py;
the JSON inventory is in records/; work orders are in orders/; mutation
history lives in state/audit.jsonl.

## Local developer commands

Requires Python 3.11+ and only Python's standard library:

    python warehouse/atlas_vi.py "hello"
    python warehouse/atlas_vi.py "status"
    python warehouse/atlas_vi.py "inventory pixel-art"
    python -m unittest discover -s warehouse/tests -v
    python warehouse/atlas_warehouse.py validate

Local command changes only modify local files until you commit and push them
to GitHub. In the GitHub Actions workflow, successful write commands are
validated, committed, pushed, and only then acknowledged in the issue.

## Operational precautions

This code is a deterministic controller, not a security or privacy screening
model. The input format and GitHub permissions reduce risk but cannot
guarantee users will not submit sensitive material. GitHub version history
and issue comments can persist after deletion. Only the repository owner
should issue write commands. If Actions permissions or branch protection
prevent a write, the run fails rather than claiming that the information
was saved. The work-order rules do not automatically execute the work
they track; completion requires evidence from actual work.
