# Assignment 4 - Problem 1 - Word Lookup
# Abdullah Khan - 30074457

import sys

lexicon = open(sys.argv[1])
inputWord = str(sys.argv[2])
# remove newline character from beside each word in the lexicon
words = [word.rstrip() for word in lexicon]
lexicon.close()

def ordinal(n):
    # encode the suffixes "th st nd rd" for values of n from 0 - 3; then map the value of n to te index of the suffix
    return "%d%s" % (n,"tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

if inputWord in words:
    print(("\"{}\" is the {} most common word in contemporary American English.").format(inputWord, ordinal(words.index(inputWord) + 1)))
else:
    print("Sorry, \"%s\" is not one of the 4000 most common words of contemporary American English." % inputWord)

letters = ' '.join(sorted(set(inputWord)))

print("It consists of the following {}:\n {}".format("letters" if len(inputWord) > 1 else "letter", letters))
