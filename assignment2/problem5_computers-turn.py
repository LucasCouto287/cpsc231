# Assignment 2 - Problem 5 - The Computer's Turn
# Abdullah Khan - 30074457
# Suhaib Tariq - 30075751

import random

points = 0

while points <= 20:
    dice = random.randint(1, 6)
    if dice == 1:
        print("pigged out!")
        points = 0
        break
    print("rolled a", dice)
    points += dice

print("turn score:", points)
