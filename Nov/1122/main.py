from play_guess_game import *  # Assuming play_game() is defined here
from rock_paper_scissor_game import *  # Assuming play_rps() is defined here
from speed_type import *
import play_house_game
from car_game import *  # <-- import your car game here

def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")
        print("3. Play speed type game")
        print("4. Play horse game")
        print("5. Play car spelling race game")  # <-- added option
        print("0. Exit")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            play_game()  # Guess game
        elif choice == "2":
            play_rps()  # Rock-paper-scissors
        elif choice == "3":
            play_speed_typing()  # Speed typing game
        elif choice == "4":
            play_house_game.horse_main()  # Horse game
        elif choice == "5":
            car_main()  # Car spelling race game
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()
