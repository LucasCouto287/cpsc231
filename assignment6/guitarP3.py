# Assignment 6 - Problem 3 Module file
# Abdullah Khan - 30074457 - Tutorial 1

import collections, random

class guitarString:
    def __init__(self, frequency):
        self.frequency = frequency
        self.p = int(44100 / frequency)
        self.waveTable = collections.deque()
        self.decayFactor = 0.996

    def pluck(self):
        # clear wavetable then fill it back up with white noise
        self.waveTable.clear()
        for index in range(self.p):
            self.waveTable.append(random.uniform(-0.5, 0.5))

    def tick(self):
        if len(self.waveTable) == 0: return 0
        yN = self.decayFactor * (0.5 * (self.waveTable[0] + self.waveTable[1]))
        self.waveTable.append(yN)
        self.waveTable.popleft()
        return yN
