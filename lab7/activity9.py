import pandas as pd

data = pd.read_csv('2salary.csv')

print("Dataset Preview:")
print(data.head())

print("\nCentral Tendencies:")
print("Mean:\n", data.mean())
print("Median:\n", data.median())
print("Mode:\n", data.mode().iloc[0])

print("\nMeasures of Dispersion:")
print("Standard Deviation:\n", data.std())
print("Variance:\n", data.var())
print("Range:\n", data.max() - data.min())