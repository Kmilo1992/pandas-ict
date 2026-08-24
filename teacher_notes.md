# Teacher Notes - Pandas from Zero

## 1. The mental model

Think of Pandas as a set of tools that lets Python work with tables.

- Python = programming language
- Pandas = library for data manipulation and analysis
- DataFrame = table
- Column = one variable/category of information
- Row = one record/observation
- CSV = simple file format for storing tabular data

## 2. What does `import pandas as pd` mean?

`import pandas` loads the Pandas library.

`as pd` gives the library a short nickname.

Therefore:
`pd.DataFrame(...)`
means:
"Use the DataFrame tool from Pandas."

## 3. What is a DataFrame?

A DataFrame is a table.

Example:
    Title | Genre | Rating
    Movie A | Action | 8.5
    Movie B | Drama | 7.2

## 4. What does `pd.read_csv()` do?

It reads a CSV file and converts it into a DataFrame.

    movies = pd.read_csv("movies.csv")

Read this as:
"Read movies.csv and store the resulting table in a variable called movies."

## 5. What does `movies["Rating"]` mean?

It selects the Rating column from the DataFrame.

## 6. What does `head()` do?

It displays the first 5 rows by default.

    movies.head()

## 7. What does `tail()` do?

It displays the last 5 rows by default.

    movies.tail()

## 8. What does `columns` do?

It tells us the names of the columns.

    movies.columns

## 9. What does `shape` do?

It returns:
    (number_of_rows, number_of_columns)

Example:
    (30, 6)

means:
30 rows and 6 columns.

## 10. What does `info()` do?

It gives structural information:
- column names
- number of non-empty values
- data types
- memory information

For this unit, students mainly need to understand the first three.

## 11. Descriptive statistics

For a numerical column:

    movies["Rating"].max()     -> highest value
    movies["Rating"].min()     -> lowest value
    movies["Rating"].mean()    -> arithmetic average
    movies["Rating"].median()  -> middle value when ordered
    movies["Rating"].describe() -> summary statistics

## 12. A useful distinction

There are two different questions:

"What is the highest rating?"
    movies["Rating"].max()

"Which movie has the highest rating?"
    movies.loc[movies["Rating"].idxmax(), "Title"]

The second question requires locating the row associated with the maximum value. You can keep this as a teacher demonstration or challenge rather than a core requirement in Lesson 5.

## 13. Suggested teaching principle

Do not ask students to memorize commands without context.

Use this sequence:
    Question -> choose information -> choose command -> run code -> interpret result

Example:
Question:
"What is the average rating?"

Information:
Rating column

Command:
movies["Rating"].mean()

Interpretation:
"The average rating is approximately 8.0."

## 14. Important setup note

The CSV and Python files must be in the same folder unless you provide a different file path.

If `python` is not recognized on Windows, try:
    py --version

and:
    py -m pip install pandas

If Pandas is installed but Python still cannot be found, the problem is the Python installation/PATH configuration rather than Pandas itself.
