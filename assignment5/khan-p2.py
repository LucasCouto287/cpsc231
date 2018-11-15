# Assignment 5 - Problem 2 - Taffy Tangle
# Abdullah Khan - 30074457 - Tutorial 1
# Afnan Imran Chaudhry - 30077054 - Tutorial 10

import random, stddraw, picture
from color import Color

bg = Color(255, 255, 255)

# red = Color(255, 55, 75)
# green = Color(55, 255, 75)
# yellow = Color(245, 245, 55)
# blue = Color(50, 175, 255)
# purple = Color(145, 55, 255)
# orange = Color(255, 155, 70)
#
# colors = [red, green, yellow, blue, purple, orange]

flags = ["brazil", "canada", "china", "india", "usa", "pakistan"]

# set up the canvas
stddraw.setXscale(0.0, 16.0)
stddraw.setYscale(0.0, 20.0)
stddraw.setCanvasSize(750, 900)

grid = [[],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []]

# append flags to the 2D grid (while taking care of three-in-a-row cases)
for outerIndex in range(len(grid)):
    streak = 0
    for index in range(7):
        randomFlag = str(random.choice(flags))
        # append the first two flags no matter if they are equal
        if len(grid[outerIndex]) < 2:
            grid[outerIndex].append(randomFlag)
        # check for equals now, starting from the third flag (horizontal only)
        elif len(grid[outerIndex]) >= 2:

            # TODO: check for vertical equals
            if randomFlag == grid[outerIndex][index - 1] and randomFlag == grid[outerIndex][index - 2]:
                # make a copy of the flags list and then remove the duplicate flag from the new list
                # replace the duplicate flag on the grid with a random flag from the new list, then empty the new list
                flagsExcludingDuplicate = flags.copy()
                flagsExcludingDuplicate.remove(randomFlag)
                grid[outerIndex].append(random.choice(flagsExcludingDuplicate))
                del flagsExcludingDuplicate[:]
                # print("equal, flag = {}".format(randomFlag))
            else:
                grid[outerIndex].append(randomFlag)



        # if len(grid[outerIndex]) > 2:
        #     if randomFlag == grid[outerIndex][index - 2]:
        #         streak += 1
        #         # flags.remove(randomFlag)
        #         # newRandomFlag = random.choice(flags)
        #         # grid[outerIndex].append(newRandomFlag)
        #         # flags.append(randomFlag)
        #         print("same")
        #     elif streak < 2:
        #         grid[outerIndex].append(randomFlag)
        # else:
        #     grid[outerIndex].append(randomFlag)
    # print(len(grid[outerIndex]))

pictureGrid = []
for index in range(len(grid)):
    for innerIndex in range(len(grid[index])):
        pictureGrid.append(grid[index][innerIndex])

def generateBoard():
    pictureIndex = 0
    for outerIndex in range(1, len(grid) + 1):
        for index in range(1, len(grid[outerIndex - 1]) + 1):
            pictureIndex += 1
            stddraw.picture(picture.Picture(pictureGrid[pictureIndex - 1] + ".png"), index * 2, outerIndex * 2)
    # stddraw.setPenColor(random.choice(colors))
    # stddraw.filledCircle(8, 18, 0.6)

# while True:
generateBoard()
stddraw.show()
    # stddraw.clear(bg)
