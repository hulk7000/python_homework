def game1():
    import random
    choices = ['rock','paper','scissor']
    user_Score = 0
    computer_Score = 0
    while user_Score <2 and computer_Score <2:
        while True:
            user = input('choose rock, paper, or scissor : ')
            if user in choices:
                break
            print('Invalid choice')
        computer = random.choice(choices)
        print(f'computer chose {computer}')

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
            print('Computer won')
        print(f'your score is {user_Score} and computer score is {computer_Score}')
    if user_Score > computer_Score:
        print('you won')
    elif user_Score < computer_Score:
        print('computer won')
    else:
        print('tie')
game1()

#10