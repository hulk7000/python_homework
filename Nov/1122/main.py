from play_guess_game import *
from rock_paper_scissor_game import *
import play_house_game
from car_game import *
from truck_game import *
from snake_game import *
from running_game import *
from dog_game import *
from cat_game import *

def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")
        print("3. Play horse game")
        print("4. Play car spelling race game")
        print("5. Play truck game")
        print("6. Play snake game")
        print("7. Play running game")
        print("8. Play dog game")
        print("9. Play cat game")
        print("0. Exit")

        choice = input("Choose an option (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            play_game()  # Guess game
        elif choice == "2":
            play_rps()  #
        elif choice == "3":
            play_house_game.horse_main()  # Horse game
        elif choice == "4":
            car_main()
        elif choice == "5":
            truck_main()
        elif choice == "6":
            snake_main()
        elif choice == "7":
            running_main()
        elif choice == "8":
            dog_main()
        elif choice == "9":
            cat_main()
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()
