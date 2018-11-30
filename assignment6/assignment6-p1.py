# Assignment 6 - Problem 1 - Brownian Bridge
# Abdullah Khan - 30074457 - Tutorial 1

import random, sys, stddraw
from stdstats import plotLines
from color import Color

bg = Color(35, 35, 35)

hurstExp = float(sys.argv[1])
scale = (2 ** (2 * hurstExp))

def fillBrownian(array, firstIndex, lastIndex, variance, scale):
    if (lastIndex - firstIndex) <= 0.01:
        print("done")
        return
    midIndex = (firstIndex + lastIndex) // 2
    midpoint = float((array[firstIndex] + array[lastIndex]) / 2)
    # mean is always zero when using gauss(), and we need to find the standard deviation using the sqrt of the variance
    # variance = variance / scale
    brownianVal = midpoint + random.gauss(0.0, variance ** (1/2))
    array[midIndex] = brownianVal
    fillBrownian(array, 0, midIndex, variance / scale, hurstExp)
    fillBrownian(array, midIndex + 1, lastIndex, variance / scale, hurstExp)
    # if midpoint in array[:midIndex]:
    # elif midpoint in array[midIndex + 1:]:

brownianList = [0.0] * 129
fillBrownian(brownianList, 0, len(brownianList) - 1, 0.05, hurstExp)

stddraw.setYscale(-1, 1)
stddraw.setCanvasSize(600, 400)
stddraw.clear(bg)
stddraw.setPenColor(Color(200, 200, 200))

plotLines(brownianList)

print(brownianList)
stddraw.show()
# import sys
# import math
# import stddraw
# import stdrandom
#
# #-----------------------------------------------------------------------
#
# # Draw a Brownian bridge from (x0, y0) to (x1, y1) with the given
# # variance and scaleFactor.
#
# def curve(x0, y0, x1, y1, variance, scaleFactor):
#     if (x1 - x0) < .01:
#         stddraw.line(x0, y0, x1, y1)
#         return
#     xm = (x0 + x1) / 2.0
#     ym = (y0 + y1) / 2.0
#     delta = stdrandom.gaussian(0, math.sqrt(variance))
#     curve(x0, y0, xm, ym+delta, variance/scaleFactor, scaleFactor)
#     curve(xm, ym+delta, x1, y1, variance/scaleFactor, scaleFactor)
#
# #-----------------------------------------------------------------------
#
# # Accept a Hurst exponent as a command-line argument.
# # Use the Hurst exponent to compute a scale factor.
# # Draw a Brownian bridge from (0, .5) to (1.0, .5) with
# # variance .01 and that scale factor.
#
# def main():
#     hurstExponent = float(sys.argv[1])
#     stddraw.setPenRadius(0.0)
#     stddraw.clear(stddraw.LIGHT_GRAY)
#     scaleFactor = 2 ** (2.0 * hurstExponent)
#     curve(0, .5, 1.0, .5, .01, scaleFactor)
#     stddraw.show()
#
# if __name__ == '__main__':
#     main()
