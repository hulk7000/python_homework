from Game_guess_game import *
from Game_rock_paper_sizzers import *
from Game_horse_game import *
from Game_guess_hand_game import *
from Game_coin_flip_game import *

def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")
        print("3. Play horse game")
        print("4. Play guess hand game")
        print("0. Exit game")

        choice = input("Choose an option (1/2/3/4/5/0): ")

        if choice == "1":
            play_guess()
        elif choice == "2":
            play_rps()
        elif choice == "3":
            horse_main()
        elif choice == "4":
            guess_main()
        elif choice == "5":
            coin_flip_main()
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()