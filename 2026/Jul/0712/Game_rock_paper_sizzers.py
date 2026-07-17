import random
from DB_database import *


def play_rps():

    choices = ["Rock", "Paper", "Scissors"]

    player_name = input("Enter your name: ")


    # Check balance before betting
    pre_balance = User_record.get_latest_balance(player_name)

    print(f"\nCurrent Balance: {pre_balance}")


    if pre_balance <= 0:
        print("❌ You don't have enough balance to play.")
        return


    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))

            if bet_amount <= 0:
                print("Bet must be greater than 0.")
                continue

            if bet_amount > pre_balance:
                print("❌ Bet exceeds your balance.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")



    player_choice = input(
        "Enter Rock, Paper or Scissors: "
    ).capitalize()


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
        or
        (player_choice == "Paper" and bot_choice == "Rock")
        or
        (player_choice == "Scissors" and bot_choice == "Paper")
    ):

        result = "Win"
        win_amount = bet_amount


    else:

        result = "Lose"
        win_amount = -bet_amount



    new_balance = pre_balance + win_amount



    print(f"\nResult: {result}")
    print(f"Before Balance: {pre_balance}")
    print(f"Current Balance: {new_balance}")



    game_record = RPS_record_game(
        player_name,
        bet_amount,
        new_balance,
        player_choice,
        bot_choice,
        win_amount,
        result,
    )


    game_record.add_info()



    User_record(
        player_name,
        win_amount
    ).update_balance()



if __name__ == "__main__":
    play_rps()