# Assignment 4 - Problem 4- Hangman Game
# Abdullah Khan - 30074457
# Raiyan Sarwar - 30075746

# hangman.py is the module which handles the visual aspect of this game
import hangman
import sys, random, stdio

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

secretWord = ["_"] * len(randomWord)
wrongGuesses = []
correctGuesses = []

def checkIfInt(val):
    try:
        check = int(val)
    except ValueError:
        return False

def turn(guess):
    global guesses, wrongGuesses, correctGuesses, letters, secretWord
    # if number of guesses remaining > 0
    if guesses > 0:
        if guess in letters and not guess in wrongGuesses and not guess in correctGuesses and checkIfInt(guess) == False and guess.isalpha():
            letterIndices = [index for index, letter in enumerate(randomWord) if letter == guess]
            for i in range(len(letterIndices)):
                secretWord[letterIndices[i]] = guess
            hangman.displayMessage(3, 13, "Nice guess!", 32)
            correctGuesses.append(guess)
        elif guess == "" or len(guess) > 1 or not checkIfInt(guess) == False or not guess.isalpha():
            hangman.displayMessage(7, 13, "Enter a valid letter (which you have not guessed before).", 22)
        elif guess in wrongGuesses or guess in correctGuesses:
            hangman.displayMessage(5, 13, "You have already guessed this letter before...", 22)
        else:
            hangman.displayMessage(4, 13, "Sorry, there is no \"{}\" in the word".format(guess), 22)
            wrongGuesses.append(guess)
            guesses -= 1
        if secretWord.count("_") == 0:
            hangman.displayMessage(7, 11, "Good job, you guessed the word correctly!", 32)
        hangman.displayMessage(3, 19, "What's your guess?", 22)
        if len(wrongGuesses) > 0:
            hangman.displayMessage(3.5, 9, "Your wrong guesses so far:", 22)
            hangman.displayMessage(3, 7, " ".join([str(letter) for letter in wrongGuesses]), 36)
    hangman.drawHangman(wrongGuesses)

while guesses >= 0:
    hangman.displaySecretWord(secretWord)
    hangman.showCanvas()
    if not secretWord.count("_") == 0 and not guesses == 0:
        turn(input("Your guess: "))
    elif guesses == 0:
        hangman.displayMessage(8, 19, "You ran out of guesses! The secret word was: \"{}\"".format(randomWord), 29)
        hangman.drawHangman(wrongGuesses)
    else:
        # hangman.displaySecretWord(secretWord)
        hangman.displayMessage(10, 10,"Good job, you guessed the word correctly!", 33)
