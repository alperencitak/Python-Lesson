import requests
import json

if __name__ == '__main__':
    class theMovieDb:
        def __init__(self):
            self.api_url = "https://api.themoviedb.org/3/"
            self.api_key = "apikey"

        def getPopularMovies(self):
            response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
            return response.json()

        def searchMovies(self,keywordStr):
            response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keywordStr}&US&page=1")
            return response.json()

    movieApi = theMovieDb()
    while True:
        selection = input("1- Popular Movies\n"
                          "2- Search Movies\n"
                          "3- Exit\n"
                          "Selection: ")

        if selection == '3':
            break
        elif selection == '1':
            result = movieApi.getPopularMovies()
            for movie in result["results"]:
                print(movie["original_title"])
            break
        elif selection == '2':
            keywordStr = input("Key: ")
            result = movieApi.searchMovies(keywordStr)
            for movie in result["results"]:
                print(movie["name"])
        else:
            print("Wrong Selection\n")

