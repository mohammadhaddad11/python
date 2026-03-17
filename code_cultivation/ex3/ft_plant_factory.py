#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"

    def display(self) -> None:
        print(f"Created: {self.get_info()}")


def create_plants() -> list[Plant]:
    plant_data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants: list[Plant] = []

    for name, height, age in plant_data:
        plants.append(Plant(name, height, age))

    return plants


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = create_plants()

    for plant in plants:
        plant.display()

    print(f"\nTotal plants created: {len(plants)}")
