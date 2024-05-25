import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=["Column1","Column2","Column3"])
df = df.reindex(['a','b','c','d','e','f','g','h'])
result = df
# result = df.drop("Column1", axis=1)
# result = df.drop(['b','d'], axis=0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["Column1"].isnull().sum()
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn
result = df
result = df["Column1"][df["Column1"].isnull()]
result = df[df["Column4"].isnull()]["Column4"]
result = df[df["Column2"].notnull()]["Column2"]
result = df.dropna(axis=0) # nan değeri olmayan satırlar
result = df.dropna(axis=1) # nan değeri olmayan sütunlar
result = df.dropna(how="any")
result = df.dropna(how="all")
result = df.dropna(subset=["Column1","Column2"], how="all") # column2 ve column1 tamamen nan ise o satırı getirme
result = df.dropna(thresh=2) # satırında en az 2 normal veri olanlar
result = df.dropna(thresh=4)
result = df.fillna(value='empty') # nan yerine yazılacak değer
result = df.fillna(value=0)
result = df.sum().sum() / (df.size - df.isnull().sum().sum())


print(result)