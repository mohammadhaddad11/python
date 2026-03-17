#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age

    def grow(self, amount: int) -> None:
        self.height += amount

    def age(self, days: int) -> None:
        self.age_in_days += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_in_days} days old"


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for plant in plants:
        plant.grow(6)
        plant.age(6)

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())