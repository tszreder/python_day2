import pandas as pd

df = pd.read_csv('C:\\Users\\B5400\\Downloads\\pokemon.csv', header=[0])

print(df)

count = df.groupby('Type').count().sort_values('Pokemon', ascending=False)
print(count)