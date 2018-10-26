# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./IMDB-Movie-Data.csv')
# print(df.info())
# 呈现runtime和rationg的分布情况

# 选择图形，直方图
# 准备数据

# .values这个方法是将所以的数据取出来放到一个列表中，如果不加这个方法，
# 那么取出来的数据就是1000列的数据
runtime_data = df['Runtime (Minutes)'].values
# print(runtime_data)
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数,10代表的是组距
num_bin = (max_runtime - min_runtime)//5

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.hist(runtime_data, num_bin)
plt.xticks(range(min_runtime, max_runtime+5, 5))

plt.show()

