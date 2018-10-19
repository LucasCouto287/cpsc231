# Assignment 3 - Problem 4 - Movei  Recommendations
# Abdullah Khan - 30074457
# Marco Arias - 30079108

import sys

movies_file = open(sys.argv[1])
cpsc231_ratings_file = sys.argv[2]
customer_file = open(sys.argv[3])

movie_input = movies_file.readlines()
customer_input = customer_file.readlines()
movies_file.close()

ratingsList = []

# open the class ratings file and look at the even lines (the lines with the ratings)
# append the ratings to a temporary list then append that list to a big 2D list with everyone's ratings
# repeat this step until everyone's ratings have been appended to the big 2D list
with open(cpsc231_ratings_file, 'r') as file:
    for lineNumber, line in enumerate(file, start = 1):
        if lineNumber % 2 == 0:
            individualRatings = []
            ratings = line.replace(",", "").rstrip()
            for index in range(len(ratings)):
                individualRatings.append(int(ratings[index]))
            ratingsList.append(individualRatings)

# make a 2 dimensional list with the converted ratings (convert ratings to the score from the similarity tableon assignment page)
scoreList = []
for index in range(len(ratingsList)):
    scoreList.append([-5 if rating == 1 else -3 if rating == 2 else 1 if rating == 3 else 3 if rating == 4 else rating for rating in ratingsList[index]])
