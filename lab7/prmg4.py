import pandas as pd

df = pd.read_csv('1experience.csv')

print("Contents of the DataFrame:")
print(df)

num_rows, num_columns = df.shape
print(f"\nTotal Rows: {num_rows}")
print(f"Total Columns: {num_columns}")

df_length = len(df)
print(f"\nLength of DataFrame: {df_length}")

print("\nFirst 2 Rows of the DataFrame:")
print(df.head(2))