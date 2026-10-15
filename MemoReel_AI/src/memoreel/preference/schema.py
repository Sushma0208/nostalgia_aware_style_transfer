"""Minimal validated schema for one pairwise candidate comparison."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class PreferenceRecord:
    participant_id: str
    source_image_id: str
    candidate_a_id: str
    candidate_b_id: str
    intended_mood: str
    selected_aesthetic: str
    preferred_candidate_id: str | None
    consent_reference: str
    interaction_sequence: int
    feedback_timestamp: datetime | None = None
    optional_reason: str | None = None

    def validate(self) -> None:
        """Raise ValueError when identifiers or comparison fields are invalid."""
        required = {
            "participant_id": self.participant_id,
            "source_image_id": self.source_image_id,
            "candidate_a_id": self.candidate_a_id,
            "candidate_b_id": self.candidate_b_id,
            "intended_mood": self.intended_mood,
            "selected_aesthetic": self.selected_aesthetic,
            "consent_reference": self.consent_reference,
        }
        for name, value in required.items():
            if not value or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if self.candidate_a_id == self.candidate_b_id:
            raise ValueError("candidate IDs must be different")
        if self.preferred_candidate_id not in (None, self.candidate_a_id, self.candidate_b_id):
            raise ValueError("preferred_candidate_id must identify candidate A, B, or be None")
        if self.interaction_sequence < 0:
            raise ValueError("interaction_sequence must be non-negative")
        if self.feedback_timestamp is not None and not isinstance(self.feedback_timestamp, datetime):
            raise ValueError("feedback_timestamp must be a datetime or None")
