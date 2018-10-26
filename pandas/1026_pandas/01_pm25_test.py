# coding=utf-8
# 绘制出5个城市的pm2.5随时间的变化情况

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./PM2.5/BeijingPM20100101_20151231.csv')

# 这个方法可以把分开的时间字符串转化为pandas的时间类型
period = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'],freq='H')
# print(period)

df['datetime'] = period
# print(df.head(1))

# 将datetime设置为索引
df.set_index('datetime', inplace=True)
# 设置重采样
df = df.resample('7D').mean()
# print(df['PM_US Post']),因为已经将时间设置为索引了，所以直接删除值为nan的就可以了
data = df['PM_US Post'].dropna()
data_china = df['PM_Dongsi']
_x = data.index
_y = data.values

_x_china = data_china.index
_y_china = data_china.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y, label="US_POST")
plt.plot(range(len(_x_china)), _y_china, label="CN_POST")

plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
plt.legend(loc='best')
plt.show()
