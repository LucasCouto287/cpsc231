# Problem 4 - Midpoint Karel
# Daanish Mazhar & Abdullah Khan

from karel import *

def turn_around():
    turn_left()
    turn_left()

def travelEast():
    while front_is_clear() and facing_east() and not beepers_present():
        move()

def travelWest():
    if facing_east() and not front_is_clear():
        turn_around()
    while front_is_clear() and facing_west():
        move()

def checkAndPlaceAdjacent():
    if beepers_present() and facing_west() or facing_east():
        pick_beeper()
        move()
        put_beeper()

begin_karel_program()

travelEast()
put_beeper()
turn_around()
checkAndPlaceAdjacent()

travelWest()
put_beeper()
turn_around()
checkAndPlaceAdjacent()

move()
travelEast()
turn_around()

# work in progress


end_karel_program()