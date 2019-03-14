import time
import sys
import random


choices = []
choices.append('rock')
choices.append('paper')
choices.append('scissors')
a = 0
print('Please press 1 to start and 2 to exit')
startChoice = input()
while a == 0:
    try:
        startChoice = int(startChoice)
        while startChoice != 1 and startChoice != 2:
            print('Please press 1 to start and 2 to exit')
            startChoice = int(input())
        a = 1
    except:
        print('Please press 1 to start and 2 to exit')
        startChoice = input()
        a = 0
if startChoice == 2:
    print('Goodbye')
    time.sleep(5)
    sys.exit()

print('How many rounds would you like to play: ')
rounds = input()
a = 0
userRounds = 0
computerRounds = 0
while a == 0:
    try:
        rounds = int(rounds)
        a = 1
    except:
        print('Please enter a number for how many rounds you would like to play: ')
        rounds = input()
        a = 0
for x in range (0,rounds):
    print('Please choose 1 for rock, 2 for paper and 3 for scissors: ')
    userChoice = input()
    while userChoice != '1' and userChoice != '2' and userChoice != '3':
        print('Please choose 1 for rock, 2 for paper and 3 for scissors: ')
        userChoice = input()
    computerChoice = random.randint(0,2)
    if userChoice == '1':
        if computerChoice == 0:
            print('You draw')
        elif computerChoice == 1:
            print('You lose')
            computerRounds = computerRounds + 1
        elif computerChoice == 2:
            print('You win')
            userRounds = userRounds + 1
    elif userChoice == '2':
        if computerChoice == 0:
            print('You win')
            userRounds = userRounds + 1
        if computerChoice == 1:
            print('You draw')
        if computerChoice == 2:
            print('You lose')
            computerRounds = computerRounds + 1
    elif userChoice == '3':
        if computerChoice == 0:
            print('You lose')
            computerRounds = computerRounds + 1
        if computerChoice == 1:
            print('You win')
            userRounds = userRounds + 1
        if computerChoice == 2:
            print('You draw')

if userRounds >= computerRounds - 1:
    print('You won')
elif userRounds <= computerRounds + 1:
    print('You lose')
else:
    print('You draw')
print('You won', userRounds, 'rounds')
print('The computer won', computerRounds, 'rounds')
time.sleep(3)
sys.exit()
