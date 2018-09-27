# Assignment 2 - Problem 2 - Expected Value
# Abdullah Khan - 30074457

import sys, random

# number of rolls - input from terminal argument
rolls = int(sys.argv[1])

# print message before outputting estimation;
print("Rolling", rolls, "times...")

total = 0
# roll x times and keep adding each roll result to the total (x = terminal argument, amount of rolls)
for index in range(rolls):
    dice = random.randrange(1, 7)
    total += dice

# print the average of all rolls as the estimated expectation
print("Estimated expectation:", total / rolls)
