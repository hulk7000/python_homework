from play_guess_game import *  # Assuming play_game() is defined here
from rock_paper_scissor_game import *  # Assuming play_rps() is defined here
from speed_type import *
import play_house_game

def display_menu():
    while True:  # Keep showing the menu in a loop until the user exits
        # Display the main menu options
        print("\n--- Main Menu ---")
        print("1. Play guess game")
        print("2. Play rock paper scissors game")  # Assuming you have a guessing game here
        print("3. Play speed type game")  # You can implement this to view past results
        print("4. Play horse game")  # You can implement this to view past results

        print("0. Exit")

        # Get user choice
        choice = input("Choose an option (1/2/3/4): ")

        # Handle the user's choice
        if choice == "1":
            play_game()  # Call the function to play Rock-Paper-Scissors
        elif choice == "2":
            play_rps()  # Call the function to play another game (e.g., guessing game)
        elif choice == "3":
            play_speed_typing()
            # Implement the functionality to view previous results if necessary
        elif choice == "4":
            play_house_game.horse_main()
        elif choice == "0":
            print("Exiting the game. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please select a valid option.")

# Ensure this function is called when the script is executed
if __name__ == "__main__":
    display_menu()  # This will display the menu when the script starts
