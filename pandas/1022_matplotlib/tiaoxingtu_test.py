# coding=utf-8

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc")
a = ["战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2","战狼2"]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

_x = range(len(a))
_y = b
plt.figure(figsize=(20,8), dpi=80)

plt.bar(_x, b, width=0.3)
plt.xticks(_x, a, fontproperties=my_font, rotation=90)

plt.show()

