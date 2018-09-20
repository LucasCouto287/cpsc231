# Problem 5 - Checkerboard Karel
# Abdullah Khan & Daanish Mazhar

from karel import *

def forward():
    move()
    findDirection()

def findDirection():
    if(facing_east()):
        if not (front_is_clear()):
            turn_left()
    elif (facing_west()):
        if not(front_is_clear()):
            for i in range(3):
                turn_left()
    elif (facing_north()):
        if not (right_is_clear()):
            if(left_is_clear()):
                turn_left()
        elif not(left_is_clear()):
            for i in range(3):
                turn_left()

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
end_karel_program()
