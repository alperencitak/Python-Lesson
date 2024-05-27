import pandas as pd

data = pd.read_csv("smartphones2.csv")
df = pd.DataFrame(data)
df.dropna(inplace=True)

# df["Smartphone"] = df["Smartphone"].str.lower()
# df["Smartphone"] = df["Smartphone"].str.upper()
# df["index"] = data["Smartphone"].str.find('a')
# result = df[df.Smartphone.str.contains("XIAOMI")]
# df.Smartphone = df.Smartphone.str.replace(' ','-').str.lower()
# result = df.columns

phone = df["Smartphone"].str.split('/', expand=True).drop(2,axis=1)
df = df.drop("Smartphone",axis=1)
df.insert(0,"Name", phone[0])
df.insert(1,"Info", phone[1])
df.drop("Free", axis=1, inplace=True)


print(df)