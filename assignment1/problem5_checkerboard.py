# Problem 5 - Checkerboard Karel
# Abdullah Khan & Daanish Mazhar

from karel import *

def main():
	put_beeper()
	check_wall()
	while(front_is_clear()):
  		beepers_east()
  		beepers_west()

def turn_right():
	for i in range(3):
		turn_left()

def beepers_east():
	while(facing_east()):
		move()
		if(front_is_clear()):
			move()
			put_beeper()
		up_east()

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

def beepers_west():
	while(facing_west()):
		move()
		if(front_is_clear()):
			move()
			put_beeper()
		up_west()

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

def check_wall():
	if(not front_is_clear()):
		turn_left()
		while(front_is_clear()):
			move()
			if(front_is_clear()):
				move()
				put_beeper()

begin_karel_program()
main()
end_karel_program()
