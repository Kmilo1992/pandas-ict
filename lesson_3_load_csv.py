import pandas as pd

# LESSON 3 - LOAD A CSV FILE
# The movies.csv file must be in the same folder as this Python file.

movies = pd.read_csv("movies.csv")

print("FULL DATASET")
print(movies)

print("\nFIRST 5 MOVIES")
print(movies.head())

print("\nLAST 5 MOVIES")
print(movies.tail())

print("\nMOVIE TITLES")
print(movies["Title"])

print("\nRATINGS")
print(movies["Rating"])

# Student challenges:
# 1. Print only Genre.
# 2. Print only Year.
# 3. Print only Views.
# 4. Try another column.
