class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_level() -> None:
    raise WaterError("Not enough water in the tank!")


def tester() -> None:
    print("\nTesting PlantError...")
    try:
        plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        water_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    tester()
