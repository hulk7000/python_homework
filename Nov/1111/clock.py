import time
import os

def countdown_timer(minutes, seconds):
    # Convert total time to seconds
    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        # Calculate remaining minutes and seconds
        mins, secs = divmod(total_seconds, 60)


        # Format the countdown as MM:SS
        time_format = f"{mins:02}:{secs:02}"

        # Clear the screen (for clean updates, works in most terminals)
        os.system('cls')

        # Display the remaining time
        print(f"\r{time_format}", end='', flush=True)

        # Wait for 1 second
        time.sleep(1)

        # Decrement the total seconds
        total_seconds -= 1

    print("\nTime's up!")


# Example: Set a 2 minutes 30 seconds timer
countdown_timer(2, 0)
