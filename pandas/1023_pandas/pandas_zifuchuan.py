# coding=utf-8

import pandas as pd

df = pd.read_csv('./IMDB-Movie-Data.csv')
# print(df.head(1))
# print(df["info"].str.split('/'))
# print(df.info())
print(df['Actors'].str.split(",").tolist())
