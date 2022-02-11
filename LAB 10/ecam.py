import pandas as pd

df = pd.read_csv('Data/credit.csv')

print(df)
print(df.describe())
print(df.columns)
print(df.plot)
df.plot