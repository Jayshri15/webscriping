import json
from bs4 import BeautifulSoup
from task_1 import scrape
from task_4 import scrape_movie_details
movie=scrape()
def get_movie_list_details():
    list=[]
    for i in movie:
        a=scrape_movie_details(i["movieName"],i["Url"])
        list.append(a)
        print(list)
    with open ("task_5.json","w+") as file:
        json.dump(list,file,indent=4)
get_movie_list_details()