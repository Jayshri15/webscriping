import requests
from bs4 import BeautifulSoup
import json
page = requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
_soup = BeautifulSoup(page.text,"html.parser")

def scrape():
    list = []
    div = _soup.find("div",class_ = "body_main container")
    tbody = div.find("table",class_ = "table")
    var = tbody.find_all("tr")
    for i in var:
        dict = {}
        td = i.find_all("td")
        for j in td:
            rank = i.find("td",class_ = "bold").get_text()[:-1]
            dict["Rank"] = int(rank)
            rating = i.find("span",class_ = "tMeterScore").get_text()[1:3]
            dict["Rating"] = int(rating)
            review = i.find("td",class_ = "right hidden-xs").get_text()
            dict["Review"] = int(review)
            movieName = i.find("a",class_ = "unstyled articleLink")["href"][3:]
            dict["movieName"] = movieName
            movieurl = i.find("a",class_ = "unstyled articleLink")["href"]
            url = "https://www.rottentomatoes.com" + movieurl
            dict["Url"] = url
            Year = i.find("a",class_ = "unstyled articleLink").get_text()
            year = Year.strip()
            dict["Year"] = int(year[-5:-1])
        list.append(dict.copy())
        if {} in list:
            list.remove({})
    with open("task1.json","w+") as file:
        json.dump(list,file,indent = 4)
    return list
movie_data = scrape()














































