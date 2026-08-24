import pandas as pd

# LESSON 6 - TEACHER SOLUTION

movies = pd.read_csv("movies.csv")

# PART 1 - EXPLORE
print("Rows and columns:", movies.shape)
print("Column names:", movies.columns)
print("\nDataset information:")
movies.info()

# PART 2 - ANALYZE
print("\nHighest rating:", movies["Rating"].max())
print("Lowest rating:", movies["Rating"].min())
print("Average rating:", movies["Rating"].mean())
print("Median rating:", movies["Rating"].median())

print("\nLongest movie:", movies["Duration"].max(), "minutes")
print("Shortest movie:", movies["Duration"].min(), "minutes")
print("Average duration:", movies["Duration"].mean(), "minutes")
print("Median duration:", movies["Duration"].median(), "minutes")

print("\nHighest views:", movies["Views"].max())
print("Lowest views:", movies["Views"].min())
print("Average views:", movies["Views"].mean())

# Finding the MOVIE associated with a maximum value:
highest_rated_movie = movies.loc[movies["Rating"].idxmax(), "Title"]
most_watched_movie = movies.loc[movies["Views"].idxmax(), "Title"]
longest_movie = movies.loc[movies["Duration"].idxmax(), "Title"]

print("\nHighest-rated movie:", highest_rated_movie)
print("Most-watched movie:", most_watched_movie)
print("Longest movie:", longest_movie)

print("\nFull descriptive summary:")
print(movies.describe())
