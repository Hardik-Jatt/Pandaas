import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35]})
print(df)
#     Name  Age
# 0  Alice   25
# 1    Bob   30
# 2  Charlie  35

# Creating a DataFrame from Dictionaries
data = [{'Name': 'Alice', 'Age': 25},
        {'Name': 'Bob', 'Age': 30},
        {'Name': 'Charlie', 'Age': 35}]
df_from_dict = pd.DataFrame(data)
print(df_from_dict)
#     Name  Age
# 0  Alice   25
# 1    Bob   30
# 2  Charlie  35

# Creating a DataFrame from a CSV File
df_from_csv = pd.read_csv('data.csv')
print(df_from_csv)
#     Name  Age
# 0  Alice   25
# 1    Bob   30
# 2  Charlie  35

# Data Inspection Functions and their Meaning

## `head()`
print(df_from_csv.head())
#     Name  Age
# 0  Alice   25
# 1    Bob   30
# 2  Charlie  35
# Returns the first 5 rows of the DataFrame by default.

## `tail()`
print(df_from_csv.tail())
#     Name  Age
# 0  Alice   25
# 1    Bob   30
# 2  Charlie  35
# Returns the last 5 rows of the DataFrame by default.

## `shape`
print(df_from_csv.shape)
# (3, 2)
# Returns a tuple representing the dimensionality of the DataFrame (rows, columns).

## `info()`
df_from_csv.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64
# dtypes: int64(1), object(1)
# memory usage: 168.0+ bytes
# Provides a concise summary of the DataFrame, including the index range, column names, data types, and memory usage.

## `describe()`
print(df_from_csv.describe())
#        Age
# count   3.0
# mean   30.0
# std     5.0
# min    25.0
# 25%    27.5
# 50%    30.0
# 75%    32.5
# max    35.0
# Generates descriptive statistics for the DataFrame, including count, mean, standard deviation, minimum, maximum, and quartiles.
