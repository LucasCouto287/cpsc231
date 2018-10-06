# Assignment 2 - Problem 9 - Computer vs. Player
# Abdullah Khan - 30074457
# Suhaib Tariq - 30075751

import random

humanScore = []
points1 = 0
turnScorePlayer = []

def humanTurn():
    global humanScore
    global points1
    global turnScorePlayer
    print("")
    # print("It's your turn:")
    if sum(humanScore) <= 100 and not sum(computerScore) >= 100:
        playerInput = input("(r)oll or (h)old? ")
        if playerInput == "r" or playerInput == "":
             dice = random.randint(1,6)
             if dice == 1:
                 print("pigged out, 1 was rolled!")
                 # points1 = 0
                 # turnScorePlayer.append(points)
                 print("your current score:", sum(humanScore))
                 if sum(computerScore) <= 100 and not sum(humanScore) >= 100:
                     computerTurn()
                 else:
                    print("you win!")
             else:
                 # points1 += dice
                 turnScorePlayer.append(dice)
                 print("- rolled a", dice)
                 if sum(humanScore) <= 100 and not sum(computerScore) >= 100:
                     humanTurn()
                 else:
                     print("computer wins...")
        elif playerInput ==  "h":
            print("turn score:", sum(turnScorePlayer))
            humanScore.append(sum(turnScorePlayer))
            print("your current score:", sum(humanScore))
            turnScorePlayer.clear()
            if sum(computerScore) <= 100 and not sum(humanScore) >= 100:
                computerTurn()
            else:
                print("computer wins...")
    else:
        print("you win!")

computerScore = []
index = 0
def computerTurn():
    print("\n")
    print("It's the computer's turn:")
    global computerScore
    global index
    turnScoreComp = []
    points = 0
    if sum(computerScore) <= 100 and not sum(humanScore) >= 100:
        while points <= 20 and sum(computerScore) <= 100:
            dice = random.randint(1, 6)
            if dice == 1:
                points = 0
                print("- pigged out, rolled a 1!")
                print("turn score:", points)
                print("computer's current score:", sum(computerScore))
                print("\nIt's your turn:")
                if sum(humanScore) <= 100 and not sum(computerScore) >= 100:
                    humanTurn()
                else:
                    print("you win!")
                break
            else:
                print("- rolled a", dice)
                points += dice
                turnScoreComp.append(dice)
            if sum(turnScoreComp) >= (20 * (index + 1)):
                computerScore.append(sum(turnScoreComp))
                print("- hold")
                print("turn score:", sum(turnScoreComp))
                print("computer's current score:", sum(computerScore))
                turnScoreComp.clear()
                if sum(humanScore) <= 100 and not sum(computerScore) >= 100:
                    print("\nIt's your turn:")
                    humanTurn()
                else:
                    print("you win!")
    else:
        print("computer wins...")

pickTurn = random.randint(1, 2)

print("A game of Pig")

if sum(computerScore) <= 100 or sum(humanScore) <= 100:
    computerTurn() if pickTurn == 1 else print("\nIt's your turn:"), humanTurn()
