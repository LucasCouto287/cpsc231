# Problem 2 - Writing with Karel
# Abdullah Khan - September 6th, 2018

from karel import *

begin_karel_program()

move()
turn_left()
for _ in range(8):
    move()
    put_beeper()
for _ in range(3):
    turn_left()
for _ in range(4):
    move()
    put_beeper()
for _ in range(3):
    turn_left()
for _ in range(4):
    move()
    put_beeper()
for _ in range(3):
    turn_left()
for _ in range(3):
    move()
    put_beeper()
for _ in range(2):
    turn_left()
for _ in range(3):
    move()
for _ in range(3):
    turn_left()
for _ in range(3):
    move()
    put_beeper()

turn_left()
move()
move()
put_beeper()
move()
move()
put_beeper()
turn_left()

for _ in range(7):
    move()
    put_beeper()
for _ in range(2):
    turn_left()
for _ in range(3):
    move()

turn_left()
move()
put_beeper()

for i in range(3):
    move()
    turn_left()
    move()
    put_beeper()
    for _ in range(3):
        turn_left()

for _ in range(3):
    turn_left()
for _ in range(4):
    move()
for _ in range(3):
    turn_left()
for _ in range(3):
    move()
put_beeper()

turn_left()
for _ in range(3):
    move()
    turn_left()
    move()
    put_beeper()
    for i in range(3):
        turn_left()

turn_left()
move()
move()

end_karel_program()