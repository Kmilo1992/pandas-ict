import pandas as pd

# LESSON 4 - EXPLORE A DATAFRAME

movies = pd.read_csv("movies.csv")

print("COLUMN NAMES")
print(movies.columns)

print("\nSHAPE (ROWS, COLUMNS)")
print(movies.shape)

print("\nDATASET INFORMATION")
print(movies.info())

print("\nFIRST 5 ROWS")
print(movies.head())

# Exploration questions:
# 1. How many rows are there?
# 2. How many columns are there?
# 3. What are the column names?
# 4. Which columns contain numerical information?
# 5. Which columns contain text?
# 6. What can you discover using info()?
#
# IMPORTANT:
# describe() is shown here only as a preview.
# We will analyze it in Lesson 5.
print("\nSTATISTICAL PREVIEW")
print(movies.describe())
