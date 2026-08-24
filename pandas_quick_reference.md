# Pandas Quick Reference - Student

```python
import pandas as pd
```

Load a CSV:
```python
movies = pd.read_csv("movies.csv")
```

First rows:
```python
movies.head()
```

Last rows:
```python
movies.tail()
```

Column names:
```python
movies.columns
```

Rows and columns:
```python
movies.shape
```

Dataset information:
```python
movies.info()
```

One column:
```python
movies["Rating"]
```

Highest:
```python
movies["Rating"].max()
```

Lowest:
```python
movies["Rating"].min()
```

Average:
```python
movies["Rating"].mean()
```

Median:
```python
movies["Rating"].median()
```

Summary:
```python
movies["Rating"].describe()
```
