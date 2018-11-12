# Assignment 5 - Bonus 1 - Computer Tic-Tac-Toe Player
# Abdullah Khan - 30074457
"""
INCOMPLETE
"""

import stddraw, random
from color import Color

bg = Color(60, 60, 60)
while True:
    try:
        userInput = str(input("choose a difficulty: (h)ard or (n)ormal? "))
        print("Good luck!")
        if userInput == "h" or userInput == "n":
            difficulty = userInput
        else:
            # throw a value error if input is invalid
            raise ValueError
        break
    except:
        print("Please pick one of the two provided difficulties. \"h\" for hard, \"n\" for normal.")

choice = ["X", "O"]
player = random.choice(choice)
computer = "X" if player == "O" else "O"

# set up the canvas
stddraw.setXscale(0.0, 12.0)
stddraw.setYscale(0.0, 12.0)
stddraw.setCanvasSize(600, 600)

grid = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
boxes = []
# coordinates to all the center points of each box
coordinates = [[2.5, 9.5], [6, 9.5], [9.5, 9.5], [2.5, 6], [6, 6], [9.5, 6], [2.5, 2.5], [6, 2.5], [9.5, 2.5]]

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

def emptyIndices(board):
    return [index for index, num in enumerate(board) if num == 0]

def minimax(newBoard, player):
    availableSpots = emptyIndices(newBoard)

    if checkWin(newBoard, player):
        return -10
    elif checkWin(newBoard, computer):
        return 10
    elif len(availableSpots) == 0:
        return 0

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

def checkWin(gridList, player):
    # check all possible winning combinations (for any player)
    return ((board[0] == player && board[1] == player && board[2] == player) or
    (board[3] == player && board[4] == player && board[5] == player) or
    (board[6] == player && board[7] == player && board[8] == player) or
    (board[0] == player && board[3] == player && board[6] == player) or
    (board[1] == player && board[4] == player && board[7] == player) or
    (board[2] == player && board[5] == player && board[8] == player) or
    (board[0] == player && board[4] == player && board[8] == player) or
    (board[2] == player && board[4] == player && board[6] == player))

def newGame():
    # clear the board and clear the filled-in box history
    grid[:9] = [0] * (len(grid))
    boxes.clear()

while True:
    showGrid()
    # if player 1 or 2 won the game
    if (checkWin(grid, 1) + checkWin(grid, 2)) == 1:
        drawMarkers()
        showMessage("{} has won! (click anywhere to play again)".format(...), 6, 0.75, 28)
        if stddraw.mousePressed():
            player = random.choice(choice)
            computer = "X" if player == "O" else "O"
            newGame()
    # if no player won but the board is fully populated, it's a draw
    elif grid.count(0) == 0:
        drawMarkers()
        showMessage("It's a draw! (click anywhere to play again)", 6, 0.6, 28)
        if stddraw.mousePressed():
            player = random.choice(choice)
            computer = "X" if player == "O" else "O"
            newGame()
    # if no one won and the board still has empty boxes, do another turn
    else:
        if computer == "X":
            computerTurn()
        else:
            turn()
        drawMarkers()
        showMessage("Player {}'s turn ({})".format(player, "×" if player == 1 else "o"), 2, 0.5, 24)
    stddraw.show(100)
    stddraw.clear(bg)
