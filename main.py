import discord
from Helper.Util import *
from Helper.Send import *
from Classes.ResponseContent import *
from Helper.InputParser import *
from Classes.ResponseContent import *
from Constant.Messages import *
from Constant.Tokens import *
from Constant.Paths import *
from Constant.Values import *
from Constant.KeyWords import *
from datetime import datetime

INTENTS = discord.Intents.all()
CLIENT = discord.Client(intents=INTENTS)

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
    exception = ""
    startTime = datetime.now()
    try:
        responses = await parseMessage(message)
    except Exception as e:
        responses = ConstantTextAction(ERROR_EXCEPTION_MESSAGE)
        exception = e
    for response in responses:
        try:
            await sendMessageReply(message, response)
        except Exception as e:
            responses = ConstantTextAction(ERROR_POST_FAILED_MESSAGE)
            exception = e
            await sendMessageReply(message, responses.pop(0))
    endTime = datetime.now()
    logAction(message, startTime, endTime, responses, exception)

def isMessageForJarvis(message):
    isAuthor = message.author == CLIENT.user
    text = message.content.lower()
    startsWithJarvis = text.startswith(JARVIS)
    return ~isAuthor & startsWithJarvis

CLIENT.run(BOT_TOKEN)
