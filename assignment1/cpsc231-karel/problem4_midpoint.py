# Problem 4 - Midpoint Karel
# Daanish Mazhar & Abdullah Khan

from karel import *

def turn_around():
    turn_left()
    turn_left()

def travelEast():
    if facing_west() and not front_is_clear():
        turn_around()
    while front_is_clear() and facing_east() and not beepers_present():
        move()

def travelWest():
    if facing_east() and not front_is_clear():
        turn_around()
    while front_is_clear() and facing_west():
        move()
        if beepers_present():
            break

def checkAndPlaceAdjacent():
    if front_is_clear() and beepers_present() and facing_west() or facing_east():
        pick_beeper()
        move()
        if not beepers_present():
            put_beeper()

def checkAndRemoveAdjacent():
    if front_is_clear() and beepers_present() and facing_west() or facing_east():
        move()
        if beepers_present():
            pick_beeper()
    if not left_is_clear():
        turn_around()
        move()
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
checkAndPlaceAdjacent()

travelWest()
turn_around()
# checkAndPlaceAdjacent()

if facing_east() and beepers_present() and not right_is_clear():
    move()
    # while not beepers_present():
    travelEast()
    turn_around()
    checkAndPlaceAdjacent()

if facing_west() and not left_is_clear():
    travelWest()
    turn_around()
    checkAndPlaceAdjacent()

if facing_east() and beepers_present() and front_is_clear() and not right_is_clear():
    move()
    travelEast()
    turn_around()
    checkAndPlaceAdjacent()
    checkAndRemoveAdjacent()

end_karel_program()