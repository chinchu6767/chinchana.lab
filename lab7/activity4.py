import pandas as pd

df = pd.read_csv('1experience.csv')

print("Last 3 rows of the DataFrame:")
print(df.tail(3))

print("\nDataFrame Description:")
print(df.describe())

print("\nDataFrame Info:")
df.info()

print("\nColumn Names:")
print(df.columns)