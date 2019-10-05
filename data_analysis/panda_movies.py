import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\B5400\\PycharmProjects\\Szkolenie_PWN\\pandas_exercise\\movie_metadata.csv', index_col='movie_title')

genres_split = df['genres'].str.split('|', n=1, expand=True)[0].value_counts()
print(genres_split)

# df['duration'].plot(kind='hist')
# plt.show()