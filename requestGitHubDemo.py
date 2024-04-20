import requests
import json

if __name__ == '__main__':
    class GitHub:
        def __init__(self):
            self.api_url = 'https://api.github.com'
            self.currentUserUrl = {}
            self.currentUserReposUrl = {}

        def getUser(self,username):
            currentUserUrl = self.api_url + f"/users/{username}"
            response = requests.get(currentUserUrl)
            self.currentUserUrl = currentUserUrl
            self.currentUserReposUrl = currentUserUrl + "/repos"
            return response.json()
        def getRepos(self):
            repos = requests.get(self.currentUserReposUrl)
            return repos.json()

        def createRepo(self,token,name):
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
            response = requests.post(self.api_url + "/user/repos", headers=headers , json={
                "name": name,
                "description": "Bu senin deposu",
                "homepage": "https://github.com",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            })
            return response.json()

    gitHub = GitHub()

    while True:
        selection = input("1- Find User\n"
                      "2- Get Repositories\n"
                      "3- Create Repository\n"
                      "4- Exit\n"
                      "Selection: ")

        if selection=='4':
            break
        elif selection=='1':
            username = input("Usarname: ")
            result = gitHub.getUser(username)
            info = f"\nName: {result['name']}\nPublic repos: {result['public_repos']}\nFollowers: {result['followers']}\n".center(20,'*')
            print(info)
        elif selection=='2':
            result = gitHub.getRepos()
            print("\nRepositories:",end=" ")
            for repo in result:
                print(f"{repo['name']}",end="  ")
            print("\n")
        elif selection=='3':
            token = "token" #input()
            name = input("Repository Name: ")
            result = gitHub.createRepo(token,name)
            print(result)
        else:
            print("Wrong Selection\n")

