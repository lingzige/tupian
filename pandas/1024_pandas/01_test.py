# coding=utf-8

import pandas as pd

df = pd.read_csv('./starbucks_store_worldwide.csv')
# print(df.info())
# print(df.head(1))
# 按照国家进行分组,按照国家和省份进行分组
grouped = df.groupby(by=["Country","State/Province"]).count()
# print(df['Brand'])
print(grouped.index)
# country可以进行遍历
# 可以调用聚合方法
# for i in country:
#	print(i)
#	print("*"*100)
# country_count = country['Brand'].count()
# print(country_count['US'])
# print(country_count['CN'])
# 统计中国每个省份店铺的数量
# china_data = df[df["Country"]=='CN']
# result = china_data.groupby(by="State/Province").count()["Brand"]

# print(result)
# for i in grouped:
#	print(i)
#	print("*"*100)
