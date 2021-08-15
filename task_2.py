import requests
from bs4 import BeautifulSoup
import json

file = open("task1.json")
movies = json.load(file)
def num():
    nmo = {}
    for i in movies:
        movie_list = []
        year = i["Year"]
        if year not in nmo:
            for j in movies:
                if year == j["Year"]:
                    movie_list.append(j)
            nmo[year]=movie_list
    with open ("_task2.json","w+") as file:
        json.dump(nmo,file,indent=4)
        var = json.dumps(nmo)
num()























