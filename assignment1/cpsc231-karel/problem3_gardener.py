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

def verticalBeepers():
    while front_is_clear():
        move()
        put_beeper()
    turn_right()

begin_karel_program()

# navigate to the initial point (quadrant 3)
startingPoint()
turn_around()
# place the first beeper
put_beeper()
# move to the next quadrant (quadrant 4)
changeQuadrant()
move()
turn_left()
# place vertical and horizontal beepers in quadrant 3
verticalBeepers()
horizontalBeepers()

# navigate to the next quadrant (quadrant 1)
changeQuadrant()
# place beepers in quadrant 1
horizontalBeepers()

# navigate to quadrant 2 and place its beepers
changeQuadrant()
verticalBeepers()
horizontalBeepers()

# navigate to quadrant 3 and place the final beepers
changeQuadrant()
horizontalBeepers()

end_karel_program()