#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__height = 0
        else:
            self.__height = height
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
            self.__age = 0
        else:
            self.__age = age

    def get_height(self) -> int:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__age)

    def set_height(self, new_height: int) -> None:
        if (new_height < 0):
            print("")
            print("Invalid operation attempted: "
                  f"height {new_height}cm [REJECTED]"
                  )
            print("Security: Negative height rejected\n")
            return
        self.__height = new_height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print("")
            print(f"Invalid operation attempted: age {new_age}days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        self.__age = new_age
        print(f"Age updated: {self.__age} days [OK]")

    def get_info(self) -> str:
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.get_info()}")
