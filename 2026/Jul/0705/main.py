from guess_number_game import *
from rock_paper_sizzer_game import *
from horse_game import *

def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")
        print("3. Play horse game")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            play_guess()
        elif choice == "2":
            play_rps()
        elif choice == "3":
            horse_main()
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()