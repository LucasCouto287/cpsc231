# Assignment 2 - Problem 8 - Computer vs. Computer
# Abdullah Khan - 30074457
# Suhaib Tariq - 30075751

import random
import sys

p1TurnScoreCounter = []
p1TurnScore = []
p2TurnScoreCounter = []
p2TurnScore = []

index1 = 0
index2 = 0

def player1Turn():
    global p1TurnScore
    global index1
    global player2Turn
    if(sum(p1TurnScoreCounter) <= 100):
        print("")
        print("PLAYER 1")
    points = 0
    turnScore = []
    while points <= 20 and sum(p1TurnScoreCounter) <= 100:
        if sum(p1TurnScoreCounter) <= 100:
            dice = random.randint(1, 6)
        else:
            dice = 0
        if dice == 1:
            points = 0
            print("- rolled a 1, pigged out!")
            print("turn score:", points)
            print("P1 current score:", sum(p1TurnScoreCounter))
            player2Turn()
            break
        if sum(p1TurnScoreCounter) <= 100:
            turnScore.append(dice)
            print("- rolled a", dice)
            points += dice
    if sum(p1TurnScoreCounter) <= 100 and sum(turnScore) >= (20 * (index1 + 1)):
        # p1TurnScoreCounter.append(p1TurnScore[len(p1TurnScore) - 1])
        p1TurnScoreCounter.append(sum(turnScore))
        print("turn score:", sum(turnScore))
        print("P1 current score:", sum(p1TurnScoreCounter))
        player2Turn()
    turnScore.clear()

def player2Turn():
    global p2TurnScore
    global index2
    global player1Turn
    if(sum(p2TurnScoreCounter) <= 100):
        print("")
        print("PLAYER 2")
    points = 0
    turnScore = []
    while points <= 20 and sum(p2TurnScoreCounter) <= 100:
        if sum(p2TurnScoreCounter) <= 100:
            dice = random.randint(1, 6)
        else:
            dice = 0
        if dice == 1:
            points = 0
            print("- rolled a 1, pigged out!")
            print("turn score:", points)
            print("P2 current score:", sum(p2TurnScoreCounter))
            player1Turn()
            break
        if sum(p2TurnScoreCounter) <= 100:
            turnScore.append(dice)
            print("- rolled a", dice)
            points += dice
        if sum(turnScore) >= (20 * (index2 + 1)) and sum(p2TurnScoreCounter) <= 100:
            # p2TurnScoreCounter.append(p2TurnScore[len(p2TurnScore) - 1])
            p2TurnScoreCounter.append(sum(turnScore))
            print("turn score:", sum(turnScore))
            print("P2 current score:", sum(p2TurnScoreCounter))
            player1Turn()
    turnScore.clear()

while sum(p1TurnScoreCounter) <= 100 or sum(p2TurnScoreCounter) <= 100:
    player1Turn()
    player2Turn()
    if sum(p1TurnScoreCounter) >= 100 or sum(p2TurnScoreCounter) >= 100:
        print("\n")
        print("GAME OVER!")
        print("Player 1 score:", sum(p1TurnScoreCounter))
        print("Player 2 score:", sum(p2TurnScoreCounter))
        print("Player", "1" if sum(p1TurnScoreCounter) > sum(p2TurnScoreCounter) else "2", "wins!")
        break
