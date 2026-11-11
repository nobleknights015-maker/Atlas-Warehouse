#!/usr/bin/env python3
"""GitHub Actions bridge for Atlas VI, including durable burst-safe issue intake."""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
from urllib.request import Request, urlopen

from atlas_vi import AtlasVI
from auren_bridge import refresh

BASE = Path(__file__).resolve().parent
QUEUE_STATE = BASE / "state" / "issue_queue.json"


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
        body = (comment.get("body") or "").strip()
        if not body.lower().startswith("/atlas "):
            raise ValueError("Issue command must start with /atlas")
        number = issue.get("number")
        if not isinstance(number, int) or number < 1:
            raise ValueError("Missing valid issue number")
        return body, actor, number
    if event_type == "workflow_dispatch":
        actor = environ.get("GITHUB_ACTOR", "").strip() or owner
        if actor != owner:
            raise PermissionError("Only repository owner may dispatch commands")
        return environ.get("ATLAS_COMMAND", "status"), actor, None
    if event_type == "schedule":
        return "maintenance", "Atlas VI scheduled inspection", None
    raise ValueError(f"Unexpected trigger {event_type}")


def github_json(environ: dict, url: str) -> object:
    token = environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("GitHub token missing")
    req = Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Atlas-Warehouse-VI"
    })
    with urlopen(req, timeout=30) as response:
        return json.load(response)


def issue_comments(environ: dict, number: int) -> list[dict]:
    repo = environ["GITHUB_REPOSITORY"]
    collected = []
    # Read every accessible comment in order, so canceled pending workflows do
    # not lose owner commands in bursts. Safety cap avoids unbounded requests.
    for page in range(1, 21):
        url = f"https://api.github.com/repos/{repo}/issues/{number}/comments?per_page=100&page={page}"
        batch = github_json(environ, url)
        if not isinstance(batch, list):
            raise ValueError("Unexpected comment API result")
        collected.extend(batch)
        if len(batch) < 100:
            break
    else:
        raise RuntimeError("Issue exceeded 2,000 comments. Rotate the console.")
    return sorted(collected, key=lambda c: c.get("id", 0))


def reply_path(environ: dict) -> Path:
    workspace = Path(environ.get("GITHUB_WORKSPACE") or Path.cwd())
    return workspace / ".atlas-replies.json"


def process_pending_issue_commands(environ: dict, number: int) -> list[dict]:
    owner = environ["GITHUB_REPOSITORY"].split("/", 1)[0]
    if QUEUE_STATE.exists():
        checkpoint = json.loads(QUEUE_STATE.read_text(encoding="utf-8"))
        cursor = int(checkpoint.get("last_processed_id", 0))
        if checkpoint.get("issue_number") != number:
            raise ValueError("Issue queue is pinned to another console")
    else:
        cursor = 0
    replies = []
    max_id = cursor
    for item in issue_comments(environ, number):
        comment_id = item.get("id")
        if not isinstance(comment_id, int) or comment_id <= cursor:
            continue
        author = (item.get("user") or {}).get("login", "")
        command = (item.get("body") or "").strip()
        if author == owner and command.lower().startswith("/atlas "):
            response = AtlasVI(actor=owner).handle(command)
            replies.append({"issue_number": number, "comment_id": comment_id, "body": response})
        max_id = max(max_id, comment_id)
    if max_id != cursor:
        QUEUE_STATE.parent.mkdir(parents=True, exist_ok=True)
        QUEUE_STATE.write_text(
            json.dumps({"issue_number": number, "last_processed_id": max_id}, indent=2) + "\n",
            encoding="utf-8"
        )
    return replies


def run(environ: dict):
    payload = json.loads(Path(environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    command, actor, number = event_command(environ, payload)
    if number is not None:
        replies = process_pending_issue_commands(environ, number)
    else:
        replies = [{"issue_number": None, "comment_id": None, "body": AtlasVI(actor=actor).handle(command)}]
    refresh()
    reply_path(environ).write_text(json.dumps(replies, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Atlas VI processed {len(replies)} command(s) and refreshed the handoff index.")


def post_comment(environ: dict, issue_number: int, body: str):
    token = environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("GITHUB_TOKEN unavailable for issue reply")
    repo = environ["GITHUB_REPOSITORY"]
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    request = Request(url, data=json.dumps({"body": body[:60000]}).encode("utf-8"), method="POST",
                      headers={"Authorization": f"Bearer {token}",
                               "Accept": "application/vnd.github+json",
                               "X-GitHub-Api-Version": "2022-11-28",
                               "Content-Type": "application/json",
                               "User-Agent": "Atlas-Warehouse-VI"})
    with urlopen(request, timeout=30) as response:
        if response.status != 201:
            raise RuntimeError(f"Comment posting failed: HTTP {response.status}")


def post(environ: dict):
    replies = json.loads(reply_path(environ).read_text(encoding="utf-8"))
    for item in replies:
        if item.get("issue_number") is not None:
            post_comment(environ, int(item["issue_number"]), item["body"])
        summary_path = environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "a", encoding="utf-8") as file:
                file.write("## Atlas Warehouse VI\n\n" + item["body"] + "\n\n")
        print(item["body"][:4000])


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("run", "post"):
        raise SystemExit("Usage: python warehouse/github_runner.py run|post")
    if sys.argv[1] == "run":
        run(os.environ)
    else:
        post(os.environ)


if __name__ == "__main__":
    main()
