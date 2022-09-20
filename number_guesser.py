import random

print('Guess the number between 1 and 10, you get 3 tries')

number = int(random.randint(1,10))
guess = int(input())
tries = 3
while guess != number:
    tries = tries - 1
    if tries == 0:
        print('Sorry, you never got it! The answer was '+str(number))
        break
    if guess < number:
        print('You are too low! Guess again.')
        guess = int(input())
    elif guess > number:
        print('You are too high! Guess again.')
        guess = int(input())
else:
    print('Damn, you got it!')
        
