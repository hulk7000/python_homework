import os
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from class_pratice2_model import Guess_game, Message

# -----------------------------
# Database setup
# -----------------------------
db_path = os.path.join(os.path.dirname(__file__), 'guessgame.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# -----------------------------
# Game record class
# -----------------------------
class Record_game:
    def __init__(self, play_name, tries, input_info):
        self.play_name = play_name
        self.tries = tries
        self.input_info = input_info

    def add_record(self):
        """Add a player's game record to the database."""
        entry = Guess_game(
            play_name=self.play_name,
            tries=self.tries,
            input_info=self.input_info
        )
        session.add(entry)
        session.commit()
        print(f"✅ Added game record: {self.play_name} ({self.tries}) {self.input_info}")

# -----------------------------
# Messages helper function
# -----------------------------
def add_message(category, content):
    """Add a message to the database."""
    entry = Message(category=category, content=content)
    session.add(entry)
    session.commit()
    print(f"✅ Saved message: [{category}] {content}")

# -----------------------------
# Create tables
# -----------------------------
Base.metadata.create_all(engine)

# -----------------------------
# Get messages directly from DB
# -----------------------------
def get_messages(category):
    """Fetch all messages for a given category from the database."""
    messages = session.query(Message.content).filter(Message.category == category).all()
    return [m[0] for m in messages]  # extract strings from tuples

# -----------------------------
# Guessing game helpers
# -----------------------------
def get_number(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans == "":
            print("Please type a number! 😊")
            continue
        if ans == "answer":
            return "ANSWER"
        if not ans.isdigit():
            print("Only numbers allowed! 🔢")
            continue
        return int(ans)

# -----------------------------
# Main guessing game logic
# -----------------------------
def play_game():
    greetings = get_messages("greetings")
    start_messages = get_messages("start_message")
    hints_low = get_messages("hints_low")
    hints_high = get_messages("hints_high")
    win_messages = get_messages("win_messages")

    if not (greetings and start_messages and hints_low and hints_high and win_messages):
        print("⚠️ Some message categories are empty. Please populate the database first!")
        return

    print(random.choice(greetings))
    print(random.choice(start_messages))

    username = input("Please enter your username: ")
    secret_number = random.randint(1, 100)
    guess = 0
    guess_count = 0
    guess_list = []

    while guess != secret_number:
        guess = get_number("Take a guess: ")
        if guess == "ANSWER":
            print(f"🕵️ SECRET NUMBER = {secret_number}")
            continue

        guess_count += 1
        guess_list.append(guess)

        if guess < secret_number:
            print(random.choice(hints_low))
        elif guess > secret_number:
            print(random.choice(hints_high))

    print(random.choice(win_messages))
    print(f"The secret number was: {secret_number}")
    print(f"{username} guessed it in {guess_count} tries! 🎯")
    print("Your guesses:", guess_list)

    # Save game record
    record = Record_game(username, guess_count, str(guess_list))
    record.add_record()
    return
# -----------------------------
# Run the game
# -----------------------------

if __name__ == '__main__':
    print("hulk is lazy")