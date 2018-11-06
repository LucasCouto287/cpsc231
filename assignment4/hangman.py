# Assignment 4 - Module which handles the visual aspect of the problem 4 hangman game
# Abdullah Khan - 30074457
# Raiyan Sarwar - 30075746

from color import Color
import stddraw

bg = Color(60, 60, 60)

stddraw.setXscale(0.0, 20.0)
stddraw.setYscale(0.0, 20.0)
stddraw.setCanvasSize(900, 900)

def displayMessage(x, y, msg, fontSize):
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.setFontSize(fontSize)
    stddraw.text(x, y, msg)

def drawHangman(wrongGuesses):
    stddraw.setPenColor(Color(190, 190, 190))
    # head
    if len(wrongGuesses) >= 1:
        stddraw.filledCircle(15, 10, 1.25)
    # torso
    if len(wrongGuesses) >= 2:
        stddraw.filledRectangle(15, 5, 0.1, 4)
        stddraw.setPenRadius(0.07)
    # left hand
    if len(wrongGuesses) >= 3:
        stddraw.line(15, 8.5, 17, 7.5)
    # right hand
    if len(wrongGuesses) >= 4:
        stddraw.line(15, 8.5, 13, 7.5)
    # left leg
    if len(wrongGuesses) >= 5:
        stddraw.line(16.5, 3, 15, 5)
    # right leg
    if len(wrongGuesses) >= 6:
        stddraw.line(15, 5, 13.5, 3)
    # gallows
    if len(wrongGuesses) >= 7:
        stddraw.setPenRadius(0.05)
        stddraw.line(15, 10, 16, 12)
        stddraw.line(16, 12, 19, 12)
        stddraw.line(19, 12, 19, 1)
        stddraw.filledRectangle(11, 1, 9, 1)
    # face
    if len(wrongGuesses) >= 8:
        stddraw.setPenColor(Color(20, 20, 20))
        stddraw.line(14.8, 10.5, 14.3, 10)
        stddraw.line(14.3, 10.5, 14.8, 10)
        stddraw.line(15.8, 10.5, 15.3, 10)
        stddraw.line(15.3, 10.5, 15.8, 10)
        stddraw.line(14.2, 9.7, 15.7, 9.6)

def displayWrongGuesses():
    stddraw.setFontSize()
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.text(4, 9, "Your wrong guesses so far:")

def displaySecretWord(word):
    stddraw.setPenColor(Color(200, 200, 200))
    stddraw.setFontSize(72)
    stddraw.text(10, 17, ("{}".format(" ".join([str(letter) for letter in word]))))

def showCanvas():
    stddraw.setFontSize(22)
    stddraw.setPenColor(Color(190, 190, 190))
    stddraw.show(0.0)
    stddraw.clear(bg)
