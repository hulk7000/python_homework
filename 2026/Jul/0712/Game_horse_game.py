import time
import random
import sys
from colorama import init
from DB_database import Horse_record, User_record
import json
from datetime import datetime


def generate_times(num, total=30):

    base = total / num
    arr = [base + random.uniform(-1, 1) for _ in range(num)]  # Add random variation
    s = sum(arr)
    arr2 = [round(t * total / s, 2) for t in arr]  # Scale so the total equals `total`
    game_info = list(zip(range(1, num + 1), arr2))
    return arr2, game_info


def render_bar(p, bar_len=100):

    filled = int(p * bar_len)
    return "-" * (bar_len - filled) + "🐎" + "=" * filled


def race_animation(num_horses, CIRCLE, race_times):

    start_time = time.time()
    progress = [0] * num_horses
    finished = [False] * num_horses
    winner = None

    for _ in range(num_horses):
        print()

    while True:
        sys.stdout.write(f"\033[{num_horses}A")
        sys.stdout.flush()

        all_done = True

        for i in range(num_horses):
            if not finished[i]:
                pct = (time.time() - start_time) / race_times[i]

                if pct >= 1:
                    pct = 1
                    finished[i] = True

                    if winner is None:
                        winner = i + 1

                progress[i] = pct

            bar = render_bar(progress[i])
            percent = int(progress[i] * 100)

            sys.stdout.write(f"{CIRCLE[i]} {bar} {percent:3}%\n")
            sys.stdout.flush()

            if not finished[i]:
                all_done = False

        if all_done:
            break

        time.sleep(0.07)

    print(f"\n🏆 Winner: {CIRCLE[winner - 1]}")
    return winner

def horse_bet(num_horses):
    """
    Get player betting information.

    Returns:
        name: Player name
        amount: Bet amount
        choice: Selected horse number
    """
    name = input("Enter player name: ")

    while True:
        try:
            amount = int(input(f"{name}, enter your bet amount: "))

            if amount <= 0:
                print("The amount must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

    while True:
        try:
            choice = int(input(f"{name}, choose a horse to bet on (1-{num_horses}): "))
            if 1 <= choice <= num_horses:
                break
            else:
                print(f"Please enter a number between 1 and {num_horses}.")
        except ValueError:
            print("Please enter a valid number.")

    return name, amount, choice


def race_result(player_name, bet_amount, horse_choice, winner):

    if horse_choice == winner:
        win_amount = bet_amount * 2
        status = "Win"
    else:
        win_amount = -bet_amount
        status = "Lose"

    print(f"{player_name}, you {status}! Balance change: {win_amount}")

    return win_amount, status


def horse_main():
    init()

    num_horses = 6
    CIRCLE = [f"({i + 1})" for i in range(num_horses)]

    # Player places a bet
    player_name, bet_amount, horse_choice = horse_bet(num_horses)

    race_times, game_info = generate_times(num_horses)

    winner = race_animation(num_horses, CIRCLE, race_times)

    win_amount, status = race_result(
        player_name,
        bet_amount,
        horse_choice,
        winner,
    )

    rankings = sorted(game_info, key=lambda x: x[1])
    winner_house = rankings[0][0]
    winner_house_time = rankings[0][1]
    ranking_list = [horse for horse, _ in rankings]

    pre_balance = User_record.get_latest_balance(player_name)
    new_balance = pre_balance + win_amount

    print(f"{player_name} balance: {new_balance}")

    Horse_record(
        player_name,
        bet_amount,
        pre_balance,
        new_balance,
        horse_choice,
        win_amount,
        winner_house,
        winner_house_time,
        ranking_list,
        game_info,
        status,
    ).add_info()

    User_record(player_name, win_amount).update_balance()


if __name__ == "__main__":
    horse_main()