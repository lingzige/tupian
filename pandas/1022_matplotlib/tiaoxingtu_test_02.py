# coding=utf-8

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc")

a = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14]
x_16 = [i+0.2*2 for i in x_14]
plt.figure(figsize=(20,8), dpi=80)

plt.bar(x_14, b_14, width=0.2)
plt.bar(x_15, b_15, width=0.2)
plt.bar(x_16, b_16, width=0.2)

plt.xticks(x_14, a, fontproperties=my_font)

plt.show()
