import stddraw
from color import Color

bg = Color(60, 60, 60)
player = 1

stddraw.setXscale(0.0, 12.0)
stddraw.setYscale(0.0, 12.0)
stddraw.setCanvasSize(600, 600)

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

boxes = []
coordinates = []

def turn():
    global box, player, coordinates
    if stddraw.mousePressed():
        mouseX = stddraw.mouseX()
        mouseY = stddraw.mouseY()
        # first row
        if mouseX <= 4 and mouseY >= 8 and not boxes.count(1) == 1:
            boxes.append(1)
            grid[0][0] = 1 if player == 1 else 2
        elif mouseX > 4 and mouseX < 8 and mouseY > 8 and not boxes.count(2) == 1:
            boxes.append(2)
            grid[0][1] = 1 if player == 1 else 2
        elif mouseX >= 8 and mouseY >= 8 and not boxes.count(3) == 1:
            boxes.append(3)
            grid[0][2] = 1 if player == 1 else 2
        # second row
        elif mouseX < 4 and mouseY <= 8 and mouseY >= 4 and not boxes.count(4) == 1:
            boxes.append(4)
            grid[1][0] = 1 if player == 1 else 2
        elif mouseX >= 4 and mouseX <= 8 and mouseY < 8 and mouseY > 4 and not boxes.count(5) == 1:
            boxes.append(5)
            grid[1][1] = 1 if player == 1 else 2
        elif mouseX > 8 and mouseY < 8 and mouseY > 4 and not boxes.count(6) == 1:
            boxes.append(6)
            grid[1][2] = 1 if player == 1 else 2
        # third row
        elif mouseX <= 4 and mouseY <= 4 and not boxes.count(7) == 1:
            boxes.append(7)
            grid[2][0] = 1 if player == 1 else 2
        elif mouseX > 4 and mouseX < 8 and mouseY <= 4 and not boxes.count(8) == 1:
            boxes.append(8)
            grid[2][1] = 1 if player == 1 else 2
        elif mouseX >= 8 and mouseY <= 4 and not boxes.count(9) == 1:
            boxes.append(9)
            grid[2][2] = 1 if player == 1 else 2
        # print(grid)
        player = 2 if player == 1 else 1
        coordinates += [2.5, 9.5], [6, 9.5], [9.5, 9.5], [2.5, 6], [6, 6], [9.5, 6], [2.5, 2.5], [6, 2.5], [9.5, 2.5]
        print(coordinates)

# def placeMarkers():
#     stddraw.setPenColor(Color(190, 190, 190))
#     stddraw.setFontSize(92)
#     marker = "X" if player == 1 else "O"
    # for i in range():


def showGrid():
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setPenRadius(0.01)
    # vertical gridlines
    for i in range(1, 3):
        stddraw.line(i * 4, 11, i * 4, 1)
    # horizontal gridlines
    for i in range(1, 3):
        stddraw.line(1, i * 4, 11, i * 4)

def showPlayerMessage(player):
    stddraw.setFontSize(24)
    stddraw.text(1.5, 0.75, "P{}'s turn ({})".format(player, "×" if player == 1 else "○"))

def drawMarkers():
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setFontSize(92)
    if len(coordinates) > 0:
        for index in range(len(grid)):
            for innerIndex in range(len(grid[index])):
                # for coordinateIndex in range(len(coordinates)):
                stddraw.text(coordinates[][0], coordinates[][1], "×" if grid[index][innerIndex] == 1 else "○" if grid[index][innerIndex] == 2 else "")

while True:
    turn()
    drawMarkers()
    showGrid()
    showPlayerMessage(player)
    stddraw.show(100)
    stddraw.clear(bg)
