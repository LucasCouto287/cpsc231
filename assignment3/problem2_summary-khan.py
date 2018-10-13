# Assignment 3 - Problem 2 - Your Personal Summary
# Abdullah Khan - 30074457

import sys

movie_file = open(sys.argv[1])
ratings_file = open(sys.argv[2])

movie_input = movie_file.readlines()
ratings_input = ratings_file.readlines()
movie_file.close()
ratings_file.close()

ratings_list = []

# remove the commas and extra whitespace from the ratings input taken from the ratings txt file
ratings = ratings_input[1].replace(", ", "")

for index in range(len(ratings) - 1):
    ratings_list.append(int(ratings[index]))

print("Hello, %s!" % ratings_input[0].rstrip(), "\n")
# count the number of zeroes and subtract that from 100 to get the number of movies I've watched
print("- You've watched", (100 - ratings_list.count(0)), "of the movies in the list.")

# list comprehension used to find all the indices of my most and least favorite movies
fav_movies_indices = [index for index, rating in enumerate(ratings_list) if rating == 5]
worse_movies_indices = [index for index, rating in enumerate(ratings_list) if rating == 1]

print("- Your favourite movies were: ")
for index in range(len(fav_movies_indices)):
    # correlate the favorite movie indices with the movie names given by reading the movies txt file
    fav_movies = (movie_input[fav_movies_indices[index]])
    print("\t", fav_movies.rstrip())

print("- Your least favourite movies were: ")
for index in range(len(worse_movies_indices)):
    # correlate the least favorite movie indices with the movie names given by reading the movies txt file
    least_fav_movies = (movie_input[worse_movies_indices[index]])
    print("\t", least_fav_movies.rstrip())
