import pandas as pd

data = pd.DataFrame

# data.iloc[0] 根據順序取一整列(Series)
# data.loc[0] 根據索引取一整列(Series)
# data[欄位名稱] 取一整攔(Series)
data = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "Salary": [3000, 50000, 10000]
}, index=['a', 'b', 'c'])

print(data)
print("------------------")
# 觀察資料
print("資料數量", data.size)
print("資料形狀(列,攔)", data.shape)
print("資料索引", data.index)

print("------------------")
# 取得(Row/橫向) 的 Series 資料(根據數據或索引)
print("取得第二列", data.iloc[1], sep='\n')
print("取得第c列", data.loc['c'], sep='\n')

# 取得(Column/直向) 的 Series 資料(根據名稱)
print("取得name欄位", data["name"], sep='\n')
print("把name轉大寫", data["name"].str.upper(), sep='\n')

# 計算薪水的平均值
print("薪水的平均值:", data["Salary"].mean(), sep='\n')

# 建立新的欄位 data["newColumnName"]=list/series
data["new"] = ["new1", "new2", "new3"]
data['rank']=pd.Series([3,6,1],index=['a','b','c'])
data["加薪100"]=data["Salary"]+100
print(data)