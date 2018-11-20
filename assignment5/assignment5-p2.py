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

# all the possible game pieces
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
centerCoordinatesX = []
centerCoordinatesY = []

# append flags to the 2D grid (while taking care of three-in-a-row cases)
for outerIndex in range(len(grid)):
    for index in range(len(grid) - 2):
        randomFlag = str(random.choice(flags))
        # append the indices to create a coordinates list
        if outerIndex == 0:
            centerCoordinatesX.append((index + 1) * 2)
            # the y-coordinates are just the reverse of the x-coordinates with the addition of 16 & 18
            centerCoordinatesY = [18, 16] + centerCoordinatesX[::-1]
        # append the first two flags no matter if they are equal
        if len(grid[outerIndex]) < 2:
            grid[outerIndex].append(randomFlag)
        # check for equals now, starting from the third flag (horizontal only)
        elif len(grid[outerIndex]) >= 2:
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

# create a reversed version of the original grid (to check for verticals)
# when iterated over, the original grid's flags corresponded to the wrong indices for some reason, which is why this step is crucial
reversedGrid = grid[::-1]

# replace vertical duplicates (the same flag more than two-in-a-row) in all columns with other flags
column = 0
for outerIndex in range(7):
    for index in range(len(reversedGrid)):
        # check for vertical equals starting from the third flag in the column
        if index > 1:
            if reversedGrid[index][column] == reversedGrid[index - 1][column] and reversedGrid[index][column] == reversedGrid[index - 2][column]:
                flagsExcludingDuplicate = flags.copy()
                flagsExcludingDuplicate.remove(reversedGrid[index][column])
                reversedGrid[index][column] = random.choice(flagsExcludingDuplicate)
                del flagsExcludingDuplicate[:]
    column += 1

pictureGrid = []
# reverse the reversed grid to bring it back to normal
boardGrid = reversedGrid[::-1]
for index in range(len(grid)):
    for innerIndex in range(len(grid[index])):
        pictureGrid.append(boardGrid[index][innerIndex])

def showBoard():
    pictureIndex = 0
    for outerIndex in range(1, len(grid) + 1):
        for index in range(1, len(grid[outerIndex - 1]) + 1):
            pictureIndex += 1
            stddraw.picture(picture.Picture(pictureGrid[pictureIndex - 1] + ".png"), index * 2, outerIndex * 2)

stddraw.setPenColor(Color(30, 30, 30))

def drawNavigator():
    if stddraw.mousePressed():
        # get the closest center value from the list of center coordinates
        # (find the coordinates with the minimum distance from the mouse coordinates)
        x = min(centerCoordinatesX, key=lambda x:abs(x - stddraw.mouseX()))
        y = min(centerCoordinatesY, key=lambda y:abs(y - stddraw.mouseY()))
        stddraw.rectangle(x - 0.75, y - 0.75, 1.5, 1.5)

while True:
    showBoard()
    drawNavigator()
    stddraw.show(0)
