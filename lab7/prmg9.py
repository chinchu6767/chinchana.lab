import pandas as pd

df = pd.read_csv("1experience.csv")

description = df.describe()

quantiles = df['YearsExperience'].quantile([0.25,0.5,0.75])

skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()

value_counts = df['YearsExperience'].value_counts()

print("Statistical Summary:\n",description)
print("\nQuantiles:\n",quantiles)
print("\nSkewness:",skewness)
print("Kurtosis:",kurtosis)
print("\nValue Counts:\n",value_counts)