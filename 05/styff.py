import requests
from itertools import permutations
import random
import os
import emoji
import json
from fake_useragent import UserAgent


lol1 = b"%E2%9C%A8"
lol2 = b"%E2%9A%A1"
lol3 = b"%F0%9F%94%91"
stuff = [lol1, lol2, lol3]
url = 'https://npst.no/api/%F0%9F%99%83.js?commands='

randnum = [i for i in range(1, 21)]

newlist = []
for x in range(10000):
    randomnum = random.choice(randnum)
    newcombo = ''
    for i in range(randomnum):
        newcombo += random.choice(stuff)
    if newcombo not in newlist:
        newlist.append(newcombo)
    else:
        pass
hash = []
print("done")
for list in newlist:
    ua = UserAgent()
    headers = {'User-Agent': str(ua.chrome)}
    with open('noughtyfile.txt', 'r') as naughty:
        for line in naughty:
            line = line.replace('\n', '')
            if list in line:
                #print("in list")
                pass
    r = requests.get(url=url+list, headers=headers)
    if "SEGFAULT" in r.text.encode('unicode-escape'):
        with open('noughtyfile.txt', 'a') as outfile:
            outfile.write(list+"\n")
        pass
    else:
        message = (r.text.encode('unicode-escape'))
        index = (message.find("message"))
        rawtext = (message[index+9:].replace("}", ''))
        if "PST" not in rawtext:
            print(rawtext)
            with open('noughtyfile.txt', 'a') as outfile:
                outfile.write(list+"\n")
        if "PST" in rawtext:
            print(rawtext, url+list)
            raise SystemExit

# https://npst.no/api/%F0%9F%99%83.js?commands=%E2%9A%A1%E2%9A%A1%E2%9C%A8%E2%9A%A1%E2%9C%A8%E2%9A%A1%E2%9C%A8%F0%9F%94%91%E2%9A%A1
# https://npst.no/api/%F0%9F%99%83.js?commands=%E2%9A%A1%E2%9A%A1%E2%9C%A8%E2%9C%A8%E2%9A%A1%E2%9A%A1%E2%9C%A8%F0%9F%94%91
# https://npst.no/api/%F0%9F%99%83.js?commands=%E2%9A%A1%E2%9A%A1%E2%9A%A1%E2%9A%A1%E2%9C%A8%F0%9F%94%91%E2%9C%A8%E2%9A%A1
# https://npst.no/api/%F0%9F%99%83.js?commands=%E2%9A%A1%E2%9C%A8%E2%9A%A1%E2%9A%A1%E2%9C%A8%E2%9A%A1%E2%9C%A8%F0%9F%94%91%E2%9A%A1
