    
import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

header("1. load hard-coded data into a df")

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
# This example shows that you select by the column you want to sort by.
header("6. df.sort_values('record_high', ascending=False)")
print(df.sort_values('record_high', ascending=False))

"""
SLICING
"""
# 7. slicing records
"""
SINGLE COLUMN
"""
header("7. slicing -- df.avg_low")
print(df.avg_low) #index with a single column

"""
SINGLE COLUMN
"""
header("7. slicing -- df['avg_low)")
print(df['avg_low']) #same as above, just different syntax

"""
SINGLE COLUMN, SORTED!
"""
header("7. slicing -- single row, sorted! df['avg_low)")
print(df.sort_values('avg_low', ascending=False)['avg_low'])  # way to sort values in single row

"""
SLICE OF ROWS
"""
header("7. slicing -- df[2:4]")
print(df[2:4]) #slice out specific rows, 2 to 3

"""
MULTIPLE COLUMNS FROM DATAFRAME - NOTE: DOUBLE BRACKET
"""
header("7. slicing -- df[['avg_low', 'avg_high']]")
print(df[['avg_low', 'avg_high']])

"""
MULTIPLE COLUMNS df.loc - SUPPORTS ROW SELECTION, and COL SELECTION
"""
header("7. slicing -- df.loc[:, ['avg_low', avg_high']]")
print(df.loc[:, ['avg_low', 'avg_high']])

"""
SPECIFIC ROW and COL df.loc
"""
header("7. slicing scalar value -- df.low[9, ['avg_precipitation']]")
print(df.loc[9, ['avg_precipitation']])

"""
INDEX LOCATION df.iloc
USE INDEXES TO GET VALUES, both ROWS AND COLUMNS
"""
header("7. df.iloc[3:5], [0,3]")
print(df.iloc[3:5], [0,3]) # slice or rows 3 - 4, and columns 3 and 5

"""
8. FILTERING
"""
# 8. Filter
header("8. df[df.avg_precipitation . 1.0]") # Filter on column values
# NOTE returns a boolean, and interprets by returning those values evaluated by the expression
print(df[df.avg_precipitation > 1.0])

# WAY TO CHECK IF A VALUE IS WITHIN A CERTAIN COLUMN
# NOTE returns the values that are found
header("8. df[df['month'].isin(['Jun','Jul','Aug'])")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

"""
ASSIGNMENT
"""
# Smimilar to slicing
header("9/ df.loc[9, ['avg_precipitation']] = 101.3")
df.loc[9, ['avg_precipitation']] = 101.3
print(df.iloc[9:11])

# NOTE setting a value to null
header("9. df.loc[9, ['avg_precipitation']] = np.nan")
df.loc[9, ['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:, 'avg_low'] = np.array([5] *len(df)")
df.loc[:, ['avg_low']] = np.array([5] *len(df))
print(df.head())

# ADDING A NEW COLUMN TO DATAFRAME
# NOTE can be done with any data in dataframe, whether calculated, aggregated or assigned
header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2 ")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())
