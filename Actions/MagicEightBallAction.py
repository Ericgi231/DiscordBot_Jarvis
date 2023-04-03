import random
from Classes.ResponseContent import *
from Constant.Messages import *

def magicEightBallAction():
    return [ResponseContent(text=random.choice(MAGIC_EIGHT_BALL_MESSAGES))]