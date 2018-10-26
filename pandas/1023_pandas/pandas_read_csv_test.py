# coding=utf-8

import pandas as pd

df = pd.read_csv('./dogNames2.csv')

# 显示详细信息
# print(df.info())

# 显示前面几行
# print(df.head())

# 快速综合统计结果
# print(df.describe())

# 统计使用次数最多的名字
# num = df.sort_values(by="Count_AnimalName", ascending=False)
# print(num.head())

# 选择排好序之后的前100行
# df_sorted = df.sort_values(by="Count_AnimalName", ascending=False)
# print(df_sorted[:100])

# 在整个数据集中单独选择某一列
# print(df['Count_AnimalName'])
# 选择前100行，但是只有一列
# print(df[:100]['Count_AnimalName'])

# 找到使用次数超过800的狗的名字
# num = df[df['Count_AnimalName']>800]['Count_AnimalName']
# print(num)


# 大于800小于1000
# num = df[(800<df['Count_AnimalName'])&(df['Count_AnimalName']<1000)]
# print(num)

# 狗的名字的长度大于4，并且使用次数超过700
num = df[(df['Row_Labels'].str.len()>4)|(df['Count_AnimalName']>700)]
print(num)








