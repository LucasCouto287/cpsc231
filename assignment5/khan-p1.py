# Assignment 5 - Problem 1 - Tic-Tac-Toe
# Abdullah Khan - 30074457

import stddraw
from color import Color

bg = Color(60, 60, 60)
player = 1

# set up the canvas
stddraw.setXscale(0.0, 12.0)
stddraw.setYscale(0.0, 12.0)
stddraw.setCanvasSize(600, 600)

grid = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
boxes = []
coordinates = []

def turn():
    global box, player, coordinates
    # length of the boxes list before doing a turn
    lengthCheck = len(boxes)
    if stddraw.mousePressed():
        mouseX = stddraw.mouseX()
        mouseY = stddraw.mouseY()
        # check which box the user clicked in and populates the boxes list (the order of the elements in this list matter)
        # first row of boxes
        if mouseX <= 4 and mouseY >= 8 and not boxes.count(1) == 1:
            boxes.append(1)
            grid[0] = 1 if player == 1 else 2
        elif mouseX > 4 and mouseX < 8 and mouseY > 8 and not boxes.count(2) == 1:
            boxes.append(2)
            grid[1] = 1 if player == 1 else 2
        elif mouseX >= 8 and mouseY >= 8 and not boxes.count(3) == 1:
            boxes.append(3)
            grid[2] = 1 if player == 1 else 2
        # second row of boxes
        elif mouseX < 4 and mouseY <= 8 and mouseY >= 4 and not boxes.count(4) == 1:
            boxes.append(4)
            grid[3] = 1 if player == 1 else 2
        elif mouseX >= 4 and mouseX <= 8 and mouseY < 8 and mouseY > 4 and not boxes.count(5) == 1:
            boxes.append(5)
            grid[4] = 1 if player == 1 else 2
        elif mouseX > 8 and mouseY < 8 and mouseY > 4 and not boxes.count(6) == 1:
            boxes.append(6)
            grid[5] = 1 if player == 1 else 2
        # third row of boxes
        elif mouseX <= 4 and mouseY <= 4 and not boxes.count(7) == 1:
            boxes.append(7)
            grid[6] = 1 if player == 1 else 2
        elif mouseX > 4 and mouseX < 8 and mouseY <= 4 and not boxes.count(8) == 1:
            boxes.append(8)
            grid[7] = 1 if player == 1 else 2
        elif mouseX >= 8 and mouseY <= 4 and not boxes.count(9) == 1:
            boxes.append(9)
            grid[8] = 1 if player == 1 else 2

        # check the length of the boxes list after doing a turn to see if they are the same or not
        # if they are the same, we don't switch the player since this player clicked on an already filled-in box
        if not len(boxes) == lengthCheck:
            player = 2 if player == 1 else 1
        # coordinates to all the center points of each box
        coordinates += [2.5, 9.5], [6, 9.5], [9.5, 9.5], [2.5, 6], [6, 6], [9.5, 6], [2.5, 2.5], [6, 2.5], [9.5, 2.5]

def showGrid():
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setPenRadius(0.01)
    # vertical gridlines
    for i in range(1, 3):
        stddraw.line(i * 4, 11, i * 4, 1)
    # horizontal gridlines
    for i in range(1, 3):
        stddraw.line(1, i * 4, 11, i * 4)

def showMessage(msg, x, y, fontSize):
    stddraw.setFontSize(fontSize)
    stddraw.text(x, y, msg)

def drawMarkers():
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setFontSize(92)
    if len(coordinates) > 0:
        for index in range(len(grid)):
            stddraw.text(coordinates[index][0], coordinates[index][1], "×" if grid[index] == 1 else "o" if grid[index] == 2 else "")

def checkWin(gridList, playerNum):
    # check all possible winning combinations (for any player)
    if gridList[0] == playerNum and gridList[1] == playerNum and gridList[2] == playerNum: return 1
    if gridList[3] == playerNum and gridList[4] == playerNum and gridList[5] == playerNum: return 1
    if gridList[6] == playerNum and gridList[7] == playerNum and gridList[8] == playerNum: return 1

    if gridList[0] == playerNum and gridList[3] == playerNum and gridList[6] == playerNum: return 1
    if gridList[1] == playerNum and gridList[4] == playerNum and gridList[7] == playerNum: return 1
    if gridList[2] == playerNum and gridList[5] == playerNum and gridList[8] == playerNum: return 1

    if gridList[0] == playerNum and gridList[4] == playerNum and gridList[8] == playerNum: return 1
    if gridList[2] == playerNum and gridList[4] == playerNum and gridList[6] == playerNum: return 1

    return 0

def newGame():
    # clear the board and clear the filled-in box history
    grid[:9] = [0] * (len(grid))
    boxes.clear()

while True:
    showGrid()
    # if player 1 or 2 won the game
    if (checkWin(grid, 1) + checkWin(grid, 2)) == 1:
        drawMarkers()
        showMessage("Player {} has won! (click anywhere to play again)".format(1 if player == 2 else 2), 6, 0.75, 28)
        if stddraw.mousePressed():
            player = 1
            newGame()
    # if no player won but the board is fully populated, it's a draw
    elif grid.count(0) == 0:
        drawMarkers()
        showMessage("It's a draw! (click anywhere to play again)", 6, 0.6, 28)
        if stddraw.mousePressed():
            player = 1
            newGame()
    # if no one won and the board still has empty boxes, do another turn
    else:
        turn()
        drawMarkers()
        showMessage("Player {}'s turn ({})".format(player, "×" if player == 1 else "o"), 2, 0.5, 24)
    stddraw.show(100)
    stddraw.clear(bg)
