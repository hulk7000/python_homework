from play_guess_game import *  # Assuming play_game() is defined here
from rock_paper_scissor_game import *  # Assuming play_rps() is defined here
from speed_type import *
import play_house_game
from car_game import *  # <-- import your car game here
from truck_game import *
from van_game import *
from turtle_game import *
from dog_game import *
from fish_game import *
from run_game import *
from robot_game import *
from eating_game import *
from snake_game import *
from cat_game import *
from frog_game import *

def display_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")
        print("3. Play speed type game")
        print("4. Play horse game")
        print("5. Play car spelling race game")
        print("6. Play truck game")
        print("7. Play van game")
        print("8. Play turtle game")
        print("9. Play dog game")
        print("10. Play fish game")
        print("11. Play run game")
        print("12. Play robot game")
        print("13. Play eating game")
        print("14. Play snake game")
        print("15. Play cat game")
        print("16. Play frog game")
        print("0. Exit")

        choice = input("Choose an option (1/2/3/4/5/6/7/8/10/11/12/13/14/15/16): ")

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
        elif choice == "6":
            truck_main()
        elif choice == "7":
            van_main()
        elif choice == "8":
            turtle_main()
        elif choice == "9":
            dog_main()
        elif choice == "10":
            fish_main()
        elif choice == "11":
            run_main()
        elif choice == "12":
            robot_main()
        elif choice == "13":
            eating_main()
        elif choice == "14":
            snake_main()
        elif choice == "15":
            cat_main()
        elif choice == "16":
            frog_main()
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    display_menu()
