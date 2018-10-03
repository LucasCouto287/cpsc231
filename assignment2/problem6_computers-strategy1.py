# Assignment 2 - Problem 6 - The Computer's Strategy
# Abdullah Khan - 30074457
# Suhaib Tariq - 30075751

import random
import sys

points = int(sys.argv[1])

turnScore = []

while points >= 80:
    dice = random.randint(1, 6)
    turnScore.append(dice)
    if dice == 1:
        print("Rolled a 1, pigged out!")
        print("turn score = 0")
        points = 0
        break
    print("rolled a", dice)
    points += dice
    if points >= 100:
    	print("turn score", sum(turnScore))
    	print("new total score:", points)
    	break

scoreCounter = []

while points <= 79 and not points == 0:
    dice = random.randint(1, 6)
    if dice == 1:
        print("Rolled a 1, pigged out!")
        points = 0
        break
    print("rolled a", dice)
    points += dice
    scoreCounter.append(dice)
    if sum(scoreCounter) >= 20:
    	print("turn score:", sum(scoreCounter))
    	print("current score:", points)
    	break
