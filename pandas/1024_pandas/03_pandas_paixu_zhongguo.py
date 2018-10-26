# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
df = pd.read_csv('./starbucks_store_worldwide.csv')
df = df[df['Country']=='CN']

data1 = df.groupby(by='City').count()['Brand'].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

plt.figure(figsize=(20,8),dpi=80)

# plt.bar(range(len(_x)),_y, width=0.3, color='orange')

plt.barh(range(len(_x)),_y, height=0.3, color='orange')
plt.yticks(range(len(_x)),_x, fontproperties=my_font)

plt.show()
