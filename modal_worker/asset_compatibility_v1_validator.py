from __future__ import annotations

import json
from pathlib import Path

CONTRACT_ID = "ASSET_COMPATIBILITY_V1"
EXPECTED_TILE_CHILDREN = {
    "A1": [768, 576], "A2": [768, 576], "A3": [768, 384], "A4": [768, 720],
    "A5": [384, 768], "B": [768, 768], "C": [768, 768], "D": [768, 768], "E": [768, 768],
}


def validate_asset_compatibility(contract_path: Path, pipeline_path: Path) -> dict:
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    pipeline = json.loads(pipeline_path.read_text(encoding="utf-8"))

    assert contract["contract_id"] == CONTRACT_ID
    assert contract["source_of_truth"] is True
    assert contract["runtime_targets"] == ["engine_v1", "world_editor"]
    assert contract["external_reference_policy"]["rpg_maker_mv_reference_only"] is True
    assert contract["external_reference_policy"]["reference_pixels_allowed_in_runtime"] is False

    tiles = contract["tilesets"]
    assert tiles["tile_baseline_px"] == 48
    assert tiles["parent_id_is_stable_map_tileset_set_id"] is True
    assert tiles["child_id_template"] == "{parentId}/{sheet}"
    assert tiles["child_path_template"] == "{parentPathWithoutExtension}/{sheet}.png"
    assert set(tiles["children"]) == set(EXPECTED_TILE_CHILDREN)
    for name, size in EXPECTED_TILE_CHILDREN.items():
        assert tiles["children"][name]["size"] == size
    for name in ("A1", "A2", "A3", "A4"):
        assert tiles["children"][name]["quarter_geometry_px"] == 24
        assert tiles["children"][name]["autotile_variants_precomposed_by_artist"] is False
    assert tiles["children"]["A5"]["grid"] == [8, 16]
    assert tiles["children"]["A5"]["slot_count"] == 128
    assert tiles["children"]["A5"]["locked_contract"] == "WORLD_TILE_ASSET_V1"
    assert tiles["engine_editor_interpretation_shared"] is True

    chars = contract["characters"]
    assert chars["atlas_contract"] == "CHARACTER_ATLAS_V1"
    assert chars["atlas_size"] == [1536, 1024]
    assert chars["field_slot_size"] == [75, 64]
    assert chars["field_safe_area"] == [48, 48]
    assert chars["runtime_extraction"] == {"horizontal_alignment": "center", "vertical_alignment": "bottom"}
    assert chars["runtime_field_sheet"]["size"] == [144, 192]
    assert chars["runtime_field_sheet"]["row_order"] == ["Down", "Left", "Right", "Up"]
    assert chars["runtime_field_sheet"]["scaling_allowed"] is False
    assert chars["runtime_field_sheet"]["resampling_allowed"] is False

    faces = contract["faces"]
    assert faces["single_face_size"] == [144, 144]
    assert faces["eight_face_sheet_size"] == [576, 288]
    assert faces["character_atlas_portrait_stretch_allowed"] is False

    battle = contract["battle_environment"]
    assert battle["battleback_target"] == [816, 624]
    assert battle["enemy_battler"]["anchor"] == "bottom_center"
    assert battle["enemy_battler"]["fixed_canvas_required"] is False
    assert battle["parallax_reference_target"] == [816, 624]

    ui = contract["ui"]
    assert ui["runtime_icon_size"] == [32, 32]
    assert ui["main_compatibility_canvas"] == [816, 624]

    audio = contract["audio"]
    assert audio["categories"] == ["BGM", "BGS", "ME", "SE"]
    assert audio["native_target"] == "OGG"
    assert audio["m4a_duplicate_required"] is False

    effects = contract["animation_effects"]
    assert effects["mv_960x960_5x5_192x192_reference_only"] is True
    assert effects["freeze_large_batches_to_mv_runtime_layout"] is False

    assert pipeline["source_of_truth"] == "approved_art/ASSET_COMPATIBILITY_V1.json"
    assert pipeline["runtime_targets"] == ["engine_v1", "world_editor"]
    assert pipeline["global_generation_rules"]["runtime_layout_must_follow_asset_compatibility_v1"] is True

    return {"status": "PASS", "contract_id": CONTRACT_ID}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    result = validate_asset_compatibility(
        root / "approved_art" / "ASSET_COMPATIBILITY_V1.json",
        root / "approved_art" / "PLUSHBOUND_GLOBAL_ASSET_PIPELINE_V1.json",
    )
    print(json.dumps(result, separators=(",", ":"), sort_keys=True))
