import random
from Classes.ResponseContent import *
from Constant.Messages import *

def injectedTextAction():
    with open('data/inject.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    text = data[0]
    with open('data/inject.txt', 'w') as fout:
        fout.writelines(data[1:])
    return [ResponseContent(text=text)]