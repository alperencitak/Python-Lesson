import pandas as pd
import numpy as np

employees = pd.read_json("employee.json")
df = pd.DataFrame(employees)
result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)
#
# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Tuzla")
result = df[["Departman","Yaş","Maaş"]].groupby("Departman").mean()
result = df[["Departman","Maaş"]].groupby("Departman").mean()
result = df.groupby("Departman")["Yaş"].mean()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].min()["Muhasebe"]


print(result)