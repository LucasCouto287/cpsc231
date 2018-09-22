# Problem 4 - Midpoint Karel
# Daanish Mazhar & Abdullah Khan

from karel import *

#function to place beepers while finding modpoint
def placeBeepers():
    while(front_is_clear()):
        move()
        put_beeper()
    turn()
    pick_beeper()
    move()

#function to pickup beepers while finding modpoint (cleanup)
def pickupBeepers():
    if(beepers_present()):
        while(beepers_present()):
            move()
        if not(beepers_present()):
            turn()
            move()
            pick_beeper()
            move()
            pickupBeepers()

#placing the final beeper after finding midpoint thanks to functions above
def finalBeeper():
    turn()
    move()
    put_beeper()

#automate turning twice
def turn():
    turn_left()
    turn_left()

#call functions
def main():
    placeBeepers()
    pickupBeepers()
    finalBeeper()




begin_karel_program()
main()
end_karel_program()
