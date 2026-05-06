import random

def gen_player_achievements() -> set[str]:
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
        "Survivor"
    ]

    player_achievements = random.sample(achievements,  random.randint(1, 10))
    return set(player_achievements)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()

    print("Player Alice:", Alice)
    print("Player Bob:", Bob)
    print("Player Charlie:", Charlie)
    print("Player Dylan:", Dylan)
    print("\nAll distinct achievements:", Alice | Bob | Charlie | Dylan) 
    print("Common achievements:", Alice & Bob & Charlie & Dylan)
    only_alice = Alice - (Bob | Charlie | Dylan)
    print("only Alice has:", only_alice)
    only_bob = Bob - (Alice | Charlie | Dylan)
    print("only Bob has:", only_bob)
    only_charlie = Charlie - (Alice | Bob | Dylan)
    print("only Charlie has:", only_charlie)
    only_dylan = Dylan - (Alice | Bob | Charlie)
    print("only Dylan has:", only_dylan)
    print("\nAlice is missing:", (Bob | Charlie | Dylan) - Alice )
    print("Bob is missing:", (Alice | Charlie | Dylan) - Bob )
    print("Charlie is missing:", (Alice | Bob | Dylan) - Charlie )
    print("Dylan is missing:", (Alice | Bob | Charlie) - Dylan )