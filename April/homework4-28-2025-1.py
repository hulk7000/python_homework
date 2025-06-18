import random
import re
choices = ['rock', 'paper', 'scissor']
computer = random.choice(choices)
user = input('Enter your choice(rock, paper, scissor): ')
if re.fullmatch(r"rock|paper|scissor",user):
    if user == 'rock':
        if computer == 'scissor':
             print(f'computer is {computer} , so You win')
        else:
             print(f'computer is paper , so You lose')
    elif user == 'scissor':
         if computer == 'paper':
             print(f'computer is {computer} , so You win')
         else:
             print(f'computer is rock , so You lose')
    elif user == 'paper':
        if computer == 'rock':
            print(f'computer is {computer} , so You win')
        else:
            print(f'computer is scissor , so You lose')
else:
    print("pls enter rock,paper,scissor")
