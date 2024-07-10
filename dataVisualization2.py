import matplotlib.pyplot as plt
import numpy as np

# yillar = np.arange(2020,2025)
# oyuncu1 = np.random.randint(0,12,5)
# oyuncu2 = np.random.randint(0,15,5)
# oyuncu3 = np.random.randint(0,25,5)
# # Stack Plot
#
# plt.plot([],[],color="y", label="oyuncu1")
# plt.plot([],[],color="r", label="oyuncu2")
# plt.plot([],[],color="b", label="oyuncu3")
# plt.stackplot(yillar,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
# plt.legend()
# plt.show()

# Pie Plot
# goal_types = ["Penaltı","Şut","Serbest Vuruş"]
# goals = [12,35,7]
# colors = ['y','r','b']
# plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0,0.05,0.05),autopct="%1.1f%%")
# plt.legend()
# plt.tight_layout()
# plt.show()

# Bar Plot
# plt.bar(["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"],[10,4,10,2,0], width=0.9,label="Ders Saati")
# plt.bar(["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"],[3,0,2,0,2], width=0.8,label="Spor Saati")
# plt.xlabel("Günler")
# plt.ylabel("Saatler")
# plt.legend()
# plt.show()

# Histogram Plot
yaslar = [22,55,62,45,21,2234,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115]
yasGrupları = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yasGrupları,histtype="bar",rwidth=0.9)
plt.title("Hist Plot")
plt.xlabel("Yaş grupları")
plt.ylabel("Kişi sayısı")
plt.legend()
plt.show()
