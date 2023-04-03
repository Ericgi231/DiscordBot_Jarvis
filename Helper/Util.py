import random
import discord
from Constant.Messages import DATE_TIME_MESSAGE_FORMAT
from Constant.KeyWords import *
from datetime import datetime
from Constant.Messages import *
from Constant.Values import *
from Classes.ResponseContent import *

def isAlphaToNumeric(word):
    if word == "a" or word == "an":
        return True
    elif word == "one":
        return True
    elif word == "two":
        return True
    elif word == "three":
        return True
    elif word == "four":
        return True
    elif word == "five":
        return True
    elif word == "six":
        return True
    elif word == "seven":
        return True
    elif word == "eight":
        return True
    elif word == "nine":
        return True
    elif word == "ten":
        return True
    else:
        return False

def alphaToNumeric(word):
    if word == "a" or word == "an":
        return 1
    elif word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9
    elif word == "ten":
        return 10
    else:
        return 1

def getRandomDateTimeString():
    num = random.randint(0, 11)
    if num == 0:
        month = "Jan"
    elif num == 1:
        month = "Feb"
    elif num == 2:
        month = "Mar"
    elif num == 3:
        month = "Apr"
    elif num == 4:
        month = "May"
    elif num == 5:
        month = "Jun"
    elif num == 6:
        month = "Jul"
    elif num == 7:
        month = "Aug"
    elif num == 8:
        month = "Sep"
    elif num == 9:
        month = "Oct"
    elif num == 10:
        month = "Nov"
    elif num == 11:
        month = "Dec"
    day = random.randint(1,31)
    if day == 1 or day == 21 or day == 31:
        day = str(day)+"st"
    elif day == 2 or day == 22:
        day = str(day)+"nd"
    elif day == 3 or day == 23:
        day = str(day)+"rd"
    else:
        day = str(day)+"th"
    hour = random.randint(1,12)
    minutes = random.randint(0,59)
    if random.randint(0,1):
        period = "am"
    else:
        period = "pm"
    return DATE_TIME_MESSAGE_FORMAT.format(month, day, hour, minutes, period)

def getRandomWords():
    response = ""
    for x in range(random.randint(1,3)):
        response += random.choice(list(open('Data/Words.txt'))).strip() + " "
    return response

def trimFillerIfPresent(text, word):
    if text == "":
        return text
    if text.split()[0] == word:
        text = trimFirstWord(text)
    if text == "":
        return text
    if text.split()[-1] == word:
        text = trimLastWord(text)
    return text

def trimFirstWord(text):
    if text == "" or len(text.split()) == 1:
        return ""
    else:
        return text.split(' ', 1)[1]

def trimLastWord(text):
    if len(text.rsplit()) == 1:
        return ""
    else:
        return text.rsplit(' ', 1)[0]

def logAction(message, startTime, endTime, responses, exception):
    log = "### {} - {} ###\n".format(message.author, message.content)
    for content in responses:
        if content.embed:
            log += "Embed: {}\n".format(content.embed.url)
        if content.file:
            log += "File: {}\n".format(content.file.filename)
        if content.text:
            log += "Text: {}\n".format(content.text)
        if exception:
            log += "Exception: {}\n".format(exception)
    log += "StartTime: {}\n".format(startTime)
    log += "EndTime: {}\n".format(endTime)
    log += "RunTime: {}\n".format(endTime-startTime)
    log += "### {} - {} ###\n".format(message.author, message.content)
    print(log)

def hasInjectText():
    with open('Data/Inject.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    return len(data) > 0

def isRandomFailure():
    return random.randint(0,FAIL_CHANCE) == 0