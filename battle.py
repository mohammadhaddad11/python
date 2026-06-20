from ex0 import FlameFactory, AquaFactory, CreatureFactory


def tester(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    f1_base = f1.create_base()
    f2_base = f2.create_base()

    print(f1_base.describe())
    print("VS")
    print(f2_base.describe())

    print("fight")
    print(f1_base.attack())
    print(f2_base.attack())


if __name__ == "__main__":
    fire = FlameFactory()
    water = AquaFactory()

    print("Testing factory")
    tester(fire)

    print("\nTesting factory")
    tester(water)

    print("\nTesting battle")
    battle(fire, water)
