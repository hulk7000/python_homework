import random
from add_record_to_db import *
from class_pratice2_model import *

def play_rps():
    choices = ["Rock", "Paper", "Scissors"]

    player_choice = input("Enter Rock, Paper or Scissors: ").capitalize()

    if player_choice not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        return

    bot_choice = random.choice(choices)
    print(f"Bot chose: {bot_choice}")

    # Determine result
    if player_choice == bot_choice:
        result = "Tie"
        print("It's a tie!")
    elif (player_choice == "Rock" and bot_choice == "Scissors") or \
         (player_choice == "Paper" and bot_choice == "Rock") or \
         (player_choice == "Scissors" and bot_choice == "Paper"):
        result = "Win"
        print("You win!")
    else:
        result = "Lose"
        print("You lose!")

    # Save to database
    game_record = RPS_record_game(bot_choice, player_choice, result)
    game_record.add_info()

    session.close()
