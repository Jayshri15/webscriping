import requests
import os
import json 
from task_4 import scrape_movie_details
from task_1 import scrape
movie = scrape()
def num():
    list = []
    for i in movie:
        path = "/home/dell42/Desktop/web_scaping/all_files/"+i["movieName"]+".text"
        if os.path.exists(path):
            pass
        else :
            create = open("/home/dell42/Desktop/web_scaping/all_files/"+ i["movieName"] + ".text","w")
            url = requests.get(i["Url"])
            create1= create.write(url.text)
            create.close()
num()                       





















