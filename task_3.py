import json

import requests
from bs4 import BeautifulSoup

file1=open("_task2.json")
movies=json.load(file1)
def num():
    years = []
    for year in movies:
        years.append(int(year))
    years.sort()
    d = {}
    i = 0
    start = years[i]
    for y in years:
        if y <= years[-1]:
            if start not in d:
                d[start] = []
                for yrs in movies:
                    if int(yrs) >= start and int(yrs) <= start + 10:
                       for k in movies[yrs]:
                           d[start].append(k)
            i = i + 1
        start=start + 10
    f = open("task_3.json","w")
    json.dump(d,f,indent = 4)
num()


















    

    






    




















