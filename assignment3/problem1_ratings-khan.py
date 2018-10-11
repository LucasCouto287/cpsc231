# Assignment 3 - Problem 1 - Your Movie Ratings
# Abdullah Khan - 30074457

import sys

file = open(sys.argv[1])
# read each line in the file and store as an array of str objects
movies = file.readlines()
file.close()

name = input("What is your name? ").capitalize()
print("\nHello, %s." % name)
print("Rate the folowing movies based on this scale:")
print("""0: Never seen it.
1: It was terrible!
2: Didn't like it...
3: It was OK.
4: I liked it!
5: It was awesome!
""")

print("Movies:")
ratings = []
for index in range(len(movies)):
    movie = movies[index]
    # only accept integer inputs (<=5 and >= 0) for the ratings
    while True:
        try:
            rating = int(input(movie))
            if rating >= 0 and rating <= 5:
                ratings.append(rating)
            else:
                # throw a value error if input is incorrect
                raise ValueError
            break
        except:
            print("Please pick a rating from 1 to 5.")

print("Thank you, %s." % name)

output = open("ratings-khan.txt", "w")

output.write(name)
output.write("\n")
output.write((", ").join(map(str, ratings)))
output.write("\n")
