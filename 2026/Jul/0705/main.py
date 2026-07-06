from guess_number_game import *
from rock_paper_sizzer_game import *


def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")

        choice = input("Choose an option (1/2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            play_rps()  #
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()