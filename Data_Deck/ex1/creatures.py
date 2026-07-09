from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Oddish(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Oddish", "Grass/Poison")

    def attack(self) -> str:
        return "Oddish uses Absorb!"

    def heal(self) -> str:
        return "Oddish heals itself using Synthesis!"


class Bellossom(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bellossom", "Grass")

    def attack(self) -> str:
        return "Bellossom dances through a Petal Dance!"

    def heal(self) -> str:
        return "Bellossom heals itself and others with Synthesis!"


class Zorua(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Zorua", "Dark")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Zorua strikes harder using its Night Daze!"
        return "Zorua strikes from the shadows with Feint Attack!"

    def transform(self) -> str:
        self.is_transformed = True
        return "Zorua slips into an illusion form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Zorua drops the illusion!"


class Zoroark(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Zoroark", "Dark")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Zoroark unleashes Night Daze at full power!"
        return "Zoroark uses Dark Pulse!"

    def transform(self) -> str:
        self.is_transformed = True
        return "Zoroark creates a powerful illusion form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Zoroark shatters the illusion!"
