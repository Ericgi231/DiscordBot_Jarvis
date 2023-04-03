import discord
import random
import re
from Classes.ResponseContent import *
from Constant.Messages import *
from Constant.Tokens import *
from Constant.Paths import *
from googlesearch import search

def manPageAction(text):
    if text == "":
        lines = open('Data/Mans.txt').read().splitlines()
        myline =random.choice(lines)
        page = myline.split()[0]
        myline = myline.split("(")[1]
        num = re.search('[0-9]+', myline).group()
        url = "https://man7.org/linux/man-pages/man" + num + "/"+page+"."+num+".html"
        return [ResponseContent(text=url)]
    else:
        query = text + " site:man7.org/linux/man-pages"
        for url in search(query, num_results=1):
            return [ResponseContent(text=url)]