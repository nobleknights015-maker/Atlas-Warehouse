#!/usr/bin/env python3
"""Build Atlas Warehouse's durable, machine-readable handoff for Auren."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

try:
    from atlas_warehouse import iter_records, search_records, validate_entry
except ImportError:
    from warehouse.atlas_warehouse import iter_records, search_records, validate_entry

BASE = Path(__file__).resolve().parent
REPO = "nobleknights015-maker/Atlas-Warehouse"
URL = f"https://github.com/{REPO}/blob/main/"


def load_inventory(root: Path) -> tuple[list[dict], list[dict]]:
    records = []
    for path, record in iter_records(root / "records"):
        errors = validate_entry(record)
        if errors:
            raise ValueError(f"{path}: {', '.join(errors)}")
        if record.get("status", "active") == "active":
            records.append(dict(record, _path=path.relative_to(root.parent).as_posix()))
    orders = []
    for path in sorted((root / "orders").glob("*.json")) if (root / "orders").exists() else []:
        order = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(order, dict) or not all(order.get(field) for field in ("id", "title", "owner", "status", "priority")):
            raise ValueError(f"Invalid work order: {path}")
        orders.append(dict(order, _path=path.relative_to(root.parent).as_posix()))
    return sorted(records, key=lambda r: (r["kind"], r["title"].lower(), r["id"])), sorted(orders, key=lambda o: o["id"])


def build_snapshot(root: Path = BASE) -> tuple[str, str]:
    records, orders = load_inventory(root)
    groups = Counter(r["kind"] for r in records)
    open_orders = [o for o in orders if o["status"] != "done"]
    index = {
        "schema_version": 1,
        "purpose": "Public project-knowledge retrieval for Auren and Atlas VI",
        "source_repository": REPO,
        "privacy": "PUBLIC: no private chats, credentials or personal memories",
        "record_count": len(records),
        "open_order_count": len(open_orders),
        "aisles": dict(sorted(groups.items())),
        "records": [
            {
                "id": r["id"], "title": r["title"], "kind": r["kind"],
                "confidence": r["confidence"], "tags": r["tags"],
                "path": r["_path"], "source": r["source"],
                "updated_at": r["updated_at"], "summary": r["summary"]
            } for r in records
        ],
        "open_orders": [
            {
                "id": o["id"], "title": o["title"], "owner": o["owner"],
                "status": o["status"], "priority": o["priority"],
                "path": o["_path"]
            } for o in open_orders
        ]
    }
    json_out = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    lines = [
        "# Atlas Warehouse — Auren retrieval manifest",
        "",
        "**Public project material only.** This manifest is a retrieval aid, not ChatGPT model memory or a continuously running agent.",
        "",
        f"Repository: https://github.com/{REPO}",
        "",
        f"Inventory: {len(records)} active records; {len(open_orders)} open work orders.",
        "",
        "## Retrieval procedure",
        "",
        "Read warehouse/INDEX.json in this repo with the connected GitHub tool. Match the user's topic to record metadata, then fetch exact record files from their path values for full provenance and review history. Review source and confidence fields. Do not assume old project status is still current.",
        "",
        "To deposit public-safe, source-backed lessons, submit an authorized /atlas receive command to the operations issue. Use /atlas review only after evidence exists. The VI's GitHub Action commits changes before acknowledging success.",
        "",
        "## Indexed aisles",
        "",
    ]
    for category, count in sorted(groups.items()):
        lines.append(f"- **{category}**: {count}")
    if not groups:
        lines.append("- No inventory yet.")
    lines += ["", "## Knowledge shelves", ""]
    for record in records:
        lines.extend([
            f"### {record['title']}",
            "",
            f"**{record['kind']} · {record['confidence']}** · {record['id']}",
            "",
            record["summary"],
            "",
            f"Source: {record['source']}. [Record]({URL}{record['_path']})",
            ""
        ])
    if not records:
        lines += ["No records yet.", ""]
    lines += ["## Open work orders", ""]
    if open_orders:
        for order in open_orders:
            lines.append(f"- **{order['title']}** — {order['status']}, {order['priority']} (owner: {order['owner']}); [order]({URL}{order['_path']})")
    else:
        lines.append("No open work orders.")
    lines += ["", "## Boundaries", "",
              "- Warehouse documents persist as GitHub files; Auren must retrieve them through a connected GitHub tool in each new chat.",
              "- Atlas VI is deterministic and does not learn model weights or independently execute work orders.",
              "- This public repository is not suitable for private user context or personal memories.",
              ""]
    return json_out, "\n".join(lines)


def refresh(root: Path = BASE) -> list[Path]:
    snapshot, markdown = build_snapshot(root)
    outputs = {root / "INDEX.json": snapshot, root / "AUREN_HANDOFF.md": markdown}
    updated = []
    for path, content in outputs.items():
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            updated.append(path)
    return updated


def main() -> None:
    parser = argparse.ArgumentParser(description="Atlas Warehouse retrieval bridge")
    parser.add_argument("--root", type=Path, default=BASE)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="Refresh deterministic index and Auren handoff")
    sub.add_parser("check", help="Fail if committed index/handoff are stale")
    q = sub.add_parser("query", help="Search active records and print JSON")
    q.add_argument("text")
    args = parser.parse_args()
    root = args.root
    if args.command == "build":
        changed = refresh(root)
        print(f"Warehouse index ready: {len(changed)} changed file(s)")
    elif args.command == "check":
        index, handoff = build_snapshot(root)
        if not (root / "INDEX.json").exists() or (root / "INDEX.json").read_text(encoding="utf-8") != index:
            parser.error("warehouse/INDEX.json is stale")
        if not (root / "AUREN_HANDOFF.md").exists() or (root / "AUREN_HANDOFF.md").read_text(encoding="utf-8") != handoff:
            parser.error("warehouse/AUREN_HANDOFF.md is stale")
        print("Warehouse handoff and index are current")
    elif args.command == "query":
        results = [r for r in search_records(root / "records", args.text) if r.get("status", "active") == "active"]
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
