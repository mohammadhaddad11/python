#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int) -> None:
        self.height += amount

    def add_age(self, days: int) -> None:
        self.age += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def growth_print(self, before_height: int) -> str:
        return f"Growth this week: +{self.height - before_height}cm"

    def display(self) -> None:
        print(self.get_info())


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    week_days = 6
    week_growth = 6
    print("=== Day 1 ===")
    rose.display()
    for day in range(7, 26, 7):
        before_height = rose.height

        rose.grow(week_growth)
        rose.add_age(week_days)

        print(f"=== Day {day} ===")
        rose.display()
        print(rose.growth_print(before_height))
