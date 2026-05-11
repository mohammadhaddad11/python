import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")

        cord = text.split(",")

        if len(cord) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(cord[0])
            y = float(cord[1])
            z = float(cord[2])
            return (x, y, z)
        except ValueError as error:
            print(f"Invalid number: {error}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    point1 = get_player_pos()

    x1, y1, z1 = point1
    print(f"Got a first tuple: {point1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_to_center = round(math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2), 4)

    print(f"Distance to center: {distance_to_center}")

    print("\nGet a second set of coordinates")
    point2 = get_player_pos()

    x2, y2, z2 = point2
    distance_between = round(math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")