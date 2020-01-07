import random
import os

chars = ['`', 'V', 'p', 'N', '!', 'V', ')', ']', 'v',
         'T', 'N', '6', '6', 'X', 'U', 'y', 'J', '4', 'a', 'i', 'Q', '!']

for x in range(1000):
    password = ''
    for x in range(15):
        password += random.choice(chars)
    # os.system('./p2w')

    print(password)
