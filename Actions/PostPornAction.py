import random
import requests
from Classes.ResponseContent import *
from Constant.Messages import *
from Constant.Tokens import *
import xmltodict

def postPornAction(count, tags):
    responses = []
    for n in range(count):
        r34url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"
        if tags != "":
            tags = tags.replace(' ','+')
            r34url += "&tags=" + tags
        else:
            r34url += "&tags=*"
        pre_data = requests.get(r34url+"&limit=0")
        pre_xml = xmltodict.parse(pre_data.content)
        total = int(pre_xml["posts"]["@count"])
        url = ""
        if total > 0:
            if total > 2000:
                total = random.randint(0,2000)
            pid = random.randint(0,int(total/100))
            r34url += "&pid=" + str(pid)
            data = requests.get(r34url)
            xml = xmltodict.parse(data.content)
            if total == 1:
                url = xml["posts"]["post"]["@file_url"]
            else:
                total_img = len(xml["posts"]["post"])
                num = random.randint(0,total_img-1)
                url = xml["posts"]["post"][num]["@file_url"]

        if url != "":
            responses.append(ResponseContent(text=url))
        else:
            if len(tags.split()) > 1:
                responses.append(ResponseContent(text="No porn found with tags `"+ tags.replace(' ','`, `') + "`"))
            else:
                responses.append(ResponseContent(text="No porn found with tag `" + tags + "`"))
            
    return responses