import random

def game2():
    game2 = random.randint(1,100)
    attempts = 0
    print('Guess the number between 1 and 100')
    while True:
        try:
            guess = int(input('Your guess: '))
            attempts += 1
            if guess < game2:
                print('Your guess is too low.')
            elif guess > game2:
                print('Your guess is too high.')
            else:
                print('Correct! Your guess it in {} attempts.'.format(attempts))
                break
        except ValueError:
            print('Please enter a valid number.')
game2()
#5