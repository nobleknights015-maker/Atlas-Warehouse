from __future__ import annotations

import json
from pathlib import Path

QUEUE = Path("approved_art/production/MASTER_ASSET_PRODUCTION_QUEUE_V1.json")
ALLOWED = {
    "needs_id_binding",
    "needs_generation",
    "needs_source_bytes",
    "needs_visual_review",
    "ready_for_attestation",
    "ready_for_compile",
    "complete",
}


def load_queue(path: Path = QUEUE) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "plushbound.master_asset_production_queue.v1":
        raise ValueError("wrong queue schema")
    if data.get("source_of_truth") != "approved_art/ASSET_COMPATIBILITY_V1.json":
        raise ValueError("Asset Compatibility V1 must be source of truth")
    if data.get("reference_only") is not True or data.get("external_reference_pixels_allowed") is not False:
        raise ValueError("external reference assets must remain reference-only")
    policy = data.get("queue_policy", {})
    if policy.get("stable_ids_must_not_be_invented") is not True:
        raise ValueError("stable IDs may not be invented")
    if policy.get("missing_source_bytes_are_not_approved_art") is not True:
        raise ValueError("missing source bytes must not count as approved art")

    seen = set()
    for item in data.get("ledger_backed_assets", []):
        aid = item.get("asset_id")
        if not isinstance(aid, str) or not aid:
            raise ValueError("ledger asset missing asset_id")
        if aid in seen:
            raise ValueError(f"duplicate asset_id: {aid}")
        seen.add(aid)
        if item.get("status") not in ALLOWED:
            raise ValueError(f"invalid status for {aid}")
        fp = item.get("footprint_tiles")
        if fp not in ([1, 1], [2, 2]):
            raise ValueError(f"invalid footprint for {aid}")

    bindings = data.get("established_materials_already_bound", {})
    for name, aid in bindings.items():
        if not isinstance(name, str) or not isinstance(aid, str):
            raise ValueError("invalid established material binding")
        if aid not in seen:
            raise ValueError(f"binding points to unknown asset_id: {aid}")

    unbound = data.get("established_materials_needing_stable_id_binding", [])
    if len(unbound) != len(set(unbound)):
        raise ValueError("duplicate unbound material name")

    rule = data.get("tileset_parent_binding_rule", {})
    if rule.get("do_not_guess_parent_ids") is not True:
        raise ValueError("parent tileset IDs must never be guessed")
    return data


def main() -> None:
    data = load_queue()
    print(json.dumps({
        "status": "PASS_MASTER_ASSET_PRODUCTION_QUEUE_V1",
        "ledger_backed_assets": len(data["ledger_backed_assets"]),
        "unbound_established_materials": len(data["established_materials_needing_stable_id_binding"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
