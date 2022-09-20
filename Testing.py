def testguess(guesslist, corrlist):
    clue = ""
    word = ""
    for i in range(0, 5):
        word += guesslist[i]
        if guesslist[i] == corrlist[i]:
            # print("{} is in the correct spot".format(guesslist[i]))
            clue += "G"

        elif guesslist[i] in corrlist:
            # print("{} is here but in a different spot".format(guesslist[i]))
            clue += "Y"
        else:
            # print("{} is not in this word".format(guesslist[i]))
            clue += "-"

    print(word, " ", clue)
    return clue == "GGGGG"  # True if correct, False otherwise


tries = 0
correctans = "proxy"
corrlist = list(correctans)
print(corrlist)
guessed_correctly = False

while tries < 6 and not guessed_correctly:
    guess = str(input('Guess a five letter word: ')).strip()
    if len(guess) != 5:
        while True:
            print("Your guess must be 5 letters and letters ONLY: ")
            guess = str(input('Guess a five letter word: ')).strip()
            if len(guess) == 5:
                break
    while not guess.isalpha():
        print("Your guess must be 5 letters long")
        guess = str(input('Guess a five letter word: ')).strip()
    while not guess.islower():
        guess = guess.lower()
    guesslist = list(guess)
    tries += 1
    print("This is guess number {}".format(tries))
    guessed_correctly = testguess(guesslist, corrlist)

if tries == 6:
    print("Damn you suck")
