from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> list[str]:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' for this normal strategy"
            )
        return [entity.attack()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, HealCapability)

    def act(self, entity: Creature) -> list[str]:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' "
                "for this defensive strategy"
            )
        healer = cast(HealCapability, entity)
        return [entity.attack(), healer.heal()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> list[str]:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' "
                "for this aggressive strategy"
            )
        transformer = cast(TransformCapability, entity)
        return [transformer.transform(), entity.attack(),
                transformer.revert()]
