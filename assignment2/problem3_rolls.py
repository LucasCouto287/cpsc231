# Assignment 2 - Problem 3 - Expected Rolls
# Abdullah Khan - 30074457

import sys, random

# number of rolls - input from terminal argument
rolls = int(sys.argv[1])

print("Rolling", rolls, "times...")

position = []

for index in range(rolls):
    dice = random.randrange(1,7)
    position.append(dice)

print("\n It took", position.index(1) + 1, "rolls to roll a 1")
