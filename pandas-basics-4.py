import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns=["Column1","Column2","Column3"])
result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]
# loc["row","column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[["A","B"]]
result = df.loc[["A","B"],["Column1","Column2"]]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column3"]
result = df.loc[:,"Column1":"Column2"]
result = df.loc[:,:"Column2"]
result = df.loc[:,"Column2":]
result = df.loc["B":,"Column2":]
result = df.loc[:"B",:"Column2"]
result = df.iloc[:,1:2]
result = df.iloc[0,1]
df["Column4"] = pd.Series(randn(3), ["A","B","C"])
df.loc["D"] = pd.Series(randn(4), ["Column1","Column2","Column3","Column4"])
df["Column5"] = df["Column1"] + df["Column3"]
df = df.drop("Column5", axis = 1)
df.drop("C", axis = 0, inplace=True) # inplace=True orjinali değiştirir.
result = df



print(result)
