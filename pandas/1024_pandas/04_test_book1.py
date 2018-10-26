# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./books.csv')
# print(df.head(1))
data1 = df[pd.notnull(df["original_publication_year"])]
# print(df)
data2 = df.groupby(by="original_publication_year").count()['book_id']
# print(data1)
data3 = data2.sort_values(ascending=False)
# print(data2)
_x = data3.index
_y = data3.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x)
plt.show()

