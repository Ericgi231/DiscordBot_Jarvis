import requests
import json
from Classes.ResponseContent import *
from googlesearch import search

def wikiAction(text):
    try:
        if text == "":
            wikiurl = "https://en.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1"
            data = requests.get(wikiurl)
            result = json.loads(data.content)
            word = result["query"]["random"][0]["title"].replace(" ","_")
            url = "https://en.wikipedia.org/wiki/" + word
            return [ResponseContent(text=url)]
        else:
            query = text + " site:en.wikipedia.org/wiki"
            for url in search(query, num_results=1):
                return [ResponseContent(text=url)]
    except Exception as e:
        raise e