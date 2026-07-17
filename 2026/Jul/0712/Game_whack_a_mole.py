import random
import time
from colorama import init
from DB_database import Whack_record, User_record


def whack_bet():

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

    return player_name, bet_amount


def play_whack_game():

    holes = 5
    rounds = 10

    hits = 0
    misses = 0

    print("\n🐹 Whack a Mole!")
    print("Hit the mole by choosing the correct hole.")

    for i in range(rounds):

        mole_position = random.randint(1, holes)

        print(f"\nRound {i + 1}/{rounds}")
        print("Holes: 1 2 3 4 5")

        try:
            choice = int(input("Choose a hole: "))

        except ValueError:
            print("Invalid choice. You missed!")
            misses += 1
            continue


        if choice == mole_position:
            hits += 1
            print("🔨 HIT!")

        else:
            misses += 1
            print(f"❌ Miss! Mole was in hole {mole_position}")

        time.sleep(0.5)


    score = hits * 10

    print("\n===== Game Result =====")
    print(f"Hits: {hits}")
    print(f"Misses: {misses}")
    print(f"Score: {score}")

    return hits, misses, score



def calculate_reward(score, bet_amount):

    if score >= 70:
        win_amount = bet_amount * 2
        status = "Win"

    else:
        win_amount = -bet_amount
        status = "Lose"

    return win_amount, status



def play_whack():

    init()

    bet_info = whack_bet()

    if bet_info is None:
        return

    player_name, bet_amount = bet_info


    hits, misses, score = play_whack_game()


    win_amount, status = calculate_reward(
        score,
        bet_amount
    )


    pre_balance = User_record.get_latest_balance(player_name)
    new_balance = pre_balance + win_amount


    print(f"\n{player_name} {status}!")
    print(f"Win Amount: {win_amount}")
    print(f"Before Balance: {pre_balance}")
    print(f"Current Balance: {new_balance}")


    Whack_record(
        player_name,
        bet_amount,
        pre_balance,
        new_balance,
        hits,
        misses,
        score,
        win_amount,
        status,
    ).add_info()


    User_record(
        player_name,
        win_amount
    ).update_balance()



if __name__ == "__main__":
    play_whack()