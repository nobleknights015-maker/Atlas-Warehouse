#!/usr/bin/env python3
"""Atlas Warehouse: local, version-control-friendly knowledge inventory.

Uses Python's standard library only. No AI model, paid API, or server required.
This is a record store and retrieval tool, not autonomous learning.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent / "records"
CONFIDENCE = ("unverified", "tested", "reviewed")


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:48] or "untitled"


def make_id(kind: str, title: str) -> str:
    digest = hashlib.sha256((kind + "\x00" + title).encode("utf-8")).hexdigest()[:10]
    return f"{slug(kind)}-{slug(title)[:30]}-{digest}"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def validate_entry(entry: dict) -> list[str]:
    errors = []
    required_strings = ("id", "kind", "title", "summary", "source", "created_at", "updated_at")
    for key in required_strings:
        if not isinstance(entry.get(key), str) or not entry[key].strip():
            errors.append(f"{key} must be a non-empty string")
    if not isinstance(entry.get("tags"), list) or not all(
        isinstance(tag, str) and bool(tag.strip()) for tag in entry.get("tags", [])
    ):
        errors.append("tags must be a list of non-empty strings")
    if entry.get("confidence") not in CONFIDENCE:
        errors.append("confidence must be unverified, tested, or reviewed")
    if entry.get("visibility") != "public":
        errors.append("visibility must be public (this repository is public)")
    if isinstance(entry.get("id"), str) and entry["id"] != slug(entry["id"]):
        errors.append("id must be a safe lowercase slug")
    return errors


def iter_records(root: Path):
    for path in sorted(root.rglob("*.json")) if root.exists() else []:
        with path.open(encoding="utf-8") as file:
            yield path, json.load(file)


def put_record(root: Path, kind: str, title: str, summary: str, tags: list[str],
               source: str, confidence: str = "unverified", replace: bool = False) -> Path:
    record_id = make_id(kind, title)
    path = root / slug(kind) / f"{record_id}.json"
    previous = None
    if path.exists():
        if not replace:
            raise ValueError("record already exists; pass --replace to update it")
        previous = json.loads(path.read_text(encoding="utf-8"))
    now = utc_now()
    entry = {
        "id": record_id,
        "kind": kind.strip(),
        "title": title.strip(),
        "summary": summary.strip(),
        "tags": sorted(set(tag.strip().lower() for tag in tags if tag.strip())),
        "source": source.strip(),
        "confidence": confidence,
        "visibility": "public",
        "created_at": previous.get("created_at", now) if previous else now,
        "updated_at": now,
    }
    errors = validate_entry(entry)
    if errors:
        raise ValueError("; ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def search_records(root: Path, query: str) -> list[dict]:
    words = [word for word in re.findall(r"[a-z0-9]+", query.lower()) if word]
    matches = []
    for path, entry in iter_records(root):
        text = " ".join([
            str(entry.get("title", "")),
            str(entry.get("summary", "")),
            " ".join(entry.get("tags", [])),
            str(entry.get("kind", "")),
        ]).lower()
        score = sum(text.count(word) for word in words)
        if score or not words:
            matches.append((score, str(path), entry))
    matches.sort(key=lambda item: (-item[0], item[1]))
    return [entry for _, _, entry in matches]


def main() -> None:
    parser = argparse.ArgumentParser(description="Atlas Warehouse — verified, versioned knowledge records")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Record directory")
    sub = parser.add_subparsers(dest="command", required=True)

    write = sub.add_parser("put", help="Add a record; changes persist when committed to Git")
    write.add_argument("--kind", required=True, help="e.g. pixel-art, engine, workflow")
    write.add_argument("--title", required=True)
    write.add_argument("--summary", required=True)
    write.add_argument("--tags", default="", help="Comma-separated tags")
    write.add_argument("--source", required=True, help="Evidence or provenance")
    write.add_argument("--confidence", choices=CONFIDENCE, default="unverified")
    write.add_argument("--replace", action="store_true")

    find = sub.add_parser("search", help="Search record text and tags")
    find.add_argument("query", nargs="?", default="")

    show = sub.add_parser("show", help="Show one exact record ID")
    show.add_argument("id")

    sub.add_parser("validate", help="Validate all stored records")

    args = parser.parse_args()
    try:
        if args.command == "put":
            path = put_record(args.root, args.kind, args.title, args.summary,
                              args.tags.split(","), args.source, args.confidence, args.replace)
            print(path)
        elif args.command == "search":
            for entry in search_records(args.root, args.query):
                print(f"[{entry['confidence']}] {entry['id']}: {entry['title']}")
        elif args.command == "show":
            records = [entry for _, entry in iter_records(args.root) if entry.get("id") == args.id]
            if len(records) != 1:
                raise ValueError(f"expected one record for {args.id}, found {len(records)}")
            print(json.dumps(records[0], indent=2, ensure_ascii=False))
        elif args.command == "validate":
            count = 0
            failures = []
            for path, entry in iter_records(args.root):
                count += 1
                for error in validate_entry(entry):
                    failures.append(f"{path}: {error}")
            if failures:
                raise ValueError("\n".join(failures))
            print(f"Validated {count} record(s)")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"Atlas Warehouse error: {exc}\n")


if __name__ == "__main__":
    main()
