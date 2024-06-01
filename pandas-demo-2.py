import pandas as pd

nba_df = pd.read_csv("nba.csv")
result = nba_df

# İlk 10 kayıt
result = nba_df.head(10)
# Toplam kayıt sayısı
result = len(nba_df.index)
# Tüm oyuncuların yaş ortalaması
result = nba_df["age"].mean()
# En büyük yaş kaç kaç ve kim
result = nba_df["age"].max()
result = nba_df[nba_df["age"] == nba_df["age"].max()][["player_name","age"]]
# Yaşı 20-25 arasında olan oyuncuların isimleri ve takımları
result = nba_df[(nba_df["age"]<25) & (nba_df["age"]>20)][["player_name","age","team_abbreviation"]]
# John Holland adlı oyuncunun oynadığı takım
result = nba_df[nba_df["player_name"] == "John Holland"][["player_name","team_abbreviation"]]
# Takımlara göre oyuncuların ortalama maaş bilgisi
result = nba_df.groupby("team_abbreviation")["age"].mean()
# Kaç farklı takım mevcut
result = nba_df["team_abbreviation"].nunique() # len(nba_df.groupby("team_abbreviation"))
# Her takımda kaç oyuncu oynamakta
result = nba_df["team_abbreviation"].value_counts()
# İsminin içinde "and" geçen kayıtlar
nba_df.dropna(inplace=True)
def str_find(name):
    return "and" in name.lower()
result = nba_df[nba_df["player_name"].apply(str_find)]["player_name"]

print(result)