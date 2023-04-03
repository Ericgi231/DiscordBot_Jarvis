import discord
import random
import os
from Classes.ResponseContent import *
from Constant.Messages import *
from Constant.Tokens import *
from Constant.Paths import *

def postMemeAction(count, tags):
    files = os.listdir(COLLECTION_PATH)
    if tags != "":
        #replace spaces with underscores
        tags = tags.replace(' ', '_')
        #filter files with tags
        files_filtered = [i for i in files if tags in i.lower()]
        if len(files_filtered) == 0:
            print("Failed to find image with tags, aborting...")
            return ResponseContent(text="Failed to find `"+tags+"` image")
    else:
        files_filtered = files

    responses = []
    #select and post each image
    for n in range(count):
        failCount = 0
        size = 8000001
        while size > 8000000:
            d = random.choice(files_filtered)
            size = os.stat(COLLECTION_PATH+d).st_size
            #print("Selected " + d + " - " + str(size) + " B")
            if size > 8000000:
                failCount += 1
                if failCount > 3:
                    print("Failed too many times, aborting...")
                    return ResponseContent(text="Failed to find image under 8mb with tag `" + tags + "`")
                print("(" + str(failCount) + ") File to large, selecting new...")
        with open(COLLECTION_PATH + d, 'rb') as f:
            pic = discord.File(f,d)
        responses.append(ResponseContent(file=pic))
    return responses