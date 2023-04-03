import discord
from Helper.Util import *
from Constant.Messages import *
from Constant.Tokens import *
from Constant.Paths import *
from Classes.ResponseContent import *

async def sendText(message, text):
    await message.channel.send(text)

async def sendLocalImage(message, file):
    with open(COLLECTION_PATH + file, 'rb') as f:
        pic = discord.File(f,file)
    await message.channel.send(file=pic)

async def sendMessageReply(message, content):
    if content.embed:
        await message.reply(embed=content.embed)
    elif content.file:
        await message.reply(file=content.file)
    elif content.text:
        await message.reply(content.text)
    else:
        await message.reply(ERROR_EXCEPTION_MESSAGE)