import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [1,4,9,16]
#
# plt.plot(x,y, "o--b")
# plt.axis([0,6,0,20])
# plt.title("Graph Title")
# plt.xlabel("x label")
# plt.ylabel("y label")

# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="linear")
# plt.plot(x, x**2, label="quadratic")
# plt.plot(x, x**3, label="cubic")
#
# plt.title("Simple Matplotlib")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.legend()

# x = np.linspace(0, 2, 100)
#
# fig,axs = plt.subplots(3)
# axs[0].plot(x,x,color="red")
# axs[0].set_title("Linear")
# axs[1].plot(x,x**2,color="blue")
# axs[1].set_title("Quadratic")
# axs[2].plot(x,x**3,color="orange")
# axs[2].set_title("Cubic")
#
# plt.tight_layout()

# x = np.linspace(0, 2, 100)
#
# fig,axs = plt.subplots(2,2)
# fig.suptitle("Figure Title")
#
# axs[0,0].plot(x,x,color="red")
# axs[0,1].plot(x,x**2,color="blue")
# axs[1,0].plot(x,x**3,color="orange")
# axs[1,1].plot(x,x**4,color="green")

import pandas as pd

df = pd.read_csv("nbaData.csv")
df.drop(["player_name", "team_abbreviation", "college",
         'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts',
         'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct',
         'ast_pct', 'season','Unnamed: 0'], axis=1, inplace=True)
print(df.columns)
df = df.groupby("age").mean()
df.plot(subplots=True)
plt.legend()

plt.show()
