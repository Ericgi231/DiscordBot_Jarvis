import discord
import random
import requests
import json
from Classes.ResponseContent import *
from Constant.Messages import *
from Constant.Tokens import *

def postStockImageAction(tags):
    url = "https://api.unsplash.com/photos/random/?client_id=" + UNSPLASH_TOKEN
    if tags != "":
        tags = tags.replace(' ','+')
        url += "&query=" + tags
    data = requests.get(url)
    result = json.loads(data.content)
    try:
        imageUrl = result["urls"]["regular"]
        imageUserName = result["user"]["name"]
        imageUserUrl = result["user"]["links"]["html"]
        downloadUrl = result["links"]["download"]
        imageDescription = result["alt_description"]        
        if imageDescription == "null":
            imageDescription = tags
        embedV = discord.Embed(title=imageDescription.capitalize(), description="Hosted on [Unsplash](https://unsplash.com/?utm_source=jarvis&utm_medium=referral)", url=downloadUrl)
        embedV.set_image(url=imageUrl)
        embedV.set_author(url=imageUserUrl,name=imageUserName)
        return [ResponseContent(embed=embedV)]
    except Exception as e:
        return [ResponseContent(text="Failed to find anything to show you with tag `" + tags + "`")]