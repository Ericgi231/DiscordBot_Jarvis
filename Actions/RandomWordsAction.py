import random
from Classes.ResponseContent import *
from Constant.Messages import *
from Helper.Util import *

def randomWordsAction():
    return [ResponseContent(text=getRandomWords())]