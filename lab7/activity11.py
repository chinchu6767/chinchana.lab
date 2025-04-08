import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler

df = pd.read_csv(r"3Salary_Data.csv")

print("Original Data:")
print(df.head())

normalizer = Normalizer()
normalized_data = normalizer.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Data:")
print(normalized_df.head())

min_max_scaler = MinMaxScaler()
min_max_scaled_data = min_max_scaler.fit_transform(df)
min_max_df = pd.DataFrame(min_max_scaled_data, columns=df.columns)

print("\nMin-Max Scaled Data:")
print(min_max_df.head())