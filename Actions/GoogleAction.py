import random
from Classes.ResponseContent import *
from Constant.Messages import *
from Helper.Util import *
from googlesearch import search

def googleAction(text):
    if text == "":
        text = getRandomWords()
    query = text
    try:
        results = search(query, num_results=1)
        for url in results:
            return [ResponseContent(text=url)]
    except Exception as e:
        raise e