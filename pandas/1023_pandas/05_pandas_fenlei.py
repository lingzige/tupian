# coding=utf-8

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('./IMDB-Movie-Data.csv')

# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()

genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zero_df)

# 给每个电影出现的分类的位置赋值为1
for i in range(len(temp_list)):
	# temp_list[i]是一个列表
	zero_df.loc[i,temp_list[i]] = 1
# print(zero_df.head(3))
count = zero_df.sum(axis=0)
# print(count)
sort_values = count.sort_values()
# print(sort_values)

_x = sort_values.index
_y = sort_values.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), genre_list)
plt.show()
