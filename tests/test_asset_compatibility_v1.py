import json
import tempfile
import unittest
from pathlib import Path

from modal_worker.asset_compatibility_v1_validator import validate_asset_compatibility


class AssetCompatibilityV1Tests(unittest.TestCase):
    def test_repo_contract_passes(self):
        root = Path(__file__).resolve().parents[1]
        result = validate_asset_compatibility(
            root / "approved_art" / "ASSET_COMPATIBILITY_V1.json",
            root / "approved_art" / "PLUSHBOUND_GLOBAL_ASSET_PIPELINE_V1.json",
        )
        self.assertEqual(result["status"], "PASS")

    def test_rejects_wrong_a5_geometry(self):
        root = Path(__file__).resolve().parents[1]
        contract = json.loads((root / "approved_art" / "ASSET_COMPATIBILITY_V1.json").read_text())
        pipeline = json.loads((root / "approved_art" / "PLUSHBOUND_GLOBAL_ASSET_PIPELINE_V1.json").read_text())
        contract["tilesets"]["children"]["A5"]["size"] = [768, 768]
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            c = td / "c.json"; p = td / "p.json"
            c.write_text(json.dumps(contract)); p.write_text(json.dumps(pipeline))
            with self.assertRaises(AssertionError):
                validate_asset_compatibility(c, p)

    def test_rejects_mv_animation_layout_as_production(self):
        root = Path(__file__).resolve().parents[1]
        contract = json.loads((root / "approved_art" / "ASSET_COMPATIBILITY_V1.json").read_text())
        pipeline = json.loads((root / "approved_art" / "PLUSHBOUND_GLOBAL_ASSET_PIPELINE_V1.json").read_text())
        contract["animation_effects"]["freeze_large_batches_to_mv_runtime_layout"] = True
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            c = td / "c.json"; p = td / "p.json"
            c.write_text(json.dumps(contract)); p.write_text(json.dumps(pipeline))
            with self.assertRaises(AssertionError):
                validate_asset_compatibility(c, p)


if __name__ == "__main__":
    unittest.main()
