# Assignment 2 - Problem 7 - Solitaire Pig
# Abdullah Khan - 30074457
# Suhaib Tariq - 30075751

import random
import sys

# list to hold all the turn scores
turnScoreCounter = []
# variable to count for one turn's score
turnScoreCount = 0
# variable to record the index of each turn
index = 0

def simulateTurn():
    global turnScoreCount
    global index
    points = 0
    turnScore = []
    while points <= 20:
        dice = random.randint(1, 6)
        if dice == 1:
            points = 0
            print("- rolled a 1, pigged out!")
            print("turn score:", points)
            print("current score:", turnScoreCount)
            break
        print("- rolled a", dice)
        points += dice
        turnScoreCounter.append(dice)
        if sum(turnScoreCounter) >= (20 * (index + 1)):
            turnScoreCount += sum(turnScoreCounter)
            print("turn score:", sum(turnScoreCounter))
            print("current score:", turnScoreCount)
            break

print("")

currentScore = turnScoreCount
def finalTurn():
    neededToWin = 100 - turnScoreCount
    points = 0
    global currentScore
    while points <= neededToWin:
        dice = random.randint(1, 6)
        if dice == 1:
            print("")
            print("- rolled a 1, pigged out!")
            points = 0
            break
        print("- rolled a", dice)
        points += dice
    print("turn score:", points)
    currentScore = turnScoreCount + points
    print("current score:", currentScore)


while turnScoreCount <= 80:
    print("")
    simulateTurn()
    turnScoreCounter.clear()

while currentScore < 100:
    finalTurn()
