# Assignment 6 - Problem 1 - Brownian Bridge
# Abdullah Khan - 30074457 - Tutorial 1

import sys, stddraw
from random import gauss
from stdstats import plotLines
from color import Color

bg = Color(35, 35, 35)

def fillBrownian(array, firstIndex, lastIndex, variance, scaleFactor):
    # base case to stop recursion if there is not midpoint (first and last are together)
    if (firstIndex - lastIndex) == 0:
        return

    # get the value of the mean in the partitioned list
    average = (array[firstIndex] + array[lastIndex]) / 2.0
    # mean is always zero when using gauss(), and we need to find the standard deviation using the sqrt of the variance
    sigma = gauss(0.0, variance ** (1/2))
    # get the index of the midpoint in the partitioned list
    midIndex = (firstIndex + lastIndex) // 2
    brownianVal = average + sigma
    array[midIndex] = brownianVal
    # recur on the sub intervals of the list
    fillBrownian(array, firstIndex, midIndex, variance / scaleFactor, scaleFactor)
    fillBrownian(array, midIndex + 1, lastIndex, variance / scaleFactor, scaleFactor)

def main():
    # initialize list with 129 values (all are 0.0)
    brownianList = [0.0] * 129
    hurstExp = float(sys.argv[1])
    scaleFactor = (2.0 ** (2.0 * hurstExp))
    fillBrownian(brownianList, 0, len(brownianList) - 1, 0.05, scaleFactor)

    stddraw.setYscale(-1, 1)
    stddraw.setCanvasSize(700, 700)
    stddraw.clear(bg)
    stddraw.setPenColor(Color(200, 200, 200))

    plotLines(brownianList)
    stddraw.show()

if __name__ == '__main__':
    main()
