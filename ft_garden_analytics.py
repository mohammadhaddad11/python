#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.height}cm, {self.age} days"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        r: float = self.trunk_diameter / 10
        shadow_area: float = (r**2) * (3.14)
        print(f"{self.name}"
              f" provides {int(shadow_area)} square meters of shade")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")

    print(f"{rose.name} (Flower): {rose.get_info()}, {rose.color} color")
    rose.bloom()
    print()
    print(
        f"{sunflower.name} (Flower): {sunflower.get_info()}, "
        f"{sunflower.color} color"
    )
    sunflower.bloom()

    print("\n")

    oak = Tree("Oak", 500, 1825, 50)
    evergreen = Tree("Evergreen", 300, 900, 25)

    print(
        f"{oak.name} (Tree): {oak.get_info()}, "
        f"{oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()
    print()
    print(
        f"{evergreen.name} (Tree): {evergreen.get_info()}, "
        f"{evergreen.trunk_diameter}cm diameter"
    )
    evergreen.produce_shade()

    print("\n")

    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "C")
    carrot = Vegetable("Carrot", 40, 60, "winter harvest", "A")

    print(
        f"{tomato.name} (Vegetable): {tomato.get_info()}, "
        f"{tomato.harvest_season}"
    )
    tomato.show_nutrition()
    print()
    print(
        f"{carrot.name} (Vegetable): {carrot.get_info()}, "
        f"{carrot.harvest_season}"
    )
    carrot.show_nutrition()
