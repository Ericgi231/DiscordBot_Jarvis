import random
from Classes.ResponseContent import *
from Constant.Messages import *
from Helper.Util import *
from Constant.Paths import *

def cringeAction():
    with open(COLLECTION_PATH + OH_NO_CRINGE_FILE, 'rb') as f:
        pic = discord.File(f,OH_NO_CRINGE_FILE)
    return [ResponseContent(file=pic)]