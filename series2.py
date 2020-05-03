import pandas as pd
#以列表資料為底，建立Series
# data = pd.Series([100,200,300],index=['A','B','C'])  #len(index)==len(list), 預設 0,1,2...
# #印出 dtype 屬性
# print(data.dtype)
# #印出 size 屬性
# print(data.size)
# print(data.index)
# #根據順序或索引 取直
# print(data['A'])
#
# #取得資料
# print(data)
# print(data[2],data['C'])

#數字運算
# print("Max",data.max())
# print("Sum",data.sum())
# print("平均值",data.mean())
# print("表準差",data.std())
# print("中位數",data.median())
# print("最大的二個數\n",data.nlargest(2))    #nsmallest(2)
################################################

data = pd.Series(["您好","Python","Pandas"])
print(data)
print(data.str.lower()) #全部小寫
print(data.str.len())   #長度迴腸
print(data.str.cat(sep="-")) #用某個字串串起來 回傳str
print(data.str.contains("P")) #每列是否有特定字串
print(data.str.replace("您好","HELLO")) #取代
print(data)