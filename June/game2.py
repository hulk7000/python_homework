import random

def game2():
    game = random.randint(1, 100)
    attempts = 0
    print('Guess the number between 1 and 100')
    while True:
        try:
            guess = int(input('Your guess: '))
            attempts += 1
            if guess < game:
                print('Your guess is too low.')
            elif guess > game:
                print('Your guess is too high.')
            else:
                print('Correct! You guessed it in {} attempts.'.format(attempts))
                break
        except ValueError:
            print('Please enter a valid number.')

game2()
#5