from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Plant")


class Bloomelle:
    def __init__(self):
        pass


class Shiftling:


class Morphagon: