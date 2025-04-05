import pandas as pd 
data = { 'name': ['alice', 'bob', 'charile', 'david'],
        'age': [25, 30, 35, 40],
        'salary': [50000, 60000, 70000, 800000]}

df = pd.DataFrame(data)
print("dataframe from scratch:")
print(df)

df['bonus'] = df['salary']* 0.10
print("\ndataframe after adding 'bonus' column:")
print(df)