import random
from Classes.ResponseContent import *
from Constant.Values import *

def randomNumberAction():
    num = random.randint(-MAX_RANDOM_NUMBER,MAX_RANDOM_NUMBER)
    return [ResponseContent(text=num)]