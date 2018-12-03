# Assignment 6 - Problem 2 - Ocean Waves
# Abdullah Khan - 30074457 - Tutorial 1

import random, stdaudio, math

def fillWhite(array, sampleNumber):
    for index in range(sampleNumber):
        array.append(random.uniform(-0.25, 0.25))

def fillBrownian(array, firstIndex, lastIndex, variance, scaleFactor):
    if (firstIndex - lastIndex) == 0:
        return
    midpoint = (array[firstIndex] + array[lastIndex]) / 2.0
    # mean is always zero when using gauss(), and we need to find the standard deviation using the sqrt of the variance
    sigma = random.gauss(0.0, variance ** (1/2))
    midIndex = (firstIndex + lastIndex) // 2
    brownianVal = midpoint + sigma
    array[midIndex] = brownianVal
    fillBrownian(array, firstIndex, midIndex, variance / scaleFactor, scaleFactor)
    fillBrownian(array, midIndex + 1, lastIndex, variance / scaleFactor, scaleFactor)

def main():
    sampleRate = 44100
    duration = 20
    frequency = 1/4
    sampleNumber = sampleRate * duration

    hurstExp = 0.5
    scaleFactor = (2.0 ** (2.0 * hurstExp))

    brownianList = [0.0] * sampleNumber
    fillBrownian(brownianList,  0, len(brownianList) - 1, 0.05, scaleFactor)
    whiteList = []
    fillWhite(whiteList, sampleNumber)

    for index in range(sampleNumber):
        timeElapsed = index / sampleRate
        timeRemaining = int(duration - timeElapsed)
        if index % sampleRate == 0:
            print("\rtime left: {}s".format("0" + str(timeRemaining) if len(str(timeRemaining)) == 1 else timeRemaining, int(duration)), end="")
        s = pow(6, (math.sin(2 * math.pi * frequency * timeElapsed)))
        y = (1 - s) * brownianList[index] + (s * whiteList[index])
        stdaudio.playSample(y)
        stdaudio.wait()

if __name__ == '__main__':
    print("\nrelax...")
    main()
    print("\n")
