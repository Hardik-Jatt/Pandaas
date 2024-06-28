import pandas as pd
print("Pandas is installed.")

import numpy as np

# Creating Pandas DataFrames

## From Lists
data = [['Saurav', 25], ['Rashmi', 30], ['Uttam', 35]]
df_from_list = pd.DataFrame(data, columns=['Name', 'Age'])

## From Arrays
data = np.array([['Saurav', 25], ['Rashmi', 30], ['Uttam', 35]])
df_from_array = pd.DataFrame(data, columns=['Name', 'Age'])

## From Dictionaries
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df_from_dict = pd.DataFrame(data)

# Common Attributes

print(f"DataFrame shape: {df_from_list.shape}")
print(f"DataFrame columns: {df_from_list.columns}")
print(f"DataFrame data types: {df_from_list.dtypes}")
print(f"DataFrame head:\n{df_from_list.head()}")
print(f"DataFrame tail:\n{df_from_list.tail()}")

# Common Methods

df_from_list.info()
print(f"DataFrame description:\n{df_from_list.describe()}")
print(f"DataFrame sorted by Age:\n{df_from_list.sort_values(by='Age')}")
df_dropped = df_from_list.drop('Age', axis=1)
print(f"DataFrame with 'Age' column dropped:\n{df_dropped}")
