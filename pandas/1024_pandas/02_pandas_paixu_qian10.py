# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./starbucks_store_worldwide.csv')

# 绘制排名前十的国家的星巴克数量
# 准备数据

# 按国家分列，统计数每列的总数,但是我们只需要一列的数据
data1 = df.groupby(by="Country").count()['Brand']

# 按照降序进行排列，并选出其中排名前十的数据
data2 = data1.sort_values(ascending=False)[:10]
# print(data2)
# print(data1)

# 绘图
_x = data2.index
_y = data2.values

plt.figure(figsize=(20,8), dpi=80)

plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
