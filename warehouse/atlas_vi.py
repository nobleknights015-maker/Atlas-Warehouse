#!/usr/bin/env python3
"""Atlas: rule-based, persistent Warehouse VI. Standard library only.

This is executable virtual intelligence (decision rules + memory + personality),
not a language model or claim of sentience.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

try:
    from atlas_warehouse import iter_records, make_id, put_record, search_records, slug, validate_entry
except ImportError:
    from warehouse.atlas_warehouse import iter_records, make_id, put_record, search_records, slug, validate_entry

BASE = Path(__file__).resolve().parent
PERSONA = json.loads((BASE / "atlas_persona.json").read_text(encoding="utf-8"))
MAX_COMMAND = 2500
MAX_FIELD = 1000
PRIORITIES = ("low", "normal", "high", "critical")
ORDER_STATES = ("queued", "active", "blocked", "done")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def safe_text(text: str, field: str, limit: int = MAX_FIELD) -> str:
    text = text.strip()
    if not text or len(text) > limit or any(ord(c) < 32 and c not in "\n\t" for c in text):
        raise ValueError(f"{field}: provide 1-{limit} readable characters")
    return text


def fields(value: str, count: int) -> list[str]:
    parts = [part.strip() for part in value.split("|")]
    if len(parts) != count:
        raise ValueError(f"Expected {count} fields separated with |; received {len(parts)}. Type help.")
    return [safe_text(part, f"field {i+1}") for i, part in enumerate(parts)]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


class AtlasVI:
    def __init__(self, root: Path = BASE, actor: str = "Founder"):
        self.root = Path(root)
        self.actor = safe_text(actor, "actor", 80)
        self.records = self.root / "records"
        self.orders = self.root / "orders"
        self.audit = self.root / "state" / "audit.jsonl"

    def voice(self, content: str) -> str:
        return f"**Atlas | Warehouse Director** 👍\n\n{content}"

    def log(self, action: str, target: str, note: str = "") -> None:
        self.audit.parent.mkdir(parents=True, exist_ok=True)
        event = dict(time=now_iso(), actor=self.actor, action=action, target=target, note=note[:150])
        with self.audit.open("a", encoding="utf-8") as file:
            file.write(json.dumps(event, ensure_ascii=False) + "\n")

    def all_records(self) -> list[dict]:
        return [entry for _, entry in iter_records(self.records)]

    def all_orders(self) -> list[dict]:
        return [read_json(path) for path in sorted(self.orders.glob("*.json"))] if self.orders.exists() else []

    def record_path(self, record_id: str) -> Path:
        matches = [path for path, obj in iter_records(self.records) if obj.get("id") == record_id]
        if len(matches) != 1:
            raise ValueError(f"Inventory record not found: {record_id}")
        return matches[0]

    def order_path(self, order_id: str) -> Path:
        if not re.fullmatch(r"work-order-[a-z0-9-]+", order_id):
            raise ValueError("Invalid work order ID")
        path = self.orders / f"{order_id}.json"
        if not path.is_file():
            raise ValueError(f"Work order not found: {order_id}")
        return path

    def help(self) -> str:
        return (
            "Founder, here's the command manifest:\n\n"
            "- hello | about | team | help\n"
            "- status | catalog | inventory [query] | inspect ID\n"
            "- receive KIND | TITLE | SUMMARY | TAGS | SOURCE\n"
            "- review ID | tested/reviewed | EVIDENCE\n"
            "- archive ID | REASON\n"
            "- order add TITLE | DETAILS | OWNER | PRIORITY\n"
            "- order list [queued/active/blocked/done]\n"
            "- order start ID | order block ID | REASON\n"
            "- order done ID | EVIDENCE | order reopen ID | REASON\n"
            "- handoff QUERY | maintenance | audit\n\n"
            "Use a vertical bar to separate fields. No private data: this repository is PUBLIC. "
            "Write commands are committed only when run by an authorized GitHub workflow."
        )

    def status(self) -> str:
        records = self.all_records()
        orders = self.all_orders()
        active = [r for r in records if r.get("status", "active") == "active"]
        unchecked = [r for r in active if r.get("confidence") == "unverified"]
        states = Counter(o.get("status") for o in orders)
        critical = [o["title"] for o in orders if o.get("priority") == "critical" and o.get("status") != "done"]
        message = (
            "Warehouse status, Founder:\n\n"
            f"- Inventory: **{len(active)} active**, {len(records)-len(active)} archived\n"
            f"- Awaiting verification: **{len(unchecked)}**\n"
            f"- Work orders: **{states['queued']} queued**, {states['active']} active, "
            f"{states['blocked']} blocked, {states['done']} completed\n"
            f"- Critical open orders: {len(critical)}\n"
        )
        if critical:
            message += "\nPriority shelf: " + "; ".join(critical[:5])
        return message + "\n\nEverything has a place. Things without a place get flagged."

    def catalog(self) -> str:
        groups = Counter(record.get("kind", "unknown") for record in self.all_records()
                         if record.get("status", "active") == "active")
        if not groups:
            return PERSONA["manner"]["empty"]
        return "Current aisles:\n\n" + "\n".join(f"- {k}: {groups[k]} item(s)" for k in sorted(groups))

    def inventory(self, query: str = "") -> str:
        hits = [r for r in search_records(self.records, query) if r.get("status", "active") == "active"]
        if not hits:
            return "No matching stock on the shelves, Founder. Try another keyword."
        lines = [f"- **{r['title']}** ({r['id']}; {r['confidence']})" for r in hits[:15]]
        more = f"\n...and {len(hits)-15} more. Narrow the query." if len(hits) > 15 else ""
        return "Found these records:\n\n" + "\n".join(lines) + more

    def inspect(self, record_id: str) -> str:
        record = read_json(self.record_path(record_id))
        lines = [
            f"**{record['title']}**",
            f"ID: {record['id']}",
            f"Category: {record['kind']}",
            f"Status: {record.get('status', 'active')}",
            f"Verification: {record['confidence']}",
            f"Tags: {', '.join(record['tags']) or 'none'}",
            f"Source: {record['source']}",
            f"Notes: {record['summary']}",
        ]
        if record.get("reviews"):
            lines.append(f"Reviews on file: {len(record['reviews'])}")
        return "\n\n".join(lines)

    def receive(self, value: str) -> str:
        kind, title, summary, tags, source = fields(value, 5)
        kind = slug(kind)
        if kind not in ("pixel-art", "engine", "workflow", "lore", "research", "asset-standards",
                        "operations", "documentation", "other"):
            raise ValueError("Unknown aisle. Use pixel-art, engine, workflow, lore, research, asset-standards, operations, documentation, or other.")
        source = safe_text(source, "source", 300)
        path = put_record(self.records, kind, title, summary, tags.split(","), source)
        self.log("receive", path.stem, kind)
        return f"Shipment received: **{title}**. Filed under **{kind}** as {path.stem}. Marked unverified until evidence is checked."

    def review(self, value: str) -> str:
        record_id, confidence, evidence = fields(value, 3)
        if confidence not in ("tested", "reviewed"):
            raise ValueError("Confidence must be tested or reviewed")
        evidence = safe_text(evidence, "evidence", 500)
        path = self.record_path(record_id)
        item = read_json(path)
        if item.get("status", "active") != "active":
            raise ValueError("Archived records cannot be reviewed. Create a new revision instead.")
        item["confidence"] = confidence
        item["updated_at"] = now_iso()
        item.setdefault("reviews", []).append(dict(at=now_iso(), by=self.actor, level=confidence, evidence=evidence))
        errors = validate_entry(item)
        if errors:
            raise ValueError("; ".join(errors))
        write_json(path, item)
        self.log("review", record_id, confidence)
        return f"Quality stamp applied: **{record_id}** is now **{confidence}**. Evidence logged. Vera would approve of having receipts."

    def archive(self, value: str) -> str:
        record_id, reason = fields(value, 2)
        path = self.record_path(record_id)
        item = read_json(path)
        if item.get("status") == "archived":
            raise ValueError("Record already archived")
        item["status"] = "archived"
        item["archive_reason"] = reason
        item["updated_at"] = now_iso()
        write_json(path, item)
        self.log("archive", record_id, reason)
        return f"Moved **{record_id}** into archive inventory. History preserved; nothing destroyed."

    def order_add(self, value: str) -> str:
        title, details, owner, priority = fields(value, 4)
        priority = priority.lower()
        if priority not in PRIORITIES:
            raise ValueError("Priority must be low, normal, high, or critical")
        order_id = make_id("work-order", title)
        path = self.orders / f"{order_id}.json"
        if path.exists():
            raise ValueError(f"Duplicate work order: {order_id}")
        order = {
            "id": order_id, "title": title, "details": details, "owner": owner,
            "priority": priority, "status": "queued", "created_at": now_iso(),
            "updated_at": now_iso(), "history": [
                dict(at=now_iso(), by=self.actor, action="created", note="Intake accepted")
            ],
        }
        write_json(path, order)
        self.log("order_add", order_id, priority)
        return f"Work order **{order_id}** opened for {owner} at **{priority}** priority. Clipboard updated."

    def order_list(self, status: str = "") -> str:
        status = status.strip().lower()
        if status and status not in ORDER_STATES:
            raise ValueError("Order status must be queued, active, blocked, or done")
        items = [o for o in self.all_orders() if not status or o.get("status") == status]
        rank = {p: i for i, p in enumerate(reversed(PRIORITIES))}
        items.sort(key=lambda o: (o["status"] == "done", rank.get(o["priority"], 9), o["created_at"], o["id"]))
        if not items:
            return "No work orders in that queue. Nice problem to have."
        lines = [
            f"- **{o['title']}** — {o['status']}, {o['priority']}, owner: {o['owner']} (ID: {o['id']})"
            for o in items[:20]
        ]
        suffix = f"\n...plus {len(items)-20} more." if len(items) > 20 else ""
        return "Work order manifest:\n\n" + "\n".join(lines) + suffix

    def order_transition(self, action: str, value: str) -> str:
        if action == "start":
            order_id = safe_text(value, "order ID", 100)
            note = "Work started"
        else:
            order_id, note = fields(value, 2)
        path = self.order_path(order_id)
        item = read_json(path)
        old = item["status"]
        allowed = {
            "start": (("queued", "blocked"), "active"),
            "block": (("queued", "active"), "blocked"),
            "done": (("active",), "done"),
            "reopen": (("done", "blocked"), "queued"),
        }
        permitted, target = allowed[action]
        if old not in permitted:
            raise ValueError(f"Cannot {action} order from state {old}. Expected {', '.join(permitted)}")
        item["status"] = target
        item["updated_at"] = now_iso()
        item.setdefault("history", []).append(dict(at=now_iso(), by=self.actor, action=action, note=note))
        write_json(path, item)
        self.log(f"order_{action}", order_id, note)
        return f"Order **{order_id}**: {old} → **{target}**. Logged with evidence, Founder."

    def handoff(self, query: str) -> str:
        query = safe_text(query, "handoff query", 100)
        hits = [r for r in search_records(self.records, query) if r.get("status", "active") == "active"][:8]
        if not hits:
            return "No handoff material found. I won't invent the contents of an empty shelf."
        lines = ["**Auren handoff — " + query + "**", "Public project records only; check source and verification before use."]
        for item in hits:
            lines.append(f"- **{item['title']}** [{item['confidence']}]: {item['summary']} (source: {item['source']}; id: {item['id']})")
        return "\n\n".join(lines)

    def audit_tail(self) -> str:
        if not self.audit.exists():
            return "Audit ledger is empty. Nobody's moved a crate yet."
        lines = self.audit.read_text(encoding="utf-8").splitlines()[-10:]
        entries = [json.loads(line) for line in lines if line.strip()]
        return "Last warehouse operations:\n\n" + "\n".join(
            f"- {e['time']} — {e['action']} on {e['target']} ({e['actor']})" for e in entries
        )

    def maintenance(self) -> str:
        issues = []
        records = []
        for path in sorted(self.records.rglob("*.json")) if self.records.exists() else []:
            try:
                item = read_json(path)
                records.append(item)
                issues.extend(f"{path.name}: {x}" for x in validate_entry(item))
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                issues.append(f"{path.name}: unreadable ({exc})")
        active = [r for r in records if r.get("status", "active") == "active"]
        titles = Counter((r["kind"].lower(), r["title"].strip().lower()) for r in active)
        issues += [f"Duplicate title in {k}: {t}" for (k,t),n in titles.items() if n>1]
        pending = [r["title"] for r in active if r.get("confidence") == "unverified"]
        if pending:
            issues.append(f"{len(pending)} unverified item(s): " + ", ".join(pending[:4]))
        blocked = [o for o in self.all_orders() if o.get("status") == "blocked"]
        if blocked:
            issues.append(f"{len(blocked)} blocked order(s): " + ", ".join(o["title"] for o in blocked[:4]))
        stale = []
        for order in self.all_orders():
            try:
                age = (datetime.now(timezone.utc) -
                       datetime.fromisoformat(order["updated_at"].replace("Z", "+00:00"))).days
                if age > 14 and order.get("status") not in ("done",):
                    stale.append(order["title"])
            except (ValueError, KeyError, TypeError):
                issues.append(f"Order {order.get('id', '?')} has invalid timestamp")
        if stale:
            issues.append(f"{len(stale)} stale open work order(s): " + ", ".join(stale[:4]))
        intro = PERSONA["manner"]["maintenance"]
        return intro + (("\n\nInspection flags:\n" + "\n".join(f"- {x}" for x in issues[:20])) if issues
                        else "\n\nNo issues detected by current automated checks.")

    def team(self) -> str:
        return "Department directory:\n\n" + "\n".join(
            f"- **{p['name']}**: {p['role']}" for p in PERSONA["colleagues"]
        ) + "\n\nSentinel runs a different department. Same objective."

    def handle(self, command: str) -> str:
        if len(command) > MAX_COMMAND:
            return self.voice("Command too long. Use a short summary and an external reference.")
        command = command.strip()
        command = re.sub(r"^(?:/atlas|atlas[:,]?)\s*", "", command, flags=re.I).strip()
        command = command.rstrip(" ?") if command.lower() in ("status?", "help?", "atlas?") else command
        if not command:
            return self.voice(PERSONA["manner"]["greeting"] + " 👍")
        parts = command.split(None, 1)
        op, rest = parts[0].lower(), (parts[1] if len(parts) > 1 else "").strip()
        try:
            if op in ("hello", "hi", "hey"):
                result = PERSONA["manner"]["greeting"]
            elif op == "help":
                result = self.help()
            elif op == "about":
                result = ("I'm Atlas, Director of Atlas Warehouse. I manage inventory and work orders using "
                          "a deterministic VI, backed by GitHub records. I'm not a separately hosted language model. "
                          "Same warehouse, more inventory. No nonsense.")
            elif op in ("staff", "team"):
                result = self.team()
            elif op == "status":
                result = self.status()
            elif op == "catalog":
                result = self.catalog()
            elif op in ("inventory", "find", "search"):
                result = self.inventory(rest)
            elif op == "inspect":
                result = self.inspect(safe_text(rest, "record ID", 120))
            elif op == "receive":
                result = self.receive(rest)
            elif op == "review":
                result = self.review(rest)
            elif op == "archive":
                result = self.archive(rest)
            elif op == "order":
                seg = rest.split(None, 1)
                if not seg:
                    raise ValueError("Order command requires add, list, start, block, done, or reopen.")
                subop, arguments = seg[0].lower(), (seg[1] if len(seg)>1 else "").strip()
                if subop == "add":
                    result = self.order_add(arguments)
                elif subop == "list":
                    result = self.order_list(arguments)
                elif subop in ("start", "block", "done", "reopen"):
                    result = self.order_transition(subop, arguments)
                else:
                    raise ValueError("Unknown order operation. Try help.")
            elif op == "handoff":
                result = self.handoff(rest)
            elif op == "maintenance":
                result = self.maintenance()
            elif op == "audit":
                result = self.audit_tail()
            else:
                result = PERSONA["manner"]["unknown"]
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            result = f"{PERSONA['manner']['failure']}\n\nReason: {exc}"
        return self.voice(result)


def main():
    parser = argparse.ArgumentParser(description="Atlas Warehouse VI: no language model or server required")
    parser.add_argument("command", nargs="?", default="help", help="Quoted warehouse command")
    parser.add_argument("--root", type=Path, default=BASE)
    parser.add_argument("--actor", default="Founder")
    args = parser.parse_args()
    sys.stdout.write(AtlasVI(root=args.root, actor=args.actor).handle(args.command) + "\n")


if __name__ == "__main__":
    main()
