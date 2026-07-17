import random
from colorama import init
from DB_database import *


ITEMS = [
    "Coin",
    "Key",
    "Ring"
]


def guess_bet():
    """
    Get player betting information.
    """

    name = input("Enter player name: ")

    pre_balance = User_record.get_latest_balance(name)

    print(f"\nCurrent Balance: {pre_balance}")

    if pre_balance <= 0:
        print("❌ You don't have enough balance to play.")
        return None

    while True:
        try:
            amount = int(input(f"{name}, enter your bet amount: "))

            if amount <= 0:
                print("Bet must be greater than 0.")
                continue

            if amount > pre_balance:
                print("❌ Bet exceeds your balance.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    return name, amount


def choose_item():

    print("\nThe hand is holding ONE of these items:\n")

    for i, item in enumerate(ITEMS, start=1):
        print(f"{i}. {item}")

    while True:
        try:
            choice = int(input("\nChoose an item (1-3): "))

            if 1 <= choice <= len(ITEMS):
                return ITEMS[choice - 1]

            print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")


def guess_game():

    hidden_item = random.choice(ITEMS)

    print("\n🤚 A hand is hiding an item...")
    print("Can you guess what's inside?\n")

    player_choice = choose_item()

    return hidden_item, player_choice


def guess_result(player_choice, hidden_item, bet_amount):

    if player_choice == hidden_item:
        win_amount = bet_amount * 2
        result = "Win"

        print("\n🎉 Correct!")
        print(f"The hand contained a {hidden_item}.")

    else:
        win_amount = -bet_amount
        result = "Lose"

        print("\n❌ Wrong!")
        print(f"The hand contained a {hidden_item}.")

    print(f"Win amount: {win_amount}")

    return win_amount, result


def guess_main():

    init()

    bet_info = guess_bet()

    if bet_info is None:
        return

    player_name, bet_amount = bet_info

    hidden_item, player_choice = guess_game()

    win_amount, result = guess_result(
        player_choice,
        hidden_item,
        bet_amount,
    )

    pre_balance = User_record.get_latest_balance(player_name)
    new_balance = pre_balance + win_amount

    print(f"\nBefore Balance: {pre_balance}")
    print(f"Current Balance: {new_balance}")

    Guess_hand_record(
        player_name=player_name,
        bet_amount=bet_amount,
        pre_balance=pre_balance,
        new_balance=new_balance,
        player_choice=player_choice,
        hidden_item=hidden_item,
        win_amount=win_amount,
        status=result,
    ).add_info()

    User_record(
        player_name,
        win_amount
    ).update_balance()


if __name__ == "__main__":
    guess_main()