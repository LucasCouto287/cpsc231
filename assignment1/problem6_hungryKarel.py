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

def bottomCorner():
    while(front_is_clear()):
        move()

def second():
    turn_left()
    while(front_is_clear()):
        move()
    for i in range(2):
        turn_left()
    move()
    for i in range(2):
        turn_left()

def top():
    turn_left()
    while(front_is_clear()):
        move()

def findBeeper():
    turn_left()
    while(not beepers_present()):
        move()
    while(beepers_present()):
        collapse()
    while(beepers_in_bag()):
        put_beeper()

def findBeeperFinal():
    turn_left()
    while(not beepers_present()):
        move()
    while(beepers_present()):
        pick_beeper()
          

def collapse():
    turn_left()
    while(beepers_present()):
        pick_beeper()
        move()
        if(not front_is_clear()):
            pick_beeper()
            turn_left()

def findBeeperSecond():
    turn_left()
    while(not beepers_present()):
        move()
    while(beepers_present()):
        collapse()
    turn_left()
    while(front_is_clear()):
        move()
    turn_left()
    while(beepers_in_bag()):
        put_beeper()


def getBack():
    for i in range(2):
        top()

def third():
    turn_left()
    while(front_is_clear()):
        move()
    for i in range(2):
        turn_left()
    for i in range(2):
        move()
    for i in range(2):
        turn_left()

def fourth():
    turn_left()
    while(front_is_clear()):
        move()
    for i in range(2):
        turn_left()
    for i in range(3):
        move()
    for i in range(2):
        turn_left()

begin_karel_program()
expandSequence()
top()
findBeeper()
bottomCorner()
second()
findBeeperSecond()
bottomCorner()
getBack()
bottomCorner()
third()
findBeeper()
bottomCorner()
fourth()
findBeeper()
bottomCorner()
top()
findBeeperFinal()
end_karel_program()
