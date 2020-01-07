import requests
import os

url = ''

with open('wordlist.txt', 'rb') as passfile:
    for passwd in passfile:
        passwd = passwd.replace('\n', '')
        os.system('7z e "./files/logger.7z.001" -oOPT -p'+passwd)

        print('7z a ./files/logger.7z.001 -p'+passwd)
