# Assignment 5 - Problem 2 - Taffy Tangle
# Abdullah Khan - 30074457 - Tutorial 1
# Afnan Imran Chaudhry - 30077054 - Tutorial 10

import random, stddraw, picture, math
from itertools import groupby
from color import Color
from time import sleep

bg = Color(35, 35, 35)

# all the possible game pieces
shapes = ["triangle", "circle", "parallelogram", "diamond", "star", "pentagon"]

# set up the canvas
stddraw.setXscale(0.0, 16.0)
stddraw.setYscale(0.0, 20.0)
stddraw.setCanvasSize(750, 900)

globalScore = []
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

# append shapes to the 2D grid (while taking care of three-in-a-row cases)
for outerIndex in range(len(grid)):
    for index in range(len(grid) - 2):
        randomShape = str(random.choice(shapes))
        # append the indices to create a coordinates list
        if outerIndex == 0:
            centerCoordinatesX.append((index + 1) * 2)
            # the y-coordinates are just the reverse of the x-coordinates with the addition of 16 & 18
            centerCoordinatesY = centerCoordinatesX[::-1] + [16, 18]
        # append the first two shapes no matter if they are equal
        if len(grid[outerIndex]) < 2:
            grid[outerIndex].append(randomShape)
        # check for equals now, starting from the third hape (horizontal only)
        elif len(grid[outerIndex]) >= 2:
            if randomShape == grid[outerIndex][index - 1] and randomShape == grid[outerIndex][index - 2] and grid[outerIndex][index - 2] == grid[outerIndex][index - 1]:
                # make a copy of the shapes list and then remove the duplicate hape from the new list
                # replace the duplicate hape on the grid with a random hape from the new list, then empty the new list
                shapesExcludingDuplicate = shapes.copy()
                shapesExcludingDuplicate.remove(randomShape)
                grid[outerIndex].append(random.choice(shapesExcludingDuplicate))
                del shapesExcludingDuplicate[:]
            else:
                grid[outerIndex].append(randomShape)

# create a reversed version of the original grid (to check for verticals)
# when iterated over, the original grid's shapes corresponded to the wrong indices for some reason, which is why this step is crucial
reversedGrid = grid[::-1]

# replace vertical duplicates (the same hape more than two-in-a-row) in all columns with other shapes
column = 0
for outerIndex in range(7):
    for index in range(len(reversedGrid)):
        # check for vertical equals starting from the third shape in the column
        if index >= 1:
            if reversedGrid[index][column] == reversedGrid[index - 1][column] and reversedGrid[index][column] == reversedGrid[index - 2][column]:
                shapesExcludingDuplicate = shapes.copy()
                shapesExcludingDuplicate.remove(reversedGrid[index][column])
                reversedGrid[index][column] = random.choice(shapesExcludingDuplicate)
                del shapesExcludingDuplicate[:]
    column += 1

stddraw.setPenColor(Color(220, 220, 220))

rectCoordinates = []
indices = []
shapesClickedOn = []
def drawNavigator(mouseX, mouseY):
    beforeSwap = boardGrid.copy()
    # get the closest center value from the list of center coordinates
    # aka finding the coordinates with the minimum distance from the mouse coordinates
    x = min(centerCoordinatesX, key=lambda x:abs(x - mouseX))
    y = min(centerCoordinatesY, key=lambda y:abs(y - mouseY))
    rectCoordinates.append((x - 0.875, y - 0.875))
    stddraw.rectangle(rectCoordinates[len(rectCoordinates) - 1][0], rectCoordinates[len(rectCoordinates) - 1][1], 1.75, 1.75)

    # to get the indices of the clicked shape
    indices.append((int(abs((y / 2) - 9)), int(x / 2) - 1))
    # get the shape using the indices above
    shapesClickedOn.append(reversedGrid[indices[len(indices) - 1][0]][indices[len(indices) - 1][1]])
    # sleep(0.3)
    swapShapes()

def swapShapes():
    global boardGrid
    # print(indices)
    print(indices)
    for index in range(len(indices) - 1):
        if (index) % 2 == 0 and len(rectCoordinates) % 2 == 0:
            # get the last two elements in the indices list (the two indices which need to be swapped)
            swapIndices = indices[-3:]
            # check if the shapes that need to be swapped are adjacent before swapping
            if ((abs(abs(indices[index][1]) - abs(indices[index - 1][1])) == 1 and (abs(indices[index][0] - indices[index - 1][0]) == 0)) or (abs(abs(indices[index][0] - abs(indices[index - 1][0])) == 1) and (abs(indices[index][1] - indices[index - 1][1]) == 0))) and not (abs(indices[index][1]) == abs(indices[index - 1][1]) and abs(indices[index][0]) == abs(indices[index - 1][0])):
                reversedGrid[swapIndices[index - 1][0]][swapIndices[index - 1][1]], reversedGrid[swapIndices[index][0]][swapIndices[index][1]] = reversedGrid[swapIndices[index][0]][swapIndices[index][1]], reversedGrid[swapIndices[index - 1][0]][swapIndices[index - 1][1]]
                boardGrid = reversedGrid[::-1]
                del swapIndices[:]
                del indices[:]
            else:
                del swapIndices[:]
                del indices[:]

    if checkForEquals():
        removeEquals()
        showBoard(boardGrid)
    else:
        showBoard(boardGrid)
        # print("revert back before swap")


