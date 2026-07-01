from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def contact_validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact requires verification")
        if self.contact_type == ContactType.telepathic and \
                self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and (
                self.message_received is None or self.message_received.strip()
                == ""):
            raise ValueError("Strong signals require a received message")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    valid_data = AlienContact(
        contact_id="AC001",
        timestamp="2023-01-01T00:00:00",
        location="Mars",
        contact_type=ContactType.radio,
        signal_strength=8.0,
        duration_minutes=10,
        witness_count=5,
        message_received="Hello",
        is_verified=True,
    )

    print("Valid contact report:")
    print(f"ID: {valid_data.contact_id}")
    print(f"Type: {valid_data.contact_type.value}")
    print(f"Location: {valid_data.location}")
    print(f"Signal: {valid_data.signal_strength}/10")
    print(f"Duration: {valid_data.duration_minutes} minutes")
    print(f"Witnesses: {valid_data.witness_count}")
    print(f"Message: {valid_data.message_received}")
    print(f"Verified: {valid_data.is_verified}")

    print("=" * 40)

    try:
        AlienContact(
            contact_id="AC001",
            timestamp="2023-01-01T00:00:00",
            location="Mars",
            contact_type=ContactType.telepathic,
            signal_strength=8.0,
            duration_minutes=10,
            witness_count=1,
            message_received="Hello",
            is_verified=True,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
