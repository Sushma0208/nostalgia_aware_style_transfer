import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from memoreel.preference.schema import PreferenceRecord


class PreferenceRecordTests(unittest.TestCase):
    def record(self, **changes):
        values = dict(
            participant_id="pseudonym-01", source_image_id="src-1",
            candidate_a_id="cand-a", candidate_b_id="cand-b",
            intended_mood="calm", selected_aesthetic="warm_analog",
            preferred_candidate_id="cand-a", consent_reference="consent-v1",
            interaction_sequence=0, feedback_timestamp=datetime.now(timezone.utc),
        )
        values.update(changes)
        return PreferenceRecord(**values)

    def test_valid_record(self):
        self.record().validate()

    def test_rejects_same_candidate_twice(self):
        with self.assertRaises(ValueError):
            self.record(candidate_b_id="cand-a").validate()

    def test_rejects_unlisted_winner(self):
        with self.assertRaises(ValueError):
            self.record(preferred_candidate_id="cand-c").validate()

    def test_allows_no_preference(self):
        self.record(preferred_candidate_id=None).validate()

    def test_requires_consent_reference(self):
        with self.assertRaises(ValueError):
            self.record(consent_reference=" ").validate()

    def test_rejects_negative_sequence(self):
        with self.assertRaises(ValueError):
            self.record(interaction_sequence=-1).validate()


if __name__ == "__main__":
    unittest.main()
