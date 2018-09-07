# Problem 1 - Picking up the Paper
# Abdullah Khan - September 6th, 2018
from karel import *

begin_karel_program()

turn_left()
move()
move()
turn_left()
move()
move()
# out of the house
turn_left()
move()
move()
turn_left()
move()
pick_beeper()
# picked up the paper, now returning home
turn_left()
move()
turn_left()
move()
# using loops to reduce repetition...
for _ in range(3):
    turn_left()
move()
for _ in range(3):
    turn_left()
move()
# re-entered the house
move()
for _ in range(3):
    turn_left()
move()
move()
turn_left()
# Karel's back in bed with the morning paper
end_karel_program()