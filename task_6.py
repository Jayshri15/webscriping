import json
from bs4 import BeautifulSoup
with open ("task_5.json","r") as f:
    data = json.load(f)

def analyse_movies_language():
    dict1 = {}
    for dic in data:
        if "language" in dic:
            language = dic ["language"]
            if language not in dict1:
                language  = dic["language"]
                dict1[language] = 1
            else:
                dict1[language] += 1
        else:
            continue
    with open ("task_6.json","w+") as f:
        json.dump(dict1,f,indent=4)
analyse_movies_language()

