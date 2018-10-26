# Assignment 4 - Problem 2 - Analog Clock
# Abdullah Khan - 30074457

from color import Color
import stddraw, time, math

clockDiameter = 5
secondsHandRadius = clockDiameter * 0.65
minutesHandRadius = clockDiameter * 0.55
hoursHandRadius = clockDiameter * 0.4
centerX = 5
centerY = 5

def clock():
    stddraw.setXscale(0.0, 10.0)
    stddraw.setYscale(0.0, 10.0)
    darkGrey = Color(30, 30, 30)
    lightGray = Color(150, 150, 150)
    grey = Color(60, 60, 60)
    lightRed = Color(225, 70, 90)

    stddraw.setPenRadius(0.02)
    stddraw.setPenColor(grey)
    stddraw.filledCircle(4.9, 4.8, 4)
    stddraw.setPenColor(lightGray)
    stddraw.filledCircle(clockDiameter, clockDiameter, 4)

    stddraw.setFontSize(34)
    stddraw.setPenRadius(0.01)
    stddraw.setFontFamily("monospace")
    for i in range(12):
        x = (centerX * 0.7) * math.cos(math.radians(i * 30)) + centerX
        y = (centerY * 0.7) * math.sin(math.radians(i * 30)) + centerY
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(y, x, "12" if i == 0 else str(i)) if i % 3 == 0 else stddraw.point(x, y)

    aggregateTime = time.localtime()
    hour = aggregateTime.tm_hour if aggregateTime.tm_hour <= 12 else aggregateTime.tm_hour - 12
    minute = aggregateTime.tm_min
    second = aggregateTime.tm_sec

    stddraw.setPenRadius(0.05)
    stddraw.setPenColor(grey)

    for i in range(12):
        x = 3.5 * math.cos(math.radians(i)) + 5
        y = 3.5 * math.sin(math.radians(i)) + 5

    s = ((second) / 60 * (-math.pi * 2)) + (math.pi / 2)
    m = ((-minute - ((second / 60))) / 60 * (math.pi * 2) + (math.pi / 2))
    h = ((((hour + (minute / 60)) / 12) * -math.pi * 2) + (math.pi / 2))

    stddraw.setPenRadius(0.06)
    stddraw.setPenColor(grey)
    stddraw.line(centerX, centerY, centerX + math.cos(m) * minutesHandRadius, centerY + math.sin(m) * minutesHandRadius)
    stddraw.setPenRadius(0.09)
    stddraw.setPenColor(darkGrey)
    stddraw.line(centerX, centerY, centerX + math.cos(h) * hoursHandRadius, centerY + math.sin(h) * hoursHandRadius)
    stddraw.setPenRadius(0.02)
    stddraw.setPenColor(lightRed)
    stddraw.line(centerX, centerY, centerX + math.cos(s) * secondsHandRadius, centerY + math.sin(s) * secondsHandRadius)
    stddraw.filledCircle(5, 5, 0.15)
    stddraw.setPenColor(grey)
    stddraw.text(8.25, 0.5, "{}:{}:{}".format(hour, "0" + str(minute) if len(str(minute)) == 1 else minute, "0" + str(second) if len(str(second)) == 1 else second))

while True:
    clock()
    stddraw.show(100)
    stddraw.clear()
