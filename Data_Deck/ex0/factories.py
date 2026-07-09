from abc import ABC, abstractmethod
from .creature import Creature, Charmander, Charizard, Squirtle, Blastoise


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Charmander()

    def create_evolved(self) -> Creature:
        return Charizard()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Squirtle()

    def create_evolved(self) -> Creature:
        return Blastoise()
