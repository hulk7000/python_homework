import random
from DB_database import Wheel_record, User_record

# (Color, Multiplier)
wheel = [
    ("Red", 2),
    ("Blue", 2),
    ("Green", 3),
    ("Yellow", 5),
    ("Black", 10),
    ("White", 0),
]


def wheel_bet():

    player_name = input("Enter player name: ")

    pre_balance = User_record.get_latest_balance(player_name)

    print(f"\nCurrent Balance: {pre_balance}")

    if pre_balance <= 0:
        print("❌ You don't have enough balance to play.")
        return None

    while True:
        try:
            bet_amount = int(input("Enter bet amount: "))

            if bet_amount <= 0:
                print("Bet must be greater than 0.")
                continue

            if bet_amount > pre_balance:
                print("❌ Bet exceeds your balance.")
                continue

            break

        except ValueError:
            print("Enter a valid number.")

    while True:

        chosen_color = input(
            "Choose Red, Blue, Green, Yellow, Black or White: "
        ).capitalize()

        if chosen_color in ["Red", "Blue", "Green", "Yellow", "Black", "White"]:
            break

        print("Invalid choice.")

    return player_name, bet_amount, chosen_color


def spin_wheel():

    return random.choice(wheel)


def wheel_result(chosen_color, wheel_color, multiplier, bet_amount):

    # White is the losing slot
    if wheel_color == "White":
        return -bet_amount, "Lose"

    # Correct guess
    if chosen_color == wheel_color:
        return bet_amount * multiplier, "Win"

    # Wrong guess
    return -bet_amount, "Lose"


def wheel_main():

    info = wheel_bet()

    if info is None:
        return

    player_name, bet_amount, chosen_color = info

    wheel_color, multiplier = spin_wheel()

    print(f"\nWheel landed on: {wheel_color}")

    if wheel_color != "White":
        print(f"Multiplier: x{multiplier}")

    win_amount, status = wheel_result(
        chosen_color,
        wheel_color,
        multiplier,
        bet_amount,
    )

    pre_balance = User_record.get_latest_balance(player_name)

    new_balance = pre_balance + win_amount

    print(f"\n{player_name} {status}!")
    print(f"Win Amount: {win_amount}")
    print(f"Previous Balance: {pre_balance}")
    print(f"Current Balance: {new_balance}")

    Wheel_record(
        player_name,
        bet_amount,
        pre_balance,
        new_balance,
        chosen_color,
        wheel_color,
        multiplier,
        win_amount,
        status,
    ).add_info()

    User_record(player_name, win_amount).update_balance()


if __name__ == "__main__":
    wheel_main()