"""
This Karel the Robot program instructs Karel to draw a checkerboard using beepers, as described in Assignment 1-P3.
    Author: Daanish Mazhar
    Date:   Septemeber 2018
"""
from karel import *

def turnRight(x):
    for i in range(x):
        turn_left()

def forward():
    move()
    findDirection()

def findDirection():
    if(facing_east()):
        if not (front_is_clear()):
            turn_left()
    elif (facing_west()):
        if not(front_is_clear()):
            turnRight(3)
    elif (facing_north()):
        if not (right_is_clear()):
            if(left_is_clear()):
                turn_left()
        elif not(left_is_clear()):
            turnRight(3)

def finalBeeper():
    if (facing_north() and not front_is_clear() and not right_is_clear()):
        put_beeper()

def main():
    if not(front_is_clear()):
            turn_left()

    while (front_is_clear()):
        if not (beepers_present()):
            put_beeper()
            forward()

        if(front_is_clear()):
            forward()
            if (beepers_present()):
                put_beeper()

begin_karel_program()
main()
finalBeeper()
end_karel_program()
