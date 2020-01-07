import requests
import re
import random
import os
import binascii

url = '.spst.no'

# 10f37281b4e4
# 172.17.0.6
# 10.101.0.243

hex = '50696767206176210a496e67656e20626f6b737461766b6a656b732e0a4c65742069206865782070c3a52066c3b86c67656e64652072656765783a205b5c64612d6'
#hex = 'd3ce864475b318bf4d2059a52cc4c7bdc1577031454'
#hex = 'fivezerosixninesixsevensixseventwozerosixonesevensixtwoonezeroafourninesixesixsevensixfivesixetwozerosixtwosixfsixbseventhreesevenfoursixonesevensixsixbsixasixfivesixbseventhreetwoezeroafourcsixfivesevenfourtwozerosixninetwozerosixeightsixfiveseveneighttwozerosevenzerocthreeafivetwozerosixsixcthreebeightsixcsixsevensixfivesixesixfoursixfivetwozeroseventwosixfivesixsevensixfiveseveneightthreeatwozerofivebfivecsixfoursixonetwodsixsixfivedsevenbthreetwosevendfivectwoeseventhreesevenzeroseventhreesevenfourfivectwoesixesixf'
#hex = '6f7073'
#hexkeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
#rangeletters = [chr(i) for i in range(256)]
# print(rangeletters)

# hextries = []
# for x in range(20000):
#     hexer = random.choice(rangeletters)+random.choice(rangeletters)
#     if hexer not in hextries:
#         hextries.append(hexer)


# print(len(hextries))
# hextries.sort()
# errror2codes = []
# for tries in hextries:
#     try:
#         req = requests.post(url='https://'+tries+url)
#         print(req.content, tries)
#         break
#     except Exception as e:
#         print(str(e))
#         errror2codes.append([tries, e])

#         pass

# for x in errror2codes:
# print(x)

# hashez = []
# with open('../hashes.txt', 'r') as hashes:
#     for hash in hashes:
#         hash = hash.split(':')[1]
#         if len(hash) == 32 and 'LINEBREAK' not in hash:
#             hashez.append(hash)
#             #get = requests.post(url='https://'+hash+url)
#             # print(get.text)

hits = re.findall('[\da-f]{2}', hex)
hexlist = []
for x in range(200000):
    one = random.choice(hits)  # .decode('hex')
    two = random.choice(hits).decode('hex')

    data = one  # + two
    if data not in hexlist:
        hexlist.append(data)
#         # if data != ' ' or data != '\n' or data != '\t' or data != '':
#         # with open('sub.txt', 'a') as outfile:
#         #     outfile.write(data+'\n')
for start in hexlist:
    try:
        print(start+url)
        os.system('dnsrecon -d '+start+url + ' -t srv')
        # print(requests.head(url='http://'+start+url).content)
    except:
        pass
    #     length = len(hexlist)
    #     counter = 0
    #     for x in hexlist:
    #         print('https://'+x+url)
    #         try:
    #             print(x+'---------------------'+str(counter)+' av ' + str(length))
    #             get = requests.get(url='https://'+x+url)
    #             print(get.text)
    #             if get.status_code == 200:
    #                 print(x, get.text)
    #                 break
    #         except Exception as e:
    #             #print(x, get.status_code)
    #             pass
    #         counter += 1
