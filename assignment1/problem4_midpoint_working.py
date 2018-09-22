# Problem 4 - Midpoint Karel
# Daanish Mazhar & Abdullah Khan

from karel import *

def placeBeepers():
    while(front_is_clear()):
        move()
        put_beeper()
    turn()
    pick_beeper()
    move()

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

def finalBeeper():
    turn()
    move()
    put_beeper()

def turn():
    turn_left()
    turn_left()

def main():
    placeBeepers()
    pickupBeepers()
    finalBeeper()




begin_karel_program()
main()
end_karel_program()
