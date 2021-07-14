import requests
import re
import json
import time

pattern = 'data-track="\w{1,}:\/\/\w{1,}.\w{1,}\/\w{1,}\/\w{1,}\/\d{1,}?-\d{1,}\/\w{1,}?-\w{1,}?-\w{1,}?-\w{1,}?-?_[(]\w{1,}?.\w{1,}[)]?.\w{1,}?"'

url = 'https://uzhits.net/mp3/'
headers={'User-Agent': 'Mozilla/5.0'}

def getSongs():
    session = requests.Session()
    response = session.get(url, headers=headers)
    text = response.content.decode()
    result = re.findall(pattern, text)

    toJson = {}
    for i, item in enumerate(result):
        toJson[i] = item
        

    resJson = json.dumps(toJson)

    with open("musicdata.json", "w") as file:
        file.write(resJson)

       
getSongs()