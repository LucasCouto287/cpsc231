# Problem 3 - Karel the Gardener
# Daanish Mazhar & Abdullah Khan

from karel import *

def changeQuadrant():
    turn_left()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def startingPoint():
    turn_left()
    move()
    for _ in range(3):
        turn_left()
    while(front_is_clear()):
        move()
    put_beeper()

def horizontalBeepers():
    if(left_is_clear()):
        move()
    while not left_is_clear():
        if not(beepers_present()):
            put_beeper()
        if(front_is_clear()):
            move()
        else:
            turn_right()
    # turn_right()

def verticalBeepers():
    while front_is_clear():
        move()
        put_beeper()
    turn_right()

begin_karel_program()

startingPoint()
turn_around()
changeQuadrant()
move()
turn_left()
verticalBeepers()
horizontalBeepers()
changeQuadrant()
# move()
horizontalBeepers()
changeQuadrant()
# turn_around()
# verticalBeepers()
#
# while not(left_is_clear()):
#     move()
#     put_beeper()
#
# changeQuadrant()
# horizontalBeepers()
end_karel_program()