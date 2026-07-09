from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Charmander(Creature):
    def __init__(self) -> None:
        super().__init__("Charmander", "Fire")

    def attack(self) -> str:
        return "Charmander uses Ember!"


class Charizard(Creature):
    def __init__(self) -> None:
        super().__init__("Charizard", "Fire/Flying")

    def attack(self) -> str:
        return "Charizard uses Flamethrower!"


class Squirtle(Creature):
    def __init__(self) -> None:
        super().__init__("Squirtle", "Water")

    def attack(self) -> str:
        return "Squirtle uses Water Gun!"


class Blastoise(Creature):
    def __init__(self) -> None:
        super().__init__("Blastoise", "Water")

    def attack(self) -> str:
        return "Blastoise uses Hydro Pump!"
