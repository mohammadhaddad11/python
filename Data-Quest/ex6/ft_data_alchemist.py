import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan','Emma', 'Gregory', 'john', 'kevin', 'Liam']
    cap_players = [player.capitalize() for player in players]
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized:{cap_players}")
    print(f"New list of capitalized names only:: {[player for player in players if player[0].isupper()]}")
    score_dict = {player: random.randint(0, 1000) for player in cap_players}
    print(f"Score dict: {score_dict}")
    avg = sum(score_dict.values())/len(score_dict)
    print(f"Score average is {avg:.2f}")
    high_scores = {player: score_dict[player] for player in score_dict if score_dict[player] > avg}
    print(f"High scores: {high_scores}")