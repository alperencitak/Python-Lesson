import pandas as pd

# series1 = pd.Series([3,2,0,1])
# series2 = pd.Series([0,3,7,2])
#
# data = dict(apples = series1, oranges = series2)
# df = pd.DataFrame(data)
# print(df)

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# data = [["Ahmet",50],["Ali",60],["Yagmur",70]]
# df = pd.DataFrame(data, index=[1,2,3], columns=["Name","Grade"])
# dict = {"Name":["Ahmet", "Ali", "Yagmur"],"Grade":[50, 60, 70]}
dict = [
          {"Name":"Ahmet","Grade":50},
          {"Name":"Ali","Grade":60},
          {"Name":"Yagmur","Grade":70},
          {"Name":"Ayse","Grade":65}
       ]
df = pd.DataFrame(dict)

print(df)
