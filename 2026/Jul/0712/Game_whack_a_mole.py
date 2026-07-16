import random
from DB_database import *

def play_whack():

    player = input("Player name: ")

    while True:
        try:
            bet = int(input("Bet amount: "))

            if bet <= 0:
                print("Bet must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    if bet <= 0:
        print("Bet must be greater than 0.")
        return

    pre_balance = User_record.get_latest_balance(player)

    if bet > pre_balance:
        print("Insufficient balance.")
        return

    hits = 0
    misses = 0

    print("\n===== Whack-a-Mole =====")
    print("A mole appears in a hole numbered 1-9.")
    print("Type the correct number to whack it!\n")

    for round_num in range(1, 11):

        mole = random.randint(1, 9)

        print(f"\nRound {round_num}")
        print(f"Mole appears at hole {mole}")

        answer = input("Whack: ")

        if answer == str(mole):
            print("Hit!")
            hits += 1
        else:
            print("Miss!")
            misses += 1

    score = hits * 10

    if hits >= 7:
        status = "Win"
        win_amount = bet * 2
    elif hits >= 5:
        status = "Draw"
        win_amount = 0
    else:
        status = "Lose"
        win_amount = -bet

    new_balance = pre_balance + win_amount

    Whack_record(
        player,
        bet,
        pre_balance,
        new_balance,
        hits,
        misses,
        score,
        win_amount,
        status,
    ).add_info()

    User_record(player, win_amount).update_balance()

    print("\n===== Game Over =====")
    print(f"Hits: {hits}")
    print(f"Misses: {misses}")
    print(f"Score: {score}")
    print(f"Result: {status}")
    print(f"Win Amount: {win_amount}")
    print(f"Previous Balance: {pre_balance}")
    print(f"New Balance: {new_balance}")

    session.close()

if __name__ == "__main__":
    play_whack()