import random
from DB_database import *
from DB_model import *


def get_number(prompt):

    while True:
        answer = input(prompt).strip().lower()

        if answer == "answer":
            return "ANSWER"

        if answer.isdigit():
            return int(answer)

        print("Please enter a number!")


def play_guess():

    def get_messages(category):
        messages = session.query(Message.content).filter(
            Message.category == category
        ).all()

        return [m[0] for m in messages]


    greetings = get_messages("greetings")
    start_messages = get_messages("start_message")
    hints_low = get_messages("hints_low")
    hints_high = get_messages("hints_high")
    win_messages = get_messages("win_messages")


    if not greetings:
        print("No messages found!")
        return


    print(random.choice(greetings))
    print(random.choice(start_messages))


    player_name = input("Enter your name: ")


    # Check balance before betting
    pre_balance = User_record.get_latest_balance(player_name)

    print(f"\nCurrent Balance: {pre_balance}")


    if pre_balance <= 0:
        print("❌ You don't have enough balance to play.")
        return


    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))


            if bet_amount <= 0:
                print("Bet must be greater than 0.")
                continue


            if bet_amount > pre_balance:
                print("❌ Bet exceeds your balance.")
                continue


            break


        except ValueError:
            print("Enter a valid number.")



    secret_number = random.randint(1, 100)

    guess = 0
    tries = 0
    guess_list = []


    while guess != secret_number:

        guess = get_number("Guess a number (1-100): ")


        if guess == "ANSWER":
            print(f"Secret number is {secret_number}")
            continue


        tries += 1
        guess_list.append(guess)


        if guess < secret_number:
            print(random.choice(hints_low))


        elif guess > secret_number:
            print(random.choice(hints_high))



    print(random.choice(win_messages))


    print(f"Secret number: {secret_number}")
    print(f"You got it in {tries} tries!")
    print("Your guesses:", guess_list)



    if tries <= 7:

        win_amount = bet_amount * 2
        result = "Win"

        print("🎉 You doubled your money!")


    else:

        win_amount = -bet_amount
        result = "Lose"

        print("😢 Too many tries. You lost your bet!")



    new_balance = pre_balance + win_amount


    print(f"\nBefore Balance: {pre_balance}")
    print(f"Current Balance: {new_balance}")



    game_record = Record_game(
        player_name=player_name,
        bet_amount=bet_amount,
        balance=new_balance,
        tries=tries,
        input_info=str(guess_list),
        win_amount=win_amount,
        result=result
    )


    game_record.add_record()



    User_record(
        player_name,
        win_amount
    ).update_balance()



if __name__ == "__main__":
    play_guess()