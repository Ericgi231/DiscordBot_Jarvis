import discord

class ResponseContent:
    text=""
    file=""
    embed=""
    
    def __init__(self, text = "", file = "", embed = ""):
        self.text = text
        self.file = file
        self.embed = embed

    def setText(self, text):
        self.text = text

    def setImage(self, file):
        self.file = file

    def setText(self, embed):
        self.embed = embed