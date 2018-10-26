# coding=utf-8

# 统计不同月份的变化情况

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./911.csv')
df['timeStamp'] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)
count_res = df.resample("M").count()['title']
# print(count_res.head())

# 画图
_x = count_res.index
_y = count_res.values
_x = [i.strftime("%Y-%m-%d") for i in _x]
plt.figure(figsize=(20,8), dpi=80)

plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.show()
