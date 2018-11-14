# Assignment 5 - Problem 2 - Taffy Tangle
# Abdullah Khan - 30074457
# Afnan

import random, stddraw
from color import Color

bg = Color(255, 255, 255)

red = Color(255, 55, 75)
green = Color(55, 255, 75)
yellow = Color(245, 245, 55)
blue = Color(50, 175, 255)
purple = Color(145, 55, 255)
orange = Color(255, 155, 70)

colors = [red, green, yellow, blue, purple, orange]

# set up the canvas
stddraw.setXscale(0.0, 16.0)
stddraw.setYscale(0.0, 20.0)
stddraw.setCanvasSize(750, 900)

def generateBoard():
    for outerIndex in range(1, 10):
        for index in range(1, 8):
            stddraw.setPenColor(random.choice(colors))
            randomShape(index * 2, outerIndex * 2)

def randomShape(x, y):
    shapes = ["circle", "triangle", "rectangle"]
    # shapes = ["circle", "triangle", "rectangle", "pentagon", "diamond", "polygon"]
    randomShape = random.choice(shapes)

    if randomShape == "circle":
        return stddraw.filledCircle(x, y, 0.6)
    elif randomShape == "triangle":
        return stddraw.filledPolygon([x, x + 0.02, x - 0.02], [y - 0.02, y + 0.02, y + 0.02])
    elif randomShape == "rectangle":
        return stddraw.filledRectangle(x - 0.02, y - 0.02, )

# while True:
generateBoard()
stddraw.show()
    # stddraw.clear(bg)
