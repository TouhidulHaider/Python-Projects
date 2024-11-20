import random

def roll_dice():
    return random.randint(1,6)

players = int(input("No. of participants: "))
players_scores = [0 for _ in range(players)]

while True:
    for player in range(players):
        round_score = 0
        print(f"\nPlayer {player+1}'s turn.")

        while (players_scores[player]) < 50:
            response = input("Do you want to roll? (y/n): ")
            if response == 'y':
                dice = roll_dice()
                if dice == 1:
                    players_scores[player] -= round_score
                    print(f"Your rolled 1. So, your round score is O. Your total score {players_scores[player]}")
                    break
                else:
                    round_score += dice
                    players_scores[player] += dice
                    print(f"Your rolled {dice}. Your round score {round_score} \nYour total score {players_scores[player]}")
            else:
                break
        
        # players_scores[player] += round_score
        # print(f"Your total score {players_scores[player]}")
        if players_scores[player] >= 50:
            break
    if max(players_scores) >= 50:
        break

print(f"\nPlayers Scores: {players_scores}")
print(f"Winner🏆 Player {players_scores.index(max(players_scores))+1}")