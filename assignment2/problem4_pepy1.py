# Assignment 2 - Problem 4 - Pepy's Problem
# Abdullah Khan - 30074457
# this is the correct version of my problem 4 (please ignore the previously submitted one)

import random

probabilityListSix = []
rolls = 6
for index in range(rolls):
    probabilityListSix.append((1 - (5/rolls) ** rolls))

probabilitySix = sum(probabilityListSix) / float(len(probabilityListSix))
print("probability of 1 once in 6 rolls is", probabilitySix)

probabilityListTwelve = []
rolls = 12

for index in range(rolls):
    probabilityListTwelve.append(((6 ** rolls) - (5 ** rolls) - (5 ** 11) * rolls) / (6 ** rolls))

probabilityTwelve = sum(probabilityListTwelve) / float(len(probabilityListTwelve))
print("probability of 1 twice in 12 rolls is:", probabilityTwelve)

print("Therefore, rolling a 1 once in 6 rolls is",
        "less likely than" if probabilitySix < probabilityTwelve else "more likely than",
        "rolling a 1 twice in 12 rolls")
