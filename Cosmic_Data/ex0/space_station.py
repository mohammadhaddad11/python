from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, ConfigDict
from typing import Optional


class SpaceStation(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_data = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=95.0,
            oxygen_level=98.0,
            last_maintenance=datetime(2023, 1, 1, 0, 0, 0),
            notes="All systems nominal",
        )
        print("Valid station created:")
        print(f"ID: {valid_data.station_id}")
        print(f"Name: {valid_data.name}")
        print(f"Crew: {valid_data.crew_size} people")
        print(f"Power: {valid_data.power_level}%")
        print(f"Oxygen: {valid_data.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if valid_data.is_operational else 'Offline'}"
        )

        print("=" * 40)
    except ValidationError as e:
        print("Unexpected validation error:")
        print(e.errors()[0]["msg"])

    try:
        SpaceStation(
            station_id="ISS001",
            name="Invalid Station",
            crew_size=25,
            power_level=95.0,
            oxygen_level=98.0,
            last_maintenance=datetime(2023, 1, 1, 0, 0, 0),
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
