import random
from Classes.ResponseContent import *
from Constant.Values import *

#https://www.unicode.org/Public/draft/emoji/
#https://www.fileformat.info/info/emoji/list.htm

def farmAction(emojiList):
    #emoji = discord.PartialEmoji.from_str(":passport_control:")
    emoji = random.choice(emojiList)
    emojiName = emoji.name
    emojiFarm = " ".join([str(emoji)]*random.randint(MIN_ANTS,MAX_ANTS))
    textOut = "THREAD CANCELED!!!!!!!!!!!!! " + emojiName + " FARM GOOOO " + emojiFarm
    return [ResponseContent(text=textOut)]