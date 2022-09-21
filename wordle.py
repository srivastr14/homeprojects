import random


def testguess(guesslet, corrlet, board):
    clue = ""
    word = ""
    rem_keys = []
    letleft = []
    counterg = dict((x, guesslet.count(x)) for x in set(guesslet))
    counterc = dict((x, corrlet.count(x)) for x in set(corrlet))
    for i in range(0, 5):
        word += guesslet[i]
        if guesslet[i] == corrlet[i]:
            clue += "G"
        elif guesslet[i] in corrlet:
            guessy = guesslist[0:i + 1]
            if counterg[guesslet[i]] <= counterc[guesslet[i]] and guessy.count(guesslet[i]) <= counterc[guesslet[i]]:
                clue += "Y"
            elif counterg[guesslet[i]] <= counterc[guesslet[i]] < guessy.count(guesslet[i]):
                clue += "Y"
            elif counterg[guesslet[i]] > counterc[guesslet[i]] and guessy.count(guesslet[i]) > counterc[guesslet[i]]:
                print("hrer :", guesslet[i], i)
                clue += "-"
            elif counterg[guesslet[i]] > counterc[guesslet[i]] > guessy.count(guesslet[i]):
                print("it's from here :", guesslet[i], i)
                for k in range(0, 5):
                    if guesslet[k] == corrlet[k] and i == k:
                        clue += "Y"
                        break
                    elif guesslet[k] == corrlet[k] and i < k:
                        clue += "Y"
                        break
                    elif guesslet[k] == corrlet[k] and i > k:
                        clue += "-"
                        break
            elif counterg[guesslet[i]] > counterc[guesslet[i]] and guessy.count(guesslet[i]) == counterc[guesslet[i]]:
                print("just right :", guesslet[i], i)
                # This works perfectly for ender/under but NOT tithe/fifty...
                for k in range(0, 5):
                    if guesslet[k] == corrlet[k] and i <= k:
                        print("and here")
                        for x in range(0,5):
                            if counterg[guesslet[k]] > guessy.count(guesslet[i]) and guesslet[x] == corrlet[x]:
                                clue += "-"
                                break
                                for b in range(0,5):
                                    if counterc[guesslet[i]] <= guessy.count(guesslet[i]):

                            # clue += "-"
                            break
                        else:
                            clue += "Y"
                            break
                        break
                    elif guesslet[k] == corrlet[k] and i > k:
                        clue += "-"
                        break
                    # elif guesslet[k] == corrlet[k] and i == k:
                    #     clue += "Y"
                    #     break
        else:
            clue += "-"
            rem_keys.append(guesslet[i])
    print(word, " ", clue)
    for rem in rem_keys:
        if any(rem in letter for letter in board):
            letleft = [letter.replace(rem, "-") for letter in board]
            board = letleft
        else:
            letleft = board
    return clue == "GGGGG", clue, letleft  # True if correct, False otherwise


def makeguess():
    chosen = str(input('Guess a five letter word: ')).strip()
    chosen = chosen.lower()
    return chosen


def specialcase(guesslet, corrlet, i):
    clue = ""
    for k in range(0, 5):
        if guesslet[k] == corrlet[k] and i != k:
            print("the real problem")
            clue += "Y"
            break
        elif guesslet[k] == corrlet[k] and i == k:
            clue += "-"
            break
    return clue


keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
list_of_guesses = []
answer_list = []
dict_check = []
words_file = open("5words.txt")
dictionary = open("words.txt")
for words in words_file:
    new_word = words.strip()
    answer_list.append(new_word.lower())
for words in dictionary:
    new_word = words.strip()
    dict_check.append(new_word.lower())

tries = 0
# correctans = random.choice(answer_list)
correctans = "under"
corrlist = list(correctans)
guessed_correctly = False
pyramid = []

while tries < 6 and not guessed_correctly:
    guess = makeguess()
    while (guess in list_of_guesses) and tries > 0:
        print("You've already guessed this word!")
        guess = makeguess()
    while guess not in dict_check:
        print("Please select a real word")
        guess = makeguess()
    while not (guess.isalpha() and len(guess) == 5):
        print("Your guess must be 5 LETTERS ONLY")
        guess = makeguess()
    list_of_guesses.append(guess)
    guesslist = list(guess)
    tries += 1
    print("This is guess number {}".format(tries))
    guessed_correctly, clues, keys = testguess(guesslist, corrlist, keyboard)
    pyramid.append(clues)
    print(*keys, sep="\n")
    keyboard = keys

while guessed_correctly:
    print("Nice work! You got it! It was {}".format(correctans))
    print(*pyramid, sep="\n")
    break

if tries == 6 and not guessed_correctly:
    print("Damn you suck, the correct word was {}".format(correctans))
    print(*pyramid, sep="\n")
