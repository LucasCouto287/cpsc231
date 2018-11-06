# Assignment 4 - Problem 3 - Console Hangman
# Abdullah Khan - 30074457
# Raiyan Sarwar - 30075746

import sys, random

lexicon = open(sys.argv[1])
# remove newline character from beside each word in the lexicon and make a list with those words
allWords = [word.rstrip() for word in lexicon]
lexicon.close()

wordsToPickFrom = []

# only append words with more than 4 characters to the new list
for i in range(len(allWords)):
    if len(allWords[i]) >= 4:
        wordsToPickFrom.append(allWords[i])

guesses = 8
# pick a random word from the new list
randomWord = random.choice(wordsToPickFrom)
# letters in the randomWord, sorted alphabetically
letters = ''.join(sorted(randomWord))

print("Welcome to Console Hangman!")

secretWord = ["_"] * len(randomWord)
wrongGuesses = []
correctGuesses = []

def checkIfInt(val):
    try:
        check = int(val)
    except ValueError:
        return False

while guesses > 0:
    print("\nThe secret word looks like:", " ".join([str(letter) for letter in secretWord]))
    if len(wrongGuesses) > 0:
        print("Your wrong guesses so far:", " ".join([str(letter) for letter in wrongGuesses]))
    # "guesses" if you have more than one left, else "guess"
    print("You have", guesses, "wrong guess{} remaining".format("es" if guesses > 1 else ""))
    guess = input("What is your guess? ")
    if guess in letters and not guess in wrongGuesses and not guess in correctGuesses and checkIfInt(guess) == False and guess.isalpha():
        letterIndices = [index for index, letter in enumerate(randomWord) if letter == guess]
        for i in range(len(letterIndices)):
            secretWord[letterIndices[i]] = guess
        print(" - Nice guess!")
        correctGuesses.append(guess)
    elif guess == "" or len(guess) > 1 or not checkIfInt(guess) == False or not guess.isalpha():
        print(" - Enter a valid letter (which you have not guessed before).")
    elif guess in wrongGuesses or guess in correctGuesses:
        print(" - You have already guessed this letter before...")
    else:
        print(" - Sorry, there is no \"{}\" in the word".format(guess))
        wrongGuesses.append(guess)
        guesses -= 1
        if guesses == 0 :
            print(" - You ran out of guesses! The secret word was: \"{}\"".format(randomWord))
    if secretWord.count("_") == 0:
        print("\n - Good job, you guessed the word correctly!")
        print(" - Secret word:", randomWord)
        break
