import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import github_runner as runner
from atlas_vi import AtlasVI


class AtlasIssueQueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.env = {"GITHUB_REPOSITORY": "founder/Atlas-Warehouse"}
        self.state = self.root / "issue_queue.json"
        self.original_atlas = AtlasVI
        self.replace_queue = patch.object(runner, "QUEUE_STATE", self.state)
        self.replace_atlas = patch.object(
            runner, "AtlasVI", lambda actor: self.original_atlas(root=self.root, actor=actor)
        )
        self.replace_queue.start()
        self.replace_atlas.start()
        self.addCleanup(self.replace_atlas.stop)
        self.addCleanup(self.replace_queue.stop)

    @staticmethod
    def item(number, name, text):
        return {"id": number, "user": {"login": name}, "body": text}

    def test_burst_intake_and_idempotent_replay(self):
        first = [
            self.item(20, "founder", "/atlas receive workflow | First lesson | Collect tests | lessons | Founder"),
            self.item(21, "someone-else", "/atlas status"),
            self.item(22, "founder", "/atlas receive workflow | Second lesson | Compare output | lessons | Founder"),
        ]
        with patch.object(runner, "issue_comments", return_value=first):
            replies = runner.process_pending_issue_commands(self.env, 2)
        self.assertEqual(len(replies), 2)
        self.assertIn("Shipment received", replies[0]["body"])
        self.assertIn("Shipment received", replies[1]["body"])
        self.assertEqual(json.loads(self.state.read_text())["last_processed_id"], 22)
        self.assertEqual(len(self.original_atlas(root=self.root).all_records()), 2)

        # A canceled pending workflow may replay the latest trigger.
        with patch.object(runner, "issue_comments", return_value=first):
            self.assertEqual(runner.process_pending_issue_commands(self.env, 2), [])
        self.assertEqual(len(self.original_atlas(root=self.root).all_records()), 2)

        second = first + [
            self.item(23, "github-actions[bot]", "Atlas replied."),
            self.item(24, "founder", "/atlas status"),
        ]
        with patch.object(runner, "issue_comments", return_value=second):
            followup = runner.process_pending_issue_commands(self.env, 2)
        self.assertEqual(len(followup), 1)
        self.assertIn("Inventory: **2 active**", followup[0]["body"])
        self.assertEqual(json.loads(self.state.read_text())["last_processed_id"], 24)

    def test_requires_same_issue(self):
        self.state.write_text(json.dumps({"issue_number": 2, "last_processed_id": 1}))
        with self.assertRaisesRegex(ValueError, "another console"):
            runner.process_pending_issue_commands(self.env, 3)


if __name__ == "__main__":
    unittest.main()
