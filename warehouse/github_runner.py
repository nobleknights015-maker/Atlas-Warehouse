#!/usr/bin/env python3
"""GitHub Actions bridge for the Atlas Warehouse VI.

Reads event JSON from GITHUB_EVENT_PATH, never evaluates commands as code.
Only repository owner issue comments can mutate or query the public warehouse.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
from urllib.request import Request, urlopen

from atlas_vi import AtlasVI


def event_command(environ: dict, event: dict) -> tuple[str, str, int | None]:
    event_type = environ.get("GITHUB_EVENT_NAME", "")
    repo = environ.get("GITHUB_REPOSITORY", "")
    if "/" not in repo:
        raise ValueError("Missing repository identity")
    owner = repo.split("/", 1)[0]
    if event_type == "issue_comment":
        issue = event.get("issue") or {}
        comment = event.get("comment") or {}
        if "pull_request" in issue:
            raise PermissionError("Pull request comments are not VI command channels")
        actor = (comment.get("user") or {}).get("login")
        if actor != owner:
            raise PermissionError("Only repository owner may command Atlas through public issues")
        text = (comment.get("body") or "").strip()
        if not text.lower().startswith("/atlas "):
            raise ValueError("Issue comment must start with /atlas")
        number = issue.get("number")
        if not isinstance(number, int) or number < 1:
            raise ValueError("Missing valid issue number")
        return text, actor, number
    if event_type == "workflow_dispatch":
        actor = environ.get("GITHUB_ACTOR", "").strip() or owner
        return environ.get("ATLAS_COMMAND", "status"), actor, None
    if event_type == "schedule":
        return "maintenance", "Atlas VI scheduled inspection", None
    raise ValueError(f"Unexpected trigger {event_type}")


def reply_path(environ: dict) -> Path:
    workspace = Path(environ.get("GITHUB_WORKSPACE") or Path.cwd())
    return workspace / ".atlas-reply.md"


def run(environ: dict):
    payload = json.loads(Path(environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    command, actor, number = event_command(environ, payload)
    reply = AtlasVI(actor=actor).handle(command)
    # Keep the exact command and issue ID out of public records unless explicitly
    # stored by a supported mutation; even a public issue may contain information
    # that does not belong in a permanent inventory.
    reply_path(environ).write_text(reply + "\n", encoding="utf-8")
    print(f"Atlas VI command processed; reply length={len(reply)}; issue={number or 'dispatch/schedule'}")


def post(environ: dict):
    body = reply_path(environ).read_text(encoding="utf-8")[:60000]
    event_name = environ.get("GITHUB_EVENT_NAME", "")
    if event_name == "issue_comment":
        event = json.loads(Path(environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
        _, _, number = event_command(environ, event)
        token = environ.get("GITHUB_TOKEN", "")
        if not token:
            raise RuntimeError("GITHUB_TOKEN unavailable for issue reply")
        repo = environ["GITHUB_REPOSITORY"]
        url = f"https://api.github.com/repos/{repo}/issues/{number}/comments"
        request = Request(url, data=json.dumps({"body": body}).encode("utf-8"), method="POST",
                          headers={"Authorization": f"Bearer {token}",
                                   "Accept": "application/vnd.github+json",
                                   "X-GitHub-Api-Version": "2022-11-28",
                                   "Content-Type": "application/json",
                                   "User-Agent": "Atlas-Warehouse-VI"})
        with urlopen(request, timeout=30) as response:
            if response.status != 201:
                raise RuntimeError(f"Comment posting failed: HTTP {response.status}")
        print(f"Atlas replied in issue #{number}")
    summary_path = environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as file:
            file.write("## Atlas Warehouse VI\n\n" + body + "\n")
    print(body)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("run", "post"):
        raise SystemExit("Usage: python warehouse/github_runner.py run|post")
    if sys.argv[1] == "run":
        run(os.environ)
    else:
        post(os.environ)


if __name__ == "__main__":
    main()
