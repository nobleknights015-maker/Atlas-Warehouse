import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from atlas_warehouse import put_record
from auren_bridge import build_snapshot, refresh, load_inventory


class AurenBridgeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "warehouse"
        self.root.mkdir(parents=True)

    def test_snapshot_and_links_are_deterministic(self):
        put_record(self.root / "records", "engine", "Save load tests",
                   "Verify saving and loading on Android hardware.",
                   ["engine", "android"], "documented hardware testing")
        created = refresh(self.root)
        self.assertEqual(len(created), 2)
        self.assertEqual(refresh(self.root), [])
        data = json.loads((self.root / "INDEX.json").read_text(encoding="utf-8"))
        self.assertEqual(data["record_count"], 1)
        self.assertEqual(data["records"][0]["kind"], "engine")
        self.assertTrue(data["records"][0]["path"].startswith("warehouse/records/"))
        self.assertIn("Save load tests", (self.root / "AUREN_HANDOFF.md").read_text(encoding="utf-8"))

    def test_archive_record_excluded(self):
        path = put_record(self.root / "records", "pixel-art", "Old example",
                          "This is a discarded experiment.", ["test"], "review")
        item = json.loads(path.read_text(encoding="utf-8"))
        item["status"] = "archived"
        path.write_text(json.dumps(item), encoding="utf-8")
        data, notes = build_snapshot(self.root)
        self.assertEqual(json.loads(data)["record_count"], 0)
        self.assertNotIn("Old example", notes)

    def test_open_order_is_listed(self):
        order_dir = self.root / "orders"
        order_dir.mkdir()
        (order_dir / "test.json").write_text(json.dumps({
            "id": "work-order-test", "title": "Review module", "owner": "Atlas",
            "status": "active", "priority": "high"
        }), encoding="utf-8")
        data, notes = build_snapshot(self.root)
        self.assertEqual(json.loads(data)["open_order_count"], 1)
        self.assertIn("Review module", notes)

    def test_invalid_record_prevents_bad_export(self):
        p = self.root / "records" / "bad.json"
        p.parent.mkdir()
        p.write_text('{"id":"invalid"}', encoding="utf-8")
        with self.assertRaises(ValueError):
            refresh(self.root)


if __name__ == "__main__":
    unittest.main()
