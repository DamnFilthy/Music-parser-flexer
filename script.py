import requests
from bs4 import BeautifulSoup
import json

img_url = 'https://uzhits.net'
header = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'

response = requests.get('https://uzhits.net/mp3/', headers={'User-Agent': header})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
obj = soup.findAll('div', attrs={'class': 'track-item fx-row fx-middle js-item'})

item_obj = {}
result_obj = {}

for i, item in enumerate(obj):
    item_obj['name'] = item.attrs['data-artist']
    item_obj['song_name'] = item.attrs['data-title']
    item_obj['img_link'] = img_url + item.attrs['data-img']
    item_obj['mp3_link'] = item.attrs['data-track']
    result_obj[i] = item_obj.copy()

json_res = json.dumps(result_obj)

with open("musicdata.json", "w") as file:
    file.write(json_res)
