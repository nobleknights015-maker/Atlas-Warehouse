import sys
import tempfile
import unittest
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from atlas_warehouse import make_id, put_record, search_records, iter_records, validate_entry


class AtlasWarehouseTests(unittest.TestCase):
    def test_store_retrieve_search_and_update(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = put_record(root, "pixel-art", "Anatomy check",
                              "Verify that both legs are complete at native resolution.",
                              ["sprite", "anatomy"], "manual review", "reviewed")
            self.assertTrue(path.exists())
            entry = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(entry["id"], make_id("pixel-art", "Anatomy check"))
            self.assertEqual(validate_entry(entry), [])
            self.assertEqual(search_records(root, "legs")[0]["id"], entry["id"])
            self.assertEqual(len(list(iter_records(root))), 1)
            with self.assertRaisesRegex(ValueError, "already exists"):
                put_record(root, "pixel-art", "Anatomy check", "different",
                           [], "manual review")
            replacement = put_record(root, "pixel-art", "Anatomy check",
                                     "Check feet and joints as well as legs.",
                                     ["anatomy"], "second review", "tested", replace=True)
            updated = json.loads(replacement.read_text(encoding="utf-8"))
            self.assertEqual(updated["created_at"], entry["created_at"])
            self.assertEqual(updated["confidence"], "tested")
            self.assertEqual(len(list(iter_records(root))), 1)

    def test_empty_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "source"):
                put_record(Path(temp), "workflow", "Missing evidence",
                           "This should be rejected.", [], "")

    def test_long_titles_produce_valid_ids(self):
        from atlas_warehouse import validate_entry
        from datetime import datetime, timezone
        title = "Native pixel-art training and quality gate"
        record_id = make_id("pixel-art", title)
        self.assertNotIn("--", record_id)
        self.assertFalse(record_id.endswith("-"))
        with tempfile.TemporaryDirectory() as temp:
            path = put_record(Path(temp), "pixel-art", title, "Native-scale evaluation",
                              ["practice"], "Founder feedback")
            self.assertTrue(path.exists())
            self.assertEqual(validate_entry(json.loads(path.read_text(encoding="utf-8"))), [])

    def test_search_no_hits(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            put_record(root, "workflow", "Build check", "Run automated tests",
                       ["testing"], "CI results")
            self.assertEqual(search_records(root, "bananas"), [])


if __name__ == "__main__":
    unittest.main()
