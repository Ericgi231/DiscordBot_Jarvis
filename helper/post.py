import re
import discord
import os
import random
import xmltodict
import requests
import json
from helper.post import *
from helper.util import *
from constant.messages import *
from constant.tokens import *
from constant.paths import *
from googlesearch import search

async def postText(message, text):
    await message.channel.send(text)
    print("Posted {0}".format(str(text).strip()))

async def postLocalImage(message, file):
    with open(COLLECTION_PATH + file, 'rb') as f:
        pic = discord.File(f,file)
    await message.channel.send(file=pic)
    print("Posted file {0}".format(file))

async def postWikiUrl(message, text):
    if text == "":
        wikiurl = "https://en.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1"
        data = requests.get(wikiurl)
        result = json.loads(data.content)
        word = result["query"]["random"][0]["title"].replace(" ","_")
        url = "https://en.wikipedia.org/wiki/" + word
        await message.channel.send(url)
        print(url)
    else:
        query = text + " site:en.wikipedia.org/wiki"
        for url in search(query, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(url)
            print(url)

async def postManPageUrl(message, text):
    if text == "":
        lines = open('data/mans.txt').read().splitlines()
        myline =random.choice(lines)
        page = myline.split()[0]
        myline = myline.split("(")[1]
        num = re.search('[0-9]+', myline).group()
        url = "https://man7.org/linux/man-pages/man" + num + "/"+page+"."+num+".html"
        await message.channel.send(url)
        print(url)
    else:
        query = text + " site:man7.org/linux/man-pages"
        for url in search(query, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(url)
            print(url)

async def postGoogleSearchUrl(message, text):
    if text == "":
        text = getRandomWords()
    query = text
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        await message.channel.send(url)
        print(url)

async def postImageFromCollection(message, count, tags):
    files = os.listdir(COLLECTION_PATH)
    if tags != "":
        #replace spaces with underscores
        tags = tags.replace(' ', '_')
        #filter files with tags
        files_filtered = [i for i in files if tags in i.lower()]
        if len(files_filtered) == 0:
            print("Failed to find image with tags, aborting...")
            await message.channel.send("Failed to find `"+tags+"` image")
            return
    else:
        files_filtered = files

    #select and post each image
    for n in range(count):
        failCount = 0
        size = 8000001
        while size > 8000000:
            d = random.choice(files_filtered)
            size = os.stat(COLLECTION_PATH+d).st_size
            print("Selected " + d + " - " + str(size) + " B")
            if size > 8000000:
                failCount += 1
                if failCount > 3:
                    print("Failed too many times, aborting...")
                    await message.channel.send("Failed to find image under 8mb with tag `" + tags + "`")
                    return
                print("(" + str(failCount) + ") File to large, selecting new...")
        await postLocalImage(message, d)

async def postPornUrl(message, count, tags):
    for n in range(count):
        r34url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index"
        if tags != "":
            tags = tags.replace(' ','+')
            r34url += "&tags=" + tags
        else:
            r34url += "&tags=*"
        pre_data = requests.get(r34url+"&limit=0")
        pre_xml = xmltodict.parse(pre_data.content)
        total = int(pre_xml["posts"]["@count"])
        url = ""
        if total > 0:
            if total > 2000:
                total = random.randint(0,2000)
            pid = random.randint(0,int(total/100))
            r34url += "&pid=" + str(pid)
            data = requests.get(r34url)
            xml = xmltodict.parse(data.content)
            if total == 1:
                url = xml["posts"]["post"]["@file_url"]
            else:
                total_img = len(xml["posts"]["post"])
                num = random.randint(0,total_img-1)
                url = xml["posts"]["post"][num]["@file_url"]

        if url != "":
            print(url + " Selected")
            await message.channel.send(url)
            print(url + " Posted")
        else:
            print("Failed to find image")
            if len(tags.split()) > 1:
                await message.channel.send("No porn found with tags `"+ tags.replace(' ','`, `') + "`")
            else:
                await message.channel.send("No porn found with tag `" + tags + "`")
            break

async def postUnsplashUrl(message, tags):
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
        print(downloadUrl + " Selected")
        embedV = discord.Embed(title=imageDescription.capitalize(), description="Hosted on [Unsplash](https://unsplash.com/?utm_source=jarvis&utm_medium=referral)", url=downloadUrl)
        embedV.set_image(url=imageUrl)
        embedV.set_author(url=imageUserUrl,name=imageUserName)
        await message.channel.send(embed=embedV)
        print(downloadUrl + " Posted")
    except:
        await message.channel.send("Failed to find anything to show you with tag `" + tags + "`")
        print("~~~ unsplash API Call Failed on " + tags + "  ~~~\n")