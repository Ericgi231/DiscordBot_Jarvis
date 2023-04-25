import discord
import random
from Helper.Util import *
from Helper.InputParser import *
from Constant.Messages import *
from Constant.Tokens import *
from Constant.Paths import *
from Constant.Values import *
from Constant.KeyWords import *
from Actions.CringeAction import *
from Actions.DateTimeAction import *
from Actions.GoogleAction import *
from Actions.HelloAction import *
from Actions.HelpAction import *
from Actions.MagicEightBallAction import *
from Actions.ManPageAction import *
from Actions.PostMemeAction import *
from Actions.PostPornAction import *
from Actions.PostStockImageAction import *
from Actions.RandomFailureAction import *
from Actions.RandomNumberAction import *
from Actions.WikiAction import *
from Actions.InjectedTextAction import *
from Actions.RandomWordsAction import *
from Actions.ConstantTextAction import *
from Actions.FarmAction import *

async def parseMessage(message):
    #Early exits
    if isRandomFailure():
        return randomFailureAction()
    if hasInjectText():
        return injectedTextAction()
    
    #Trim Jarvis
    text = message.content.lower()
    text = trimFirstWord(text)

    try:
        text = trimFillerIfPresent(text, PLEASE)
        if text.startswith(HELP):
            return helpAction()
        elif text.startswith(tuple(HELLO)):
            return helloAction()
        elif text.startswith(CANCEL):
            emojiList = await message.guild.fetch_emojis()
            return farmAction(emojiList)
        elif text.startswith(THANK):
            return cringeAction()
        elif text.startswith(WHEN):
            return dateTimeAction()
        elif text.startswith(tuple(WILL)):
            return magicEightBallAction()
        elif text.startswith(tuple(MANY)):
            return randomNumberAction()
        elif text.startswith(GOOGLE):
            return googleAction(trimFirstWord(text))
        elif text.startswith(WIKI):
            return wikiAction(trimFirstWord(text))
        elif text.startswith(MAN):
            return manPageAction(trimFirstWord(text))
        elif text.startswith(tuple(SHOW)):
            return parsePostMessage(trimFirstWord(text))
        else:
            return randomWordsAction()
    except Exception as e:
        raise e

def parsePostMessage(text):
    try:
        if text == "":
            return ConstantTextAction(ERROR_INVALID_USE_MESSAGE)
        text = trimFillerIfPresent(text, ME)
        if text == "":
            return ConstantTextAction(ERROR_INVALID_USE_MESSAGE)
        keyword = text.split()[-1]
        count = 1
        if text.split()[0].isnumeric():
            count = int(text.split()[0])
            text = trimFirstWord(text)
        elif isAlphaToNumeric(text.split()[0]):
            count = alphaToNumeric(text.split()[0])
            text = trimFirstWord(text)
        if count > POST_LIMIT:
            return ConstantTextAction(ERROR_OVER_LIMIT_MESSAGE)

        if keyword.startswith(tuple(MEME)):
            return postMemeAction(count, trimLastWord(text))
        elif keyword.startswith(tuple(PORN)):
            return postPornAction(count, trimLastWord(text))
        else:
            return postStockImageAction(text)
    except Exception as e:
        raise e