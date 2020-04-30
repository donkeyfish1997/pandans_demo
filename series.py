#載入 pandas 模組
import pandas as pd
#建立Series
data = pd.Series([10, 20, 15])
#基本 Series 操作
print(data)

print("Max", data.max())
print("Median", data.median())

data = data * 2
print(data)

data=data==20
print(data)
