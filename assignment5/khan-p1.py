import stddraw
from color import Color

bg = Color(60, 60, 60)
player = 1

stddraw.setXscale(0.0, 12.0)
stddraw.setYscale(0.0, 12.0)
stddraw.setCanvasSize(600, 600)

grid = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]
boxes = []


box = 0

def turn():
    global box
    if stddraw.mousePressed():
        mouseX = stddraw.mouseX()
        mouseY = stddraw.mouseY()
        # print(mouseX, mouseY)
        # first row
        if mouseX <= 4 and mouseY >= 8 and not boxes.count(1) == 1:
            boxes.append(1)
        elif mouseX > 4 and mouseX < 8 and mouseY > 8 and not boxes.count(2) == 1:
            boxes.append(2)
        elif mouseX >= 8 and mouseY >= 8 and not boxes.count(3) == 1:
            boxes.append(3)
        # second row
        elif mouseX < 4 and mouseY <= 8 and mouseY >= 4 and not boxes.count(4) == 1:
            boxes.append(4)
        elif mouseX >= 4 and mouseX <= 8 and mouseY < 8 and mouseY > 4 and not boxes.count(5) == 1:
            boxes.append(5)
        elif mouseX > 8 and mouseY < 8 and mouseY > 4 and not boxes.count(6) == 1:
            boxes.append(6)
        # third row
        elif mouseX <= 4 and mouseY <= 4 and not boxes.count(7) == 1:
            boxes.append(7)
        elif mouseX > 4 and mouseX < 8 and mouseY <= 4 and not boxes.count(8) == 1:
            boxes.append(8)
        elif mouseX >= 8 and mouseY <= 4 and not boxes.count(9) == 1:
            boxes.append(9)

def showGrid():
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setPenRadius(0.01)
    # vertical gridlines
    for i in range(1, 3):
        stddraw.line(i * 4, 11, i * 4, 1)
    # horizontal gridlines
    for i in range(1, 3):
        stddraw.line(1, i * 4, 11, i * 4)

def showPlayer(player):
    stddraw.setFontSize(24)
    stddraw.text(1.5, 0.75, "P{}'s turn ({})".format(player, "×" if player == 1 else "○"))

while True:
    turn()
    showGrid()
    showPlayer(player)
    stddraw.show(100)
    stddraw.clear(bg)
