import random
import json
from get_number import get_number
from message_dic import message_dic
from add_record_to_db import Record_game
from class_pratice2_model import *

def play_game():
    print(random.choice(message_dic.get("greetings")))
    print(random.choice(message_dic.get("start_message")))

    username = input('plz input your username : ')
    secret_number = random.randint(1, 100)

    guess = 0
    guess_count = 0
    guess_list = []

    while guess != secret_number:
        guess = get_number("Take a guess: ")
        guess_list.append(guess)

        # Show the secret number if requested
        if guess == "ANSWER":
            print(f"🕵️ SECRET NUMBER = {secret_number}")
            continue

        guess_count += 1

        # Give hints
        if guess < secret_number:
            print(random.choice(message_dic.get("hints_low")))
        elif guess > secret_number:
            print(random.choice(message_dic.get("hints_high")))

    # Final messages
    print(random.choice(message_dic.get("win_messages")))
    print(f"The secret number was: {secret_number}")
    print(f"{username} guessed it in {guess_count} tries! 🎯")
    print("Your guesses:", guess_list)

    # Return data to be saved
    return username, guess_count, guess_list

def save_result(username, guess_count, guess_list):
    input_info_json = json.dumps(guess_list)  # convert list → JSON string

    w = Record_game(username, guess_count, input_info_json)
    w.add_record()

    print("✅ Game result saved to database.")

def main():
    username, guess_count, guess_list = play_game()
    save_result(username, guess_count, guess_list)

if __name__ == "__main__":
    main()
