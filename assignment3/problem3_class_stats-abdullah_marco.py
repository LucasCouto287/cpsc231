# Assignment 3 - Problem 3 - Class Statistics
# Abdullah Khan - 30074457
# Marco Arias - 30079108

import sys
from collections import Counter

movies_file = open(sys.argv[1])
ratings_file = sys.argv[2]

movie_input = movies_file.readlines()
movies_file.close()

ratingsList = []

# open the class ratings file and look at the even lines (the lines with the ratings)
# append the ratings to a temporary list then append that list to a big 2D list with everyone's ratings
# repeat this step until everyone's ratings have been appended to the big 2D list
with open(ratings_file, 'r') as file:
    for lineNumber, line in enumerate(file, start = 1):
        if lineNumber % 2 == 0:
            individualRatings = []
            ratings = line.replace(",", "").rstrip()
            for index in range(len(ratings)):
                individualRatings.append(int(ratings[index]))
            ratingsList.append(individualRatings)

# calculate the average number of movies people in our class have seen
totalMoviesSeen = []
for index in range(len(ratingsList)):
    individualRatingList = ratingsList[index]
    individualMoviesSeen = []
    for ratingIndex in range(len(individualRatingList)):
        if not individualRatingList[ratingIndex] == 0:
            individualMoviesSeen.append(individualRatingList[ratingIndex])
    totalMoviesSeen.append(len(individualMoviesSeen))

print("The average student in CPSC 231 has watched", sum(totalMoviesSeen) // len(totalMoviesSeen),"(rounded) movies out of the 100.")

# get the most popular movies in our class
fav_movies_indices = []
for index in range(len(ratingsList)):
    fav_movies_indices += [index for index, rating in enumerate(ratingsList[index]) if rating > 0]

mostPopular = Counter(fav_movies_indices).most_common(5)

print("\nThe most popular movies were:")
for i in range(len(mostPopular)):
    print("   -", movie_input[mostPopular[i][0]].rstrip())

# get the least popular movies in our class
unknown_movies_indices = []
for index in range(len(ratingsList)):
    unknown_movies_indices += [index for index, rating in enumerate(ratingsList[index]) if rating == 0]

leastPopular = Counter(unknown_movies_indices).most_common(5)

print("\nThe least popular movies were:")
for i in range(len(leastPopular)):
    print("   -", movie_input[leastPopular[i][0]].rstrip())

# make a list with the average of all the non-zero ratings for each movie
averageRatings = []

for outerIndex in range(len(ratingsList[0])):
    if [i[outerIndex] for i in ratingsList].count(0) >= 10:
        singleMovieRatingList = [i[outerIndex] for i in ratingsList]
        while 0 in singleMovieRatingList: singleMovieRatingList.remove(0)
        averageRatings.append(sum(singleMovieRatingList) / len(singleMovieRatingList))

# make a list of all the average values and store them along with their indices in the list (in descending order of rating average)
ratingIndices = sorted(((round(value, 4), index) for index, value in enumerate(averageRatings)), reverse=True)

# get the 5 movies with the highest average ratings
print("\nThe highest rated movies were:")
for i in range(5):
    print("   -", movie_input[ratingIndices[i][1]].rstrip())

# get the 5 movies with the lowest average ratings (reverse of the previous loop)
print("\nThe lowest rated movies were:")
for i in range(5):
    print("   -", movie_input[ratingIndices[len(ratingIndices) - 1 - i][1]].rstrip())

varianceList = []

for outerIndex in range(len(ratingsList[0])):
    if [i[outerIndex] for i in ratingsList].count(0) >= 10:
        singleMovieRatingList = [i[outerIndex] for i in ratingsList]
        while 0 in singleMovieRatingList: singleMovieRatingList.remove(0)
        mean = sum(singleMovieRatingList) / len(singleMovieRatingList)
        variance = sum((x - mean) ** 2 for x in singleMovieRatingList) / len(singleMovieRatingList)
        varianceList.append(variance)

varianceIndices = sorted(((round(value, 4), index) for index, value in enumerate(varianceList)), reverse=True)

# get the 5 movies with the highest variance (using the same method as before)
print("\nThe most contentious movies were:")
for i in range(5):
    print("   -", movie_input[varianceIndices[i][1]].rstrip())
