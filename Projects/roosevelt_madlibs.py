# Project idea by Kylie Ying on freeCodeCamp: https://www.youtube.com/watch?v=8ext9G7xspg

# Note: I only used her tutorial as a starting point for this assignment. I made it my own.

# Here is a famous quote by Winston Churchill
    # "The only Limit to our realization of tomorrow will be our doubts of today." - Franklin D. Roosevelt

#string concatenation

import random

author = "Franklin D. Roosevelt"
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")
noun4 = input("Noun 4: ")
funnyAuthor = input("Who is this quote attributed to?")

# Randomise the order of the nouns so that they appear in a funny way

# Create a list with the given nouns
nouns = [noun1, noun2, noun3, noun4]

# Shuffle the list of nouns
random.shuffle(nouns)

# Join the list of nouns into an fstring
madlib = f"The only Limit to our {nouns[0]} of {nouns[1]} will be our {nouns[2]} of {nouns[3]}. - {funnyAuthor} "

# Print the string
print(madlib)
