import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")
result = soup.find_all("li",{"class":"column"},limit=10)
for res in result:
    link = res.a.get("href")
    p_name = res.a.h3.text
    images = res.find("img",{"class":"cardImage"}).get("data-images").split(",")
    price = res.find("div",{"class":"priceContainer"}).find_all("span")[-1].ins.text.strip(" TL")
    print(price)
