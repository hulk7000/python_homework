def get_number(prompt):
    """Gets a number or 'answer' from the user."""
    while True:
        answer = input(prompt).strip().lower()

        if answer == "":
            print("Please type a number! 😊")
            continue

        if answer == "answer":
            return "ANSWER"

        if not answer.isdigit():
            print("Only numbers allowed! Try again. 🔢")
            continue

        return int(answer)