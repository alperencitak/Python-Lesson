from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://m.imdb.com/chart/top/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0"
    }
    html = requests.get(url,headers=headers).content
    soup = BeautifulSoup(html,"html.parser")
    list = soup.find("ul",{"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base"}).find_all("li", limit=15)
    for movie in list:
        print(movie.find("h3", {"class":"ipc-title__text"}).text + "  -  " + movie.find("span",{"class":"sc-b189961a-8 kLaxqf cli-title-metadata-item"}).text)