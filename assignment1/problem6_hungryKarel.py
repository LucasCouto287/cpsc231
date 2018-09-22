# Problem 6 - Hungry Karel
# Abdullah Khan & Daanish Mazhar

from karel import *

#open each stack upwards to be counted (checked)
def expandStack():
    move()
    while(beepers_present()):
        pick_beeper()
    turn_left()
    while(front_is_clear() and beepers_in_bag()):
        put_beeper()
        move()
        check()

#check position of karel
def check():
    if(facing_north() and not front_is_clear() and beepers_in_bag()):
        put_beeper()

#come back after expanding
def comeBack():
    for i in range(2):
        turn_left()
    while(front_is_clear()):
        move()
    turn_left()
    move()

#expand all stacks
def expandSequence():
    while (not beepers_present() and front_is_clear()):
        expandStack()
        comeBack()

#find bottom corner
def bottomCorner():
    while(front_is_clear()):
        move()

#second stack
def second():
    turn_left()
    while(front_is_clear()):
        move()
    for i in range(2):
        turn_left()
    move()
    for i in range(2):
        turn_left()

#top of map
def top():
    turn_left()
    while(front_is_clear()):
        move()

#find the beeper in current line
def findBeeper():
    turn_left()
    while(not beepers_present()):
        move()
    while(beepers_present()):
        collapse()
    while(beepers_in_bag()):
        put_beeper()

#find the final beeper in line
def findBeeperFinal():
    turn_left()
    while(not beepers_present()):
        move()
    while(beepers_present()):
        pick_beeper()

#close down expaned stack
def collapse():
    turn_left()
    while(beepers_present()):
        pick_beeper()
        move()
        if(not front_is_clear()):
            pick_beeper()
            turn_left()

#second beeper lookup
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

#get bacl to move to top twice
def getBack():
    for i in range(2):
        top()

#find third line
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

#find the fourth or onwards line
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

#call all main functions
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
