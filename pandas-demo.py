import pandas as pd

# Dosya hakkındaki bilgiler
df = pd.read_csv("imdb (1000 movies) in june 2022.csv")
result = df.columns

# İlk 5 ve 10 kayıt
result = df.head()
result = df.head(10)

# Son 5 ve 10 kayıt
result = df.tail()
result = df.tail(10)

# Sadece film ismi
result = df['movie name\r\n']
result = df['movie name\r\n'].head()

# Filtrelemeler
result = df[['movie name\r\n','RATING']]
result = df[['movie name\r\n','RATING']].head()
result = df[['movie name\r\n','RATING']].tail(7)
result = df[5:][['movie name\r\n','RATING']].head()
result = df[['movie name\r\n','RATING']][df['RATING'] >= 8.5].head(50)
result = df[['movie name\r\n','runtime']][(df['runtime'] >= '100') & (df['runtime'] <= '170')].head(50)

print(result)