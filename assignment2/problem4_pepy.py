# Assignment 2 - Problem 4 - Pepy's Problem
# Abdullah Khan - 30074457

import random

listOfOnes1 = []
listOfOnes2 = []

def simulateSixRolls():
    for index in range(6):
        dice = random.randint(1, 6)
        if dice == 1:
            listOfOnes1.append(dice)
    return (listOfOnes1.count(1))/ (6)


def simulateTwelveRolls():
    for index in range(12):
        dice = random.randint(1, 6)
        if dice == 1:
            listOfOnes2.append(dice)
    if len(listOfOnes2) >= 2:
        return (listOfOnes2.count(1)) / (12)
    else:
        return 0.0

prob1 = simulateSixRolls()
prob2 = simulateTwelveRolls()

print("Estimated likelihood of 1 once in 6 rolls:", prob1)
print("Estimated likelihood of 1 twice in 12 rolls:", prob2)

if prob1 < prob2:
    print("Therefore, 1 once in 6 rolls is less likely than 1 twice in 12 rolls")
elif(prob1 == prob2):
    print("Therefore, 1 once in 6 rolls has the same chances as 1 twice in 12 rolls")
else:
    print("Therefore, 1 once in 6 rolls is more likely than 1 twice in 12 rolls")
