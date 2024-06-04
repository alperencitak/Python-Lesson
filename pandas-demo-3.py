import pandas as pd

dfYoutube = pd.read_csv("USvideos.csv")

# İlk 10 kayıt
result = dfYoutube.head(10)
# İkinci 5 kayıt
result = dfYoutube[5:15].head()
# Kolon isimleri ve sayıları
result = dfYoutube.columns
result = len(dfYoutube.columns)
# Like ve dislike ortalamaları
result = dfYoutube["likes"].mean()
result = dfYoutube["dislikes"].mean()
# İlk 50 videonun isim, like ve dislike kolonları
result = dfYoutube.head(50)[["title","likes","dislikes"]]
# Bazı kolonların silinmesi
dfYoutube.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled','video_error_or_removed', 'description'],axis=1, inplace=True)
# En çok ve en az görüntülenen videolar
result = dfYoutube[["title","views"]].max()
result = dfYoutube[["title","views"]].min()
# En fazla görüntülenen ilk 10 video
def maxTenVideo(df, str):
    data = pd.DataFrame()
    for i in range(0,10):
        video = df[df[str] == df[str].max()]
        data = data._append(video, ignore_index=True)
        df.drop(video.index, axis=0, inplace=True)
    return data
result = maxTenVideo(dfYoutube,"views")[["title","views"]]
# ---Alternatif---
result = dfYoutube.sort_values("views",ascending=False)[["title","views"]].head(10)
# Kategoriye göre beğeni ortalamaları
result = dfYoutube.groupby("category_id")["likes"].mean()
# Kategoriye göre yorum sayılarının çoktan aza sırası
result = dfYoutube.groupby("category_id")["comment_count"].count().sort_values(ascending=False)
# Her kategorideki video sayısı
result = dfYoutube["category_id"].value_counts()
# Her videonun title uzunluğunun yeni bir kolonda kayıt edilmesi
dfYoutube["title_len"] = dfYoutube["title"].apply(len)
result = dfYoutube[["title","title_len"]]
# Her video için kullanılan tag sayısı
dfYoutube["tag_count"] = dfYoutube["tags"].apply(lambda x: len(x.split("|")))
result = dfYoutube[["title","tag_count"]]
# Like / dislike oranına göre en popüler 10 video
def popularity(df):
    likeList = list(df["likes"])
    dislikeList = list(df["dislikes"])
    likesanddislikesList = zip(likeList,dislikeList)
    popular = []
    for like,dislike in likesanddislikesList:
        if (like + dislike) == 0:
            popular.append(0)
        else:
            popular.append(like / (like + dislike))
    return popular
dfYoutube["popularity"] = popularity(dfYoutube)
result = dfYoutube[["likes","dislikes","popularity"]].sort_values("popularity",ascending=False)


print(result)