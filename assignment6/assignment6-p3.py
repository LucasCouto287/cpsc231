# Assignment 6 - Problem 3 - Guitar String (client)
# Abdullah Khan - 30074457 - Tutorial 1

import stddraw, stdaudio
from guitarP3 import guitarString as gs
from picture import Picture

# create guitar strings that vibrate at the provided fundamental frequency (pitch)
aString = gs(440.004)
cString = gs(523.25)

# set up canvas and draw a background picture
stddraw.setCanvasSize(600, 600)
guitarPicture = Picture("guitar.png")
stddraw.picture(guitarPicture)
stddraw.show(0.0)

escape = False
while not escape:
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if not key == chr(27):
            if key == "a":
                aString.pluck()
            elif key == "c":
                cString.pluck()
        else:
            escape = True
            print("goodbye")

    string = aString.tick()
    string += cString.tick()
    stdaudio.playSample(string)
