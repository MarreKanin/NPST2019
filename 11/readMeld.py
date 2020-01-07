# -*- coding: utf-8 -*-
import os
from textwrap import wrap

with open('melding.txt', 'rb') as binfile:
    count = 0
    cipher = ''
    for x in binfile:
        x = x.replace('\n', '')
        cipher += x
        number = x
        data = (wrap(x, 10))
        fullString = x.replace('0', ' ')
        #fullString = fullString.replace('1', '█')

counter = 0
stringer = ''

# primes factorization of 1337 = 191 * 7
with open('outfile.txt', 'a') as outfile:
    for x in fullString:
        stringer += x
        counter += 1
        if counter == 191:
            stringer += '\n'
            counter = 0
    print(stringer)
    outfile.write(stringer)
