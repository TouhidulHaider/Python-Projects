import random

def rolling_dice():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

# Choosing the players
players = 0
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Minimum 2 and maximum 4 players can participate. Try again.")
    else:
        print("Invalid..Try again.")

'''
Initializing maximum score to 50 
and list of players where the score of each player is set to 0
'''
max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_id in range (players):
        print(f"\nPlayer {player_id+1}'s turn just started")
        print("Your total score is: ", players_scores[player_id])
        
        round_score = 0
        while True:
            choice = input("Would you like to roll (y/n): ")
            if choice != 'y':
                break
            else:
                value = rolling_dice()
                if value == 1:
                    print("You rolled 1. Your turn is done. Your score in this round is 0")
                    round_score = 0
                    break
                else:
                    round_score += value
                    print(f"You rolled {value}")
                print(f"Your score in this round is {round_score}")

        players_scores[player_id] += round_score
        print("Your total score is", players_scores[player_id])
        if players_scores[player_id] >= 50:
            break

max_score = max(players_scores)
winner = players_scores.index(max_score) + 1

print(f"\nWinner🥇: player {winner} \n          Your total score {max_score}")
