import pandas as pd
#############################
#Series 單維度

content = [1,2,3]
data=pd.Series(content)
data.max()      #找到最大值
data.median()   #計算中位數
data=data*2     #放大兩倍

############################
#DataFrame 表格
data=pd.DataFrame('dict')
data["欄位名稱"]
data.iloc['列編號']    #由0開始