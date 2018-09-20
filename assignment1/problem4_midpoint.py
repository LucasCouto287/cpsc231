# Problem 4 - Midpoint Karel
# Daanish Mazhar & Abdullah Khan

from karel import *

def turn_around():
    turn_left()
    turn_left()

# navigate towards the east until it finds a beeper
def travelEast():
    if not facing_east():
        turn_around()
    move()
    while front_is_clear() and not beepers_present():
        move()

# navigate towards the west until it finds a beeper
def travelWest():
    if not facing_west():
        turn_around()
    move()
    while front_is_clear() and not beepers_present():
        move()

# if standing on a beeper which has another beeper next to it, pick the beeper and move on
# if not, then put the adjacent beeper
# (this effectively moves the east and west beepers closer and closer until the midpoint)
def checkAndPlaceAdjacent():
    if front_is_clear() and beepers_present() and facing_west() or facing_east():
        pick_beeper()
        move()
        if not beepers_present():
            put_beeper()

# check and remove adjacent beepers; this is used when the east and west beepers are close enough
# this effectively removes any adjacent beepers until one is left (on the midpoint)
def checkAndRemoveAdjacent():
    if front_is_clear() and beepers_present():
        move()
        if beepers_present():
            pick_beeper()
        if not left_is_clear() and facing_west():
            turn_around()
            move()

begin_karel_program()

# travel back and forth from east to west and keep checking and removing adjacent beepers
# until they are close to the midpoint
travelEast()
turn_around()
put_beeper()
checkAndPlaceAdjacent()

travelWest()
turn_around()
put_beeper()
checkAndPlaceAdjacent()

travelEast()
turn_around()
checkAndPlaceAdjacent()

travelWest()
turn_around()
checkAndPlaceAdjacent()

travelEast()
turn_around()
checkAndPlaceAdjacent()

travelWest()
turn_around()
checkAndPlaceAdjacent()

travelEast()
turn_around()
checkAndPlaceAdjacent()

# a fail-safe method which performs a final check so that only one beeper is remaining in the world
checkAndRemoveAdjacent()

# extra condition statement in case any beepers are left over
if front_is_clear() and not left_is_clear():
    move()
    pick_beeper()
    move()
    put_beeper()

end_karel_program()