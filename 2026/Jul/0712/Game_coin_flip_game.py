import random
from DB_database import Coin_flip_record, User_record


def coin_flip_bet():
    player_name = input("Enter player name: ")

    while True:
        try:
            bet_amount = int(input("Enter bet amount: "))
            if bet_amount <= 0:
                print("Bet must be greater than 0.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        player_choice = input("Choose Heads or Tails: ").capitalize()

        if player_choice in ["Heads", "Tails"]:
            break

        print("Please choose Heads or Tails.")

    return player_name, bet_amount, player_choice


def flip_coin():
    return random.choice(["Heads", "Tails"])


def coin_result(player_choice, coin, bet_amount):

    if player_choice == coin:
        win_amount = bet_amount
        status = "Win"
    else:
        win_amount = -bet_amount
        status = "Lose"

    return win_amount, status


def coin_flip_main():

    player_name, bet_amount, player_choice = coin_flip_bet()

    coin = flip_coin()

    print(f"\nCoin landed on: {coin}")

    win_amount, status = coin_result(
        player_choice,
        coin,
        bet_amount,
    )

    pre_balance = User_record.get_latest_balance(player_name)
    new_balance = pre_balance + win_amount

    print(f"{player_name} {status}!")
    print(f"Balance: {new_balance}")

    Coin_flip_record(
        player_name,
        bet_amount,
        pre_balance,
        new_balance,
        player_choice,
        coin,
        win_amount,
        status,
    ).add_info()

    User_record(player_name, win_amount).update_balance()


if __name__ == "__main__":
    coin_flip_main()