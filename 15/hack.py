import requests
import os
import time

url = ''

with open('../../Tools/rockyou.txt', 'rb') as passfile:
    for passwd in passfile:
        passwd = passwd.replace('\n', '')
        os.system('7za x "./feriebilder.zip" -oOPT -p' +
                  passwd + " > /dev/null 2>&1")
        files = os.listdir('./OPT/')
        # print(passwd)
        time.sleep(0.001)
        count = 0
        for x in files:
            size = os.path.getsize("./OPT/"+x)
            # print(size)
            if size < 200:
                count += 1
        if count == 3:
            os.system("rm -rf ./OPT/")
        else:
            print(passwd)
            break

        #print('7z x ./files/logger.7z.001 -p'+passwd)
