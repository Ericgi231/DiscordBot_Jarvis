import random
from Classes.ResponseContent import *
from Constant.Messages import *

def randomFailureAction():
    return [ResponseContent(text=random.choice(NEGATIVE_MESSAGES))]