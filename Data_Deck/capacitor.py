from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing_tester(factory: HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transform_tester(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healer = HealingCreatureFactory()
    transformer = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    healing_tester(healer)

    print("\nTesting Creature with transform capability")
    transform_tester(transformer)
