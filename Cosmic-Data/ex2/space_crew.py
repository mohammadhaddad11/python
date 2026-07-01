from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")

        if not any(
                crew.rank in {Rank.commander, Rank.captain}
                for crew in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        exp_crew = 0

        for crew in self.crew:
            if crew.years_experience >= 5:
                exp_crew += 1

        exp_needed = (len(self.crew) + 1) // 2

        if self.duration_days > 365 and exp_crew < exp_needed:
            raise ValueError(
                "Long missions require experienced crew members")

        if any(not crew.is_active for crew in self.crew):
            raise ValueError(
                "Crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    valid_crew = SpaceMission(
        mission_id="M0001",
        mission_name="Mission 1",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=365,
        crew=[
            CrewMember(
                member_id="C01",
                name="Crew Member 1",
                rank=Rank.commander,
                age=30,
                specialization="Specialization 1",
                years_experience=10,
                is_active=True,
            )
        ],
        mission_status="planned",
        budget_millions=100.0,
    )

    print("Valid mission crew created:")
    print(f"ID: {valid_crew.mission_id}")
    print(f"Name: {valid_crew.mission_name}")
    print(f"Destination: {valid_crew.destination}")
    print(f"Launch Date: {valid_crew.launch_date}")
    print(f"Duration: {valid_crew.duration_days} days")
    print(f"Mission Status: {valid_crew.mission_status}")
    print(f"Budget: {valid_crew.budget_millions} million")
    print("Crew:")

    for crew in valid_crew.crew:
        print(
            f"- {crew.name} ({crew.rank.value}) - "
            f"{crew.specialization}"
        )

    print("=" * 40)

    try:
        SpaceMission(
            mission_id="M0002",
            mission_name="Mission 2",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=365,
            crew=[
                CrewMember(
                    member_id="C02",
                    name="Crew Member 2",
                    rank=Rank.officer,
                    age=30,
                    specialization="Specialization 2",
                    years_experience=10,
                    is_active=True,
                )
            ],
            mission_status="planned",
            budget_millions=100.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
