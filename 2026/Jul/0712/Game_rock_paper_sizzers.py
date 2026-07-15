import random
from DB_database import *

def play_rps():

    choices = ["Rock", "Paper", "Scissors"]

    player_name = input("Enter your name: ")

    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
            if bet_amount <= 0:
                print("Bet must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    player_choice = input("Enter Rock, Paper or Scissors: ").capitalize()

    if player_choice not in choices:
        print("Invalid choice!")
        return

    bot_choice = random.choice(choices)

    print(f"Bot chose: {bot_choice}")

    if player_choice == bot_choice:
        result = "Tie"
        win_amount = 0
    elif (
        (player_choice == "Rock" and bot_choice == "Scissors")
        or (player_choice == "Paper" and bot_choice == "Rock")
        or (player_choice == "Scissors" and bot_choice == "Paper")
    ):
        result = "Win"
        win_amount = bet_amount
    else:
        result = "Lose"
        win_amount = -bet_amount

    before_balance = User_record.get_latest_balance(player_name)
    balance = before_balance + win_amount

    print(f"Result: {result}")
    print(f"Before Balance: {before_balance}")
    print(f"Balance: {balance}")

    game_record = RPS_record_game(
        player_name,
        bet_amount,
        balance,
        bot_choice,
        player_choice,
        win_amount,
        result,
    )

    game_record.add_info()

    User_record(player_name, win_amount).update_balance()

    session.close()