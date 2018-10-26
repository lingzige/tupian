# coding=utf-8

import pandas as pd

df = pd.read_csv('./IMDB-Movie-Data.csv')
actor_list = df['Actors'].str.split(', ').tolist()
# print(actor_list)

actor = [j for i in actor_list for j in i]
print(len(set(actor)))
