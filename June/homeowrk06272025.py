def game1():
    import random
    choices = ['rock', 'paper', 'scissor']
    user_Score = 0
    computer_Score = 0
    while user_Score <2 and computer_Score <2:
        while True:
            user = input("Choose rock, paper, or scissor: ").lower()
            if user in choices:
                break
            print('Invalid choice. please choose only rock, paper, or scissor.')
        computer = random.choice(choices)
        print(f'Computer chose {computer}')

        if user == computer:
            print('Draw')
            pass
        elif (user == 'rock' and computer == 'scissor') or \
            (user == 'paper' and computer == 'rock') or \
            (user == 'scissor' and computer == 'paper'):
            user_Score += 1
            print('You won')
        else:
            computer_Score += 1
            print('computer wins')

        print(f'your score is {user_Score} and computer score is {computer_Score}')
    if user_Score > computer_Score:
        print('You won')
    elif user_Score < computer_Score:
        print('You lost')
    else:
        print('Draw')
game1()

#10