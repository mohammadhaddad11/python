import random


def gen_player_achievements() -> set[str]:
    player_achievements = random.sample(
        achievements,
        random.randint(1, 10)
    )
    return set(player_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    achievements = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Survivor",
    "Hidden Path Finder"
]
    
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    all_achievements = set(achievements)

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    print("\nAll distinct achievements:", alice | bob | charlie | dylan)
    print("Common achievements:", alice & bob & charlie & dylan)

    print("Only Alice has:", alice - (bob | charlie | dylan))
    print("Only Bob has:", bob - (alice | charlie | dylan))
    print("Only Charlie has:", charlie - (alice | bob | dylan))
    print("Only Dylan has:", dylan - (alice | bob | charlie))

    print("\nAlice is missing:", all_achievements - alice)
    print("Bob is missing:", all_achievements - bob)
    print("Charlie is missing:", all_achievements - charlie)
    print("Dylan is missing:", all_achievements - dylan)