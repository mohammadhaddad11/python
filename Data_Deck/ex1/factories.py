from ex0.factories import CreatureFactory
from ex1.creatures import Oddish, Bellossom, Zorua, Zoroark


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Oddish:
        return Oddish()

    def create_evolved(self) -> Bellossom:
        return Bellossom()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Zorua:
        return Zorua()

    def create_evolved(self) -> Zoroark:
        return Zoroark()
