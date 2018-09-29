# Assignment 2 - Problem 3 - Expected Rolls
# Abdullah Khan - 30074457

import sys, random

# number of turns to simulate - input from terminal argument
turns = int(sys.argv[1])

# a list to hold all the number or rolls before pigging out
# should equal to the number of turns to simulate ("turns" variable)
counterList = []

# simulate one turn until pigging out
def simulateTurn():
    counter = 0
    dice = 0
    while not dice == 1:
        dice = random.randint(1, 6)
        counter += 1
    counterList.append(counter)

for index in range(turns):
    simulateTurn()

print("Simulating", turns, "turns...")
print("Estimated number of rolls before pigging out:", sum(counterList) / float(len(counterList)))
