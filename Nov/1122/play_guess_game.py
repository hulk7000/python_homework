import os
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from message_dic import message_dic

# -----------------------------
# Database setup
# -----------------------------
db_path = os.path.join(os.path.dirname(__file__), 'guessgame.db')
engine = create_engine(f"sqlite:///{db_path}", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# -----------------------------
# Guess game record table
# -----------------------------
class Guess_game(Base):
    __tablename__ = "guess_game"
    id = Column(Integer, primary_key=True, autoincrement=True)
    play_name = Column(String, nullable=False)
    tries = Column(Integer, nullable=False)
    input_info = Column(String, nullable=False)

# -----------------------------
# Messages table
# -----------------------------
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)

    @staticmethod
    def add_message(category, content):
        exists = session.query(Message).filter(
            Message.category == category,
            Message.content == content
        ).first()
        if not exists:
            entry = Message(category=category, content=content)
            session.add(entry)
            session.commit()

# -----------------------------
# Create tables if missing
# -----------------------------
Base.metadata.create_all(engine)

# -----------------------------
# Populate messages from message_dic
# -----------------------------
for category, messages in message_dic.items():
    for msg in messages:
        Message.add_message(category, msg)

print("🎉 All messages have been saved to the database!")

# -----------------------------
# Helper to get messages
# -----------------------------
def get_messages(category):
    """Return list of messages for category from DB."""
    db_msgs = [m[0] for m in session.query(Message.content).filter(Message.category == category).all()]
    return db_msgs

# -----------------------------
# Record game class
# -----------------------------
class Record_game:
    def __init__(self, play_name, tries, input_info):
        self.play_name = play_name
        self.tries = tries
        self.input_info = input_info

    def add_record(self):
        entry = Guess_game(
            play_name=self.play_name,
            tries=self.tries,
            input_info=self.input_info
        )
        session.add(entry)
        session.commit()
        print(f"✅ Added game record: {self.play_name} ({self.tries}) {self.input_info}")

# -----------------------------
# Helper to get user input
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
# Main guessing game
# -----------------------------
def play_game():
    print(random.choice(get_messages("greetings")))
    print(random.choice(get_messages("start_message")))

    username = input("Enter your username: ")
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
            print(random.choice(get_messages("hints_low")))
        elif guess > secret_number:
            print(random.choice(get_messages("hints_high")))

    print(random.choice(get_messages("win_messages")))
    print(f"The secret number was: {secret_number}")
    print(f"{username} guessed it in {guess_count} tries! 🎯")
    print("Your guesses:", guess_list)

    # Save the game record
    record = Record_game(username, guess_count, str(guess_list))
    record.add_record()

# -----------------------------
# Run game
# -----------------------------
if __name__ == "__main__":
    play_game()
