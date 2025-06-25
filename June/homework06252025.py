import random

choices = ['rock', 'paper', 'scissor']
user_Score = 0
computer_Score = 0

for _ in range(3):
    user = input('choose rock, paper, or scissor: ').lower()
    computer = random.choice(choices)
    print(f'Computer chose {computer}')

    if user == computer:
        pass
    elif (user == 'rock' and computer == 'scissor') or \
        (user == 'paper' and computer == 'rock') or \
        (user == 'scissor' and computer == 'paper'):
        user_Score += 1
    else:
        computer_Score += 1

if user_Score > computer_Score:
    print('You won!')
elif computer_Score < user_Score:
    print('You lost!')
else:
    print('Draw!')

#10