#載入 pandas 模組
import pandas as pd
#建立DataFrame
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "Salary":[3000,50000,15555]
})
#基本 DataFrame 操作
print(data)
print("------------------")
#取得特定的欄位
print(data["name"])
print("------------------")
print(data.iloc[0])
print(type(data.iloc[0]))