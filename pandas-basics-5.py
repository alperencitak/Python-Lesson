import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])
result = df
result = df.columns
result = df.head(5) # result = df.iloc[0:5]
result = df.tail(5) # result = df.iloc[-5:]
result = df["Column1"].head(5)
result = df.Column1.head(5)
result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()
result = df[df > 50]
result = df["Column1"][df["Column1"] > 50]
result = df.Column2[df["Column1"] > 50]
result = df[["Column1","Column2"]][df[["Column1","Column2"]] > 50]
result = df.Column1[(df["Column1"] > 50) & (df["Column1"] % 2 == 0) ]
result = df.Column1[((df["Column1"] > 50) & (df["Column1"] % 2 != 0)) | (df["Column1"] % 2 == 0) ]
result = df[["Column1","Column2"]].query("Column1 >= 50 & Column1 % 2 == 0")



print(result)