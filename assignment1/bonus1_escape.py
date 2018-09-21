# Bonus problem - Escape
# Abdullah Khan & Daanish Mazhar

from karel import *

def findWall():
    turn_left()
    while front_is_clear():
        move()

def alignSelf():
    while not front_is_clear():
        turn_left()

def traverseWall():
    while not right_is_clear():
        move()
        if not front_is_clear():
            alignSelf()

def checkForExit():
    if right_is_clear():
        escape()

def escape():
    turn_left()
    turn_left()
    turn_left()
    move()

begin_karel_program()

findWall()
alignSelf()
traverseWall()
checkForExit()


end_karel_program()