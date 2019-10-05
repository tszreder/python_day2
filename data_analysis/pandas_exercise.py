import pandas as pd
import numpy as np


df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

df1 = pd.DataFrame({
     'one': pd.Series(np.random.randn(2), index=['d', 'e']),
     'two': pd.Series(np.random.randn(3), index=['d', 'e', 'f'])
})

dfa = pd.DataFrame({'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],'Max Speed': [380., 370., 24., 26.]})

# print(dfa)
# print(dfa.groupby('Animal').mean())

# print(df)
# mean = df.mean()
# print(mean)
# print(df.max())
# print(df.corr())
# print(df.count())

# print(df.describe())

# print(df)

# print(df.sort_values('one', ascending=False))
# print(df.sort_values('one', ascending=True))
# print(df.sort_values(['one', 'two'], ascending=[True, True]))
# grouped = df.groupby('one')
# print(grouped.head())

# print(df.dropna())
# print(df.fillna(40))
# print(df.mean())
# print(df.fillna(df.mean()))
# df.append(df1)
# print(df.append(df1))
conc = pd.concat([df, df], axis=1)
print(conc)
