from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy, \
    AggressiveStrategy, InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, st1 = opponents[i]
            f2, st2 = opponents[j]
            c1 = f1.create_base()
            c2 = f2.create_base()
            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                print("\n".join(st1.act(c1)))
                print("\n".join(st2.act(c2)))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    water = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    s1 = NormalStrategy()
    s2 = DefensiveStrategy()
    s3 = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Charmander+Normal), (Healing+Defensive) ]")
    battle([(flame, s1), (healing, s2)])

    print("\nTournament 1 (error)")
    print("[ (Charmander+Aggressive), (Healing+Defensive) ]")
    battle([(flame, s3), (healing, s2)])

    print("\nTournament 2 (multiple)")
    print("[ (Squirtle+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(water, s1), (healing, s2), (transform, s3)])
