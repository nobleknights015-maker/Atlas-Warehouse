import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from atlas_vi import AtlasVI, PERSONA
from atlas_warehouse import iter_records, make_id
from github_runner import event_command


class AtlasVITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.atlas = AtlasVI(self.root)

    def test_persona_and_help(self):
        self.assertEqual(PERSONA["identity"], "Atlas")
        self.assertIn("younger brother", PERSONA["relationship"])
        self.assertIn("👍", self.atlas.handle("hello"))
        self.assertIn("Warehouse Director", self.atlas.handle("status"))
        self.assertIn("Work order", self.atlas.handle("help").title())
        self.assertIn("Sentinel", self.atlas.handle("team"))
        self.assertIn("deterministic VI", self.atlas.handle("about"))

    def test_inventory_lifecycle(self):
        result = self.atlas.handle(
            "receive pixel-art | Gait baseline | Check six articulated legs. | gait, legs | Founder review"
        )
        self.assertIn("Shipment received", result)
        record_id = make_id("pixel-art", "Gait baseline")
        self.assertTrue((self.root / "records" / "pixel-art" / (record_id + ".json")).exists())
        self.assertIn("Gait baseline", self.atlas.handle("find gait"))
        self.assertIn("unverified", self.atlas.handle("inspect " + record_id))
        self.assertIn("reviewed", self.atlas.handle(
            "review " + record_id + " | reviewed | Founder checked silhouette"
        ))
        self.assertIn("reviewed", self.atlas.handle("inspect " + record_id))
        self.assertIn("Gait baseline", self.atlas.handle("handoff legs"))
        self.assertIn("Pixel", self.atlas.handle("catalog").title())
        self.assertIn("archive inventory", self.atlas.handle(
            "archive " + record_id + " | Superseded by new baseline"
        ))
        self.assertNotIn("Gait baseline", self.atlas.handle("find gait"))
        self.assertIn("archived", self.atlas.handle("inspect " + record_id))
        self.assertIn("receive", self.atlas.handle("audit"))
        self.assertEqual(len(list(iter_records(self.root / "records"))), 1)

    def test_work_order_lifecycle(self):
        command = "order add Validate sprite sheet | Test pixel grid alignment | Vera | high"
        result = self.atlas.handle(command)
        self.assertIn("Work order", result)
        order_id = make_id("work-order", "Validate sprite sheet")
        self.assertIn("queued", self.atlas.handle("order list"))
        self.assertIn("active", self.atlas.handle("order start " + order_id))
        self.assertIn("blocked", self.atlas.handle("order block " + order_id + " | Waiting on samples"))
        self.assertIn("active", self.atlas.handle("order start " + order_id))
        self.assertIn("done", self.atlas.handle("order done " + order_id + " | CI passed"))
        self.assertIn("queued", self.atlas.handle("order reopen " + order_id + " | New samples arrived"))
        item = json.loads((self.root / "orders" / (order_id + ".json")).read_text())
        self.assertEqual(len(item["history"]), 6)
        self.assertEqual(item["owner"], "Vera")
        self.assertIn("queued", self.atlas.handle("order list queued"))

    def test_invalid_commands_do_not_mutate(self):
        bad = [
            "receive secret | title | summary | tag | source",
            "receive pixel-art | title | summary | tags",
            "order add build a thing | details | Atlas | emergency",
            "order done non-existent | evidence",
            "review nonexistent | tested | tests",
        ]
        for command in bad:
            self.assertIn("Nothing was changed", self.atlas.handle(command))
        self.assertEqual(self.atlas.all_orders(), [])
        self.assertEqual(self.atlas.all_records(), [])
        self.assertFalse(self.atlas.audit.exists())

    def test_bad_state_transition_and_maintenance(self):
        self.atlas.handle("order add Bad dependency | Need data | Auren | critical")
        order_id = make_id("work-order", "Bad dependency")
        self.assertIn("Nothing was changed", self.atlas.handle("order done " + order_id + " | no tests"))
        self.assertIn("Critical open orders: 1", self.atlas.handle("status"))
        self.assertIn("No issues detected", self.atlas.handle("maintenance"))
        self.assertIn("Inspection", self.atlas.handle("maintenance"))

    def test_no_duplicate_order_and_no_unverified_claim(self):
        command = "order add Audit audit | Check storage | Atlas | normal"
        self.assertIn("opened", self.atlas.handle(command))
        self.assertIn("Duplicate", self.atlas.handle(command))
        self.atlas.handle("receive workflow | Audit routine | Run checks | ops | Team report")
        self.assertIn("unverified", self.atlas.handle("maintenance"))

    def test_alias_and_length_limit(self):
        self.assertIn("Warehouse status", self.atlas.handle("/atlas status"))
        self.assertIn("Warehouse status", self.atlas.handle("Atlas: status"))
        self.assertIn("too long", self.atlas.handle("a" * 3000))


class GitHubBridgeTests(unittest.TestCase):
    def setUp(self):
        self.env = {"GITHUB_REPOSITORY": "founder/Atlas-Warehouse",
                    "GITHUB_EVENT_NAME": "issue_comment"}
        self.comment = {"comment": {"user": {"login": "founder"}, "body": "/atlas status"},
                        "issue": {"number": 42}}

    def test_owner_issue_command(self):
        self.assertEqual(event_command(self.env, self.comment), ("/atlas status", "founder", 42))

    def test_public_issue_comment_rejection(self):
        event = json.loads(json.dumps(self.comment))
        event["comment"]["user"]["login"] = "outsider"
        with self.assertRaises(PermissionError):
            event_command(self.env, event)
        event = json.loads(json.dumps(self.comment))
        event["issue"]["pull_request"] = {"url": "https://example.test/pr"}
        with self.assertRaises(PermissionError):
            event_command(self.env, event)
        event = json.loads(json.dumps(self.comment))
        event["comment"]["body"] = "hello atlas"
        with self.assertRaises(ValueError):
            event_command(self.env, event)

    def test_dispatch_and_schedule(self):
        dispatch = dict(self.env, GITHUB_EVENT_NAME="workflow_dispatch", GITHUB_ACTOR="founder",
                        ATLAS_COMMAND="order list")
        self.assertEqual(event_command(dispatch, {})[:2], ("order list", "founder"))
        schedule = dict(self.env, GITHUB_EVENT_NAME="schedule")
        self.assertEqual(event_command(schedule, {})[0], "maintenance")


if __name__ == "__main__":
    unittest.main()
