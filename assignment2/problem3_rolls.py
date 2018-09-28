# Assignment 2 - Problem 3 - Expected Rolls
# Abdullah Khan - 30074457

import sys, random

# number of rolls - input from terminal argument
rolls = int(sys.argv[1])

print("Rolling", rolls, "times...")

rolledNums = []

for index in range(rolls):
    dice = random.randrange(1,7)
    rolledNums.append(dice)

# print("\n It took", rolledNums.index(1) + 1, "rolls to roll the first 1")
# print("\n 1 was rolled", rolledNums.count(1), "times")

if 1 in rolledNums:
    print("\n Estimated expectation:", rolls / rolledNums.count(1))
else:
    print("1 wasn't rolled")
