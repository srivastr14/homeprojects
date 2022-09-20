#! /usr/bin/env python3

import random

while True:
    print('How many dice are we rolling?')
    numDice = input()
    if not numDice.isdigit():
        while True:
            answer = str(input('That\'s... not a whole number. Do you want to roll again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print('Wow, read instructions.')
        if answer == 'y':
            continue
        else:
            print('Thanks for playing!')
            break
    print('')
    print('Here are the dice rolls!')
    final_sum = 0 
    for i in range(0,int(numDice)):
        roll = random.randint(1,6)
        print(roll)
        final_sum += roll
        if i == int(numDice) - 1:
            print('')
            print('The sum of your rolls is ' + str(final_sum))
        else:
            continue
    while True:
        answer = str(input('Do you want to roll again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print('invalid input')
    if answer == 'y':
        continue
    else:
        print('Thanks for playing!')
        break
    

    
