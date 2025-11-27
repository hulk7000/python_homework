import time
import random
from add_record_to_db import Type_record

def play_speed_typing():
    print("🔥 Welcome to the Typing Speed Challenge!")

    username = input("Enter your username: ")

    words = ["banana", "python", "school", "laptop", "keyboard", "challenge"]
    target = random.choice(words)

    print(f"\nType the following word as fast as you can:")
    print(f"👉  {target}")

    input("\nPress ENTER when you're ready...")

    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time

    if typed == target:
        print(f"\n🎉 Correct! You typed it in {time_taken:.2f} seconds.")
        status = "Correct"
    else:
        print("\n❌ Incorrect!")
        print(f"You typed: {typed}")
        print(f"Correct word was: {target}")
        print(f"Time taken: {time_taken:.2f} seconds")
        status = "Incorrect"

    # Save to database
    record = Type_record(username, time_taken, typed, status)
    record.add_info()
    print("\n💾 Your result has been saved!")
