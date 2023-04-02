import discord
import random
from helper.post import *
from helper.util import *
from constant.messages import *
from constant.tokens import *
from constant.paths import *
from constant.values import *
from constant.keyWords import *

INTENTS = discord.Intents.all()
CLIENT = discord.Client(intents=INTENTS)

async def respondToInvalidMessage(message):
    await postText(message, getRandomWords())

async def respondToMessage(message, text):
    print("### Responding to {0} ###".format(text))
    if text.startswith(HELP):
        await postText(message, HELP_MESSAGE)
    elif text.startswith(tuple(HELLO)):
        await postText(message, HELLO_MESSAGE)
    elif text.startswith(THANK):
        await postLocalImage(message, OH_NO_CRINGE_FILE)
    elif text.startswith(WHEN):
        await postText(message, getRandomDateTimeString())
    elif text.startswith(tuple(WILL)):
        await postText(message, random.choice(MAGIC_EIGHT_BALL_MESSAGES))
    elif text.startswith(tuple(MANY)):
        await postText(message, random.randint(-MAX_RANDOM_NUMBER,MAX_RANDOM_NUMBER))
    elif text.startswith(GOOGLE):
        await postGoogleSearchUrl(message, trimFirstWord(text))
    elif text.startswith(WIKI):
        await postWikiUrl(message, trimFirstWord(text))
    elif text.startswith(MAN):
        await postManPageUrl(message, trimFirstWord(text))
    elif text.startswith(tuple(SHOW)):
        await respondToPostMessage(message, trimFirstWord(text))
    else:
        await respondToInvalidMessage(message)
    print("### Responded to {0} ###\n".format(text))

async def respondToPostMessage(message, text):
    if text == "":
        await postText(message, ERROR_INVALID_USE_MESSAGE)
        return
    text = trimFillerIfPresent(text, ME)
    if text == "":
        await postText(message, ERROR_INVALID_USE_MESSAGE)
        return
    keyword = text.split()[-1]
    count = 1
    if text.split()[0].isnumeric():
        count = int(text.split()[0])
        text = trimFirstWord(text)
    elif isAlphaToNumeric(text.split()[0]):
        count = alphaToNumeric(text.split()[0])
        text = trimFirstWord(text)
    if count > POST_LIMIT:
        await postText(message, ERROR_OVER_LIMIT_MESSAGE)
        return
    if keyword.startswith(tuple(MEME)):
        await postImageFromCollection(message, count, trimLastWord(text))
    elif keyword.startswith(tuple(PORN)):
        await postPornUrl(message, count, trimLastWord(text))
    else:
        await postUnsplashUrl(message, text)

async def randomNo(message):
    if random.randint(0,FAIL_CHANCE) == 0:
        print("### Jarvis is saying no ###")
        await postText(message, random.choice(NEGATIVE_MESSAGES))
        return 1
    return 0 

async def readInject(message):
    with open('data/inject.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    if len(data) > 0:
        print("### Jarvis saying injected word ###")
        await postText(message, data[0])
        with open('data/inject.txt', 'w') as fout:
            fout.writelines(data[1:])
        return 1
    return 0 

@CLIENT.event
async def on_ready():
    print('We have logged in as {0.user}\n'.format(CLIENT))

@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return
    text = message.content.lower()
    if not text.startswith(JARVIS):
        return
    if await randomNo(message):
        print("### Jarvis said no ###\n")
        return
    if await readInject(message):
        print("### Jarvis said injected word ###\n")
        return
    text = trimFirstWord(text)
    try:
        text = trimFillerIfPresent(text, PLEASE)
        await respondToMessage(message, text)
    except:
        print("### An exception was thrown ###\n")
        await postText(message, ERROR_EXCEPTION_MESSAGE)

CLIENT.run(BOT_TOKEN)