# reverse the reversed grid to bring it back to normal
boardGrid = reversedGrid[::-1]

reversedBoardGrid = boardGrid[::-1]
def checkForEquals():
    global globalScore
    verticalColumn = 0
    for outerIndex in range(len(reversedBoardGrid)):
        consecutiveTaffies = [sum(1 for _ in group) for _, group in groupby(reversedBoardGrid[outerIndex])]
        for index in range(len(consecutiveTaffies)):
            if consecutiveTaffies[index] >= 3:
                # print("equal (horizontal), at indices", outerIndex + 1, index + 1)
                globalScore.append(consecutiveTaffies[index])
                return True
    for outerIndex in range(7):
        for index in range(len(reversedBoardGrid)):
            if index > 1:
                if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn]):
                    globalScore.append(3)
                    return True
                if index > 2:
                    if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn]):
                        globalScore.append(1)
                        return True
                if index > 3:
                    if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn] == reversedBoardGrid[index - 4][verticalColumn]):
                        globalScore.append(1)
                        return True
        verticalColumn += 1

def removeEquals():
    verticalColumn = 0
    for outerIndex in range(len(reversedBoardGrid)):
        consecutiveTaffies = [sum(1 for _ in group) for _, group in groupby(reversedBoardGrid[outerIndex])]
        for index in range(len(consecutiveTaffies)):
            if consecutiveTaffies[index] >= 3:
                # print("equal (horizontal), at indices", outerIndex + 1, index + 1)
                reversedBoardGrid[outerIndex][index] = ""
                reversedBoardGrid[outerIndex][index + 1] = ""
                reversedBoardGrid[outerIndex][index + 2] = ""
                if consecutiveTaffies[index] >= 4:
                    reversedBoardGrid[outerIndex][index + 1] = ""
                    reversedBoardGrid[outerIndex][index + 2] = ""
                    reversedBoardGrid[outerIndex][index + 3] = ""
                    # reversedBoardGrid[outerIndex][index + 4] = ""
    for outerIndex in range(7):
        for index in range(len(reversedBoardGrid)):
            if index > 1:
                if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn]):
                    reversedBoardGrid[index][verticalColumn] = ""
                    reversedBoardGrid[index - 1][verticalColumn] = ""
                    reversedBoardGrid[index - 2][verticalColumn] = ""
                if index > 2:
                    if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn]):
                        reversedBoardGrid[index - 1][verticalColumn] = ""
                        reversedBoardGrid[index - 2][verticalColumn] = ""
                        reversedBoardGrid[index - 3][verticalColumn] = ""
                if index > 3:
                    if (reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 1][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn] and
                    reversedBoardGrid[index][verticalColumn] == reversedBoardGrid[index - 2][verticalColumn] == reversedBoardGrid[index - 3][verticalColumn] == reversedBoardGrid[index - 4][verticalColumn]):
                        reversedBoardGrid[index][verticalColumn] = ""
                        reversedBoardGrid[index - 1][verticalColumn] = ""
                        reversedBoardGrid[index - 2][verticalColumn] = ""
                        reversedBoardGrid[index - 3][verticalColumn] = ""
                        reversedBoardGrid[index - 4][verticalColumn] = ""
        verticalColumn += 1

def showBoard(board):
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setFontSize(30)
    stddraw.text(3, 19.25, "Taffy Tangle")
    if len(globalScore) > 0:
        stddraw.text(13, 19.25, "Score: {}".format(int(sum(globalScore))))
    else:
        stddraw.text(13, 19.25, "Score: 0")
    pictureGrid = []
    for index in range(len(grid)):
        for innerIndex in range(len(grid[index])):
            if board[index][innerIndex] == "":
                pictureGrid.append("empty")
            else:
                pictureGrid.append(board[index][innerIndex])
    pictureIndex = 0
    for outerIndex in range(1, len(grid) + 1):
        for index in range(1, len(grid[outerIndex - 1]) + 1):
            pictureIndex += 1
            stddraw.picture(picture.Picture(pictureGrid[pictureIndex - 1] + ".png"), index * 2, (outerIndex * 2) - 0)

stddraw.clear(bg)
while True:
    showBoard(boardGrid)
    if stddraw.mousePressed():
        if len(rectCoordinates) >= 1:
            showBoard(boardGrid)
            stddraw.clear(bg)
        drawNavigator(stddraw.mouseX(), stddraw.mouseY())
    stddraw.show(0.0)
