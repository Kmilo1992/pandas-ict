import pandas as pd

# LESSON 5 - DESCRIPTIVE STATISTICS

movies = pd.read_csv("movies.csv")

# RATING
print("RATING")
print("Maximum:", movies["Rating"].max())
print("Minimum:", movies["Rating"].min())
print("Average:", movies["Rating"].mean())
print("Median:", movies["Rating"].median())

# DURATION
print("\nDURATION")
print("Maximum:", movies["Duration"].max())
print("Minimum:", movies["Duration"].min())
print("Average:", movies["Duration"].mean())
print("Median:", movies["Duration"].median())

# VIEWS
print("\nVIEWS")
print("Maximum:", movies["Views"].max())
print("Minimum:", movies["Views"].min())
print("Average:", movies["Views"].mean())
print("Median:", movies["Views"].median())

# DESCRIBE
print("\nRATING DESCRIBE")
print(movies["Rating"].describe())

# Student challenge:
# Repeat the analysis for another numerical column.
