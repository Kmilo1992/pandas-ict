import pandas as pd

# LESSON 2 - FIRST PANDAS DATAFRAME
# Goal: understand that a DataFrame is a table of data.

data = {
    "Title": ["Avatar", "Titanic", "Inception", "Frozen", "Interstellar"],
    "Genre": ["Sci-Fi", "Drama", "Sci-Fi", "Animation", "Sci-Fi"],
    "Rating": [7.8, 7.9, 8.8, 7.4, 8.7]
}

movies = pd.DataFrame(data)

print(movies)

# Try these challenges:
# 1. Add another movie.
# 2. Change one rating.
# 3. Add a new column called "Year".
# 4. Print only the Rating column.
