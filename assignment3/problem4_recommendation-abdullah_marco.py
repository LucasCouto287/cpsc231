# Assignment 3 - Problem 4 - Movie Recommendations
# Abdullah Khan - 30074457
# Marco Arias - 30079108

import sys, math
from collections import Counter
import difflib

movies_file = open(sys.argv[1])
cpscpsc231_ratings31_ratings_file = sys.argv[2]
customer_file = open(sys.argv[3])

movie_input = movies_file.readlines()
customer_input = customer_file.readlines()
movies_file.close()
customer_file.close()
# get the customer name (the person who we are going to recommend the movies to)
customerName = customer_input[0]
customerRatings = []
individualRatings = customer_input[1].replace(",", "")

for index in range(len(individualRatings) - 1):
    customerRatings.append(int(individualRatings[index]))

ratingsList = []

# open the class ratings file and look at the even lines (the lines with the ratings)
# append the ratings to a temporary list then append that list to a big 2D list with everyone's ratings
# repeat this step until everyone's ratings have been appended to the big 2D list
with open(cpscpsc231_ratings31_ratings_file, 'r') as file:
    for lineNumber, line in enumerate(file, start = 1):
        # get the index in the ratings file for the customer (so we can isolate their individual ratings)
        if lineNumber % 2 == 1 and customerName in line:
            customerIndex = lineNumber - len(ratingsList)
        else:
            customerIndex = 0
        if lineNumber % 2 == 0:
            individualRatings = []
            ratings = line.replace(",", "").rstrip()
            for index in range(len(ratings)):
                individualRatings.append(int(ratings[index]))
            ratingsList.append(individualRatings)

# make a 2 dimensional list with the converted ratings (convert ratings to the score using the similarity table on the assignment page)
scoreList = []
for index in range(len(ratingsList)):
    scoreList.append([-5 if rating == 1 else -3 if rating == 2 else 1 if rating == 3 else 3 if rating == 4 else rating for rating in ratingsList[index]])

similarityScores = []

customerRatingsCounter = Counter(customerRatings)
def similarity(customerRatings, classmate_ratings):
    seqMatcher = difflib.SequenceMatcher(None, customerRatings, classmate_ratings)
    return seqMatcher.ratio()

for index in range(len(ratingsList)):
    compareCounter = Counter(ratingsList[index])
    similarityScores.append(similarity(customerRatingsCounter, compareCounter))

mostSimilarIndices = sorted(((value, index) for index, value in enumerate(similarityScores)), reverse=True)
mostSimilarRatings = ratingsList[mostSimilarIndices[0][1]]

print("Hello, %s!" % customerName.rstrip())

comparisonHighestRatingIndices = [i for i, rating in enumerate(mostSimilarRatings) if rating == 5]
customerNotSeenIndices = [x for x, rating in enumerate(customerRatings) if rating == 0]

recommendedMoviesIndices = []
print("Based on your ratings of the 100 movies, we believe you might like the following movie(s) as well:")
for index in range(len(customerNotSeenIndices)):
    if customerNotSeenIndices[index] in comparisonHighestRatingIndices:
        recommendedMoviesIndices.append(customerNotSeenIndices[index])

if len(recommendedMoviesIndices) > 0:
    for index in range(len(recommendedMoviesIndices)):
        # show a maximum of 6 recommended movies
        if index < 6:
            print("   -", movie_input[customerNotSeenIndices[index]].rstrip())
else:
    mostSimilarRatings = ratingsList[mostSimilarIndices[1][1]]
    comparisonHighestRatingIndices = [i for i, rating in enumerate(mostSimilarRatings) if rating == 5]
    print("   -", movie_input[customerNotSeenIndices[index]].rstrip())