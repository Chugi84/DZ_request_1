from pprint import pprint

import requests

import json

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url).json()
hero_1 = response[106]['powerstats']['intelligence']
hero_2 = response[236]['powerstats']['intelligence']
hero_3 = response[506]['powerstats']['intelligence']
if hero_1 < hero_2 < hero_3:
    print('Самый умный Thanos')
elif hero_1 > hero_2 > hero_3:
    print('Самый умный Hulk')
else:
    print('Самый умный Captain America')
