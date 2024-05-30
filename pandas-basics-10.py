import pandas as pd
import numpy as np

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[25,10,20,13,25],
    "Column3":["abc","bcaa","ae","cba","defda"]
}

def kareAl(x):
    return x**2

kareAl2 = lambda x: x*x
df = pd.DataFrame(data)

result = df.Column2.unique() # Aynı ifadeleri 1 kere gösterir
result = df.Column2.nunique() # Aynı ifadeler 1 kere gösterilince kaç eleman var
result = df.Column2.value_counts() # Aynı değerlerin sayısı
result = df["Column2"] * 2
result = df["Column1"].apply(kareAl) # Method uygula
result = df["Column1"].apply(kareAl2)
result = df["Column1"].apply(lambda x: x*2)
result = df["Column3"].apply(len)
df["Column4"] = result
result = df
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info
result = df.sort_values("Column2") # Integer ifade olduğundan küçükten büyüğe sıralar
result = df.sort_values("Column2", ascending=False) # büyükten küçüğe sıralar
result = df.sort_values("Column3") # String ifade olduğundan alfabetik sıralar
result = df.sort_values("Column3", ascending=False) # alfabetikte tersten sıralar

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Mayıs"],
    "Kategori": ["Elektronik","Elektronik","Kitap","Kitap","Kitap","Kitap"],
    "Gelir": [20,30,15,14,32,42]
}
df = pd.DataFrame(data)

result = df
result = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

print(result)