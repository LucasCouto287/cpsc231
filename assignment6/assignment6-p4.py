# Assignment 6 - Problem 4 - Guitar String (client)
# Abdullah Khan - 30074457 - Tutorial 1

import stddraw, stdaudio, time
from guitarP4 import guitarString as gs
from picture import Picture
from collections import deque

# set up canvas and draw a background picture
stddraw.setCanvasSize(600, 600)
guitarPicture = Picture("guitar.png")
stddraw.picture(guitarPicture)

def main():
    stddraw.show(360)

    allKeys = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/ "
    keys = list(allKeys)

    keysPressed = deque()
    frequencies = deque()
    guitarStrings = deque()
    keysToTick = deque()

    # populate the frequencies list using the semitone formula (and first value is 110.0)
    frequencies.append(110.00)
    for index in range(len(keys)):
        frequencies.append((2 ** (1/12)) * frequencies[index])

    # create guitar string objects with different frequencies taken from the frequencies list
    for index in range(len(frequencies)):
        guitarStrings.append(gs(frequencies[index]))

    escape = False
    timer = 0
    while not escape:
        timer += 1
        if timer % 3600 == 0:
            stddraw._checkForEvents()
        while stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key in keys:
                keysPressed.append(key)
                guitarStrings[keys.index(keysPressed[0])].pluck()
                keysToTick.append(key)
                keysPressed.popleft()
            elif key == chr(27):
                escape = True
                print("goodbye")

        string = guitarStrings[0].tick()
        for index in range(1, len(guitarStrings) - 1):
            string += guitarStrings[index].tick()
        stdaudio.playSample(string)

if __name__ == '__main__':
    main()
