# Problem 5 - Checkerboard Karel
# Abdullah Khan & Daanish Mazhar

from karel import *

#main sequence to be called in start karel
def main():
	put_beeper()
	check_wall()
	while(front_is_clear()):
  		beepers_east()
  		beepers_west()

#turn right three times (automate)
def turn_right():
	for i in range(3):
		turn_left()

#check beepers while east
def beepers_east():
	while(facing_east()):
		move()
		if(front_is_clear()):
			move()
			put_beeper()
		up_east()

#check beepers east while travelling up
def up_east():
	if(not front_is_clear()):
		if(not beepers_present()):
			turn_left()
			if(front_is_clear()):
				move()
				turn_left()
				put_beeper()
		else:
			turn_left()
			if(front_is_clear()):
				move()
				turn_left()
				move()
				put_beeper()

#check beepers while facing west
def beepers_west():
	while(facing_west()):
		move()
		if(front_is_clear()):
			move()
			put_beeper()
		up_west()

#check beepers west while travelling up
def up_west():
	if(not front_is_clear()):
		if(not beepers_present()):
			turn_right()
			if(front_is_clear()):
				move()
				turn_right()
				put_beeper()
		else:
			turn_right()
			if(front_is_clear()):
				move()
				turn_right()
				move()
				put_beeper()

#check for wall while on the edge of a line
def check_wall():
	if(not front_is_clear()):
		turn_left()
		while(front_is_clear()):
			move()
			if(front_is_clear()):
				move()
				put_beeper()

#call main sequence
begin_karel_program()
main()
end_karel_program()
