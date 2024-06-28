import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                   'Age': [25, 32, 18, 47, 33],
                   'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']})

## Indexing and Slicing

# Indexing using .loc
print(df.loc[1])  # Access row by label
print(df.loc[:, 'Name'])  # Access column by label
print(df.loc[1:3, 'Name':'City'])  # Access range of rows and columns by label

# Indexing using .iloc 
print(df.iloc[1])  # Access row by integer position
print(df.iloc[:, 0])  # Access column by integer position
print(df.iloc[1:4, 0:2])  # Access range of rows and columns by integer position

## Data Manipulation and Transformation

# Filtering
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Sorting
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)

# Applying functions
df['Age_Squared'] = df['Age'] ** 2
print(df)

# Handling missing data
df['City'] = df['City'].fillna('Unknown')
print(df)

## Reshaping

# Melting (converting wide to long format)
melted_df = pd.melt(df, id_vars=['Name'], var_name='Attribute', value_name='Value')
print(melted_df)

# Pivoting (converting long to wide format)
pivoted_df = melted_df.pivot(index='Name', columns='Attribute', values='Value')
print(pivoted_df)

# Stacking (converting columns to rows)
stacked_df = df.set_index(['Name', 'City']).stack()
print(stacked_df)

# Unstacking (converting rows to columns)
unstacked_df = stacked_df.unstack()
print(unstacked_df)
