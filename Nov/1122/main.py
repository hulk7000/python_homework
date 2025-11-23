import random
from get_number import get_number 
from message_dic import message_dic
from add_record_to_db import Record_game
from class_pratice2_model import *
# print(random.choice(message_dic.get("win_messages")))

# Start game
print(random.choice(message_dic.get("greetings")))
print(random.choice(message_dic.get("start_message")))
username = input('plz input your username : ')

secret_number = random.randint(1, 100)
guess = 0
guess_count = 0

while guess != secret_number:
    guess = get_number("Take a guess: ")

    # Player asked for the answer
    if guess == "ANSWER":
        print(f"🕵️ SECRET NUMBER = {secret_number}")
        continue  # Keep playing

    guess_count += 1

    if guess < secret_number:
        print(random.choice(message_dic.get("hints_low")))
    elif guess > secret_number:
        print(random.choice(message_dic.get("hints_high")))

# Winning message
print(random.choice(message_dic.get("win_messages")))
print("The secret number was:", secret_number)
print(f"{username} guessed it in {guess_count} tries! 🎯")

w = Record_game(username,guess_count)
w.add_record()