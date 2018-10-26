# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('./911.csv')
# print(df.head(1))
# print(df.info())

# split之后，temp_list是一个series类型,tolist是变成一个大列表，也即是大列表中嵌套小列表
temp_list = df['title'].str.split(":").tolist()
# print(temp_list)

# cate_list为只包含三个元素的列表
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造一个全为0的数组，将出现这个三个元素的地方赋值为1
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
# print(zeros_df)

# 遍历，将出现的地方赋值为1
for cate in cate_list:
	zeros_df[cate][df['title'].str.contains(cate)] = 1
print(zeros_df.sum(axis=0))
	# break
