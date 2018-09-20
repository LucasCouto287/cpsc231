# Problem 5 - Checkerboard Karel
# Abdullah Khan & Daanish Mazhar

from karel import *

def expandStack():
    move()
    while(beepers_present()):
        pick_beeper()
    turn_left()
    while(front_is_clear() and beepers_in_bag()):
        put_beeper()
        move()
        check()

def check():
    if(facing_north() and not front_is_clear() and beepers_in_bag()):
        put_beeper()

def comeBack():
    for i in range(2):
        turn_left()
    while(front_is_clear()):
        move()
    turn_left()
    move()

def expandSequence():
    while (not beepers_present() and front_is_clear()):
        expandStack()
        comeBack()

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
def forward():
    while(front_is_clear()):
        findDirection()
        move()

begin_karel_program()
expandSequence()
forward()
end_karel_program()
