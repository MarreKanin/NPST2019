import os
from bs4 import BeautifulSoup
import binascii
words = []
# with open('pingu.txt') as pingutext:
#     for line in pingutext:
#         line = line.replace('\n', '')
#         line = line.split(' ')
#         for lin in line:
#             if lin != '':
#                 words.append(lin)
# print(words)
# cipher = []
# with open('cipher.txt', 'r') as cipherfile:
#     for line in cipherfile:
#         line = line.replace('\n', '').replace(' ', '')
#         lines = line.split(';')
#         # print(lines)
#         for x in lines:
#             if x.startswith('&#'):
#                 print(x)

with open('testical.html', 'r') as cipherfile:
    for line in cipherfile:
        line = line.replace('\n', '').replace('\r', '')
        line = line.split(';')
        for lin in line:
            lin = lin+';'
            if lin != ';':
                words.append(lin)

cipher = ''
cipher2 = ''
datacipher = []
htmlchars = []
for x in words:
    htmlchars.append(x)
    char = str(BeautifulSoup(x, 'html.parser'))
    if x == '&zwj;':
        x = u"\u200D"
    if x == '&zwnj;':
        x = u"\u200C"
    if x == '&#8236;':
        x = u"\u8236"
    if x == '&#65279;':
        x = u"\U00065279"
    cipher2 += x
    cipher += char

    # print(html.unescape(x))
    # print(x)

# &zwj; = u"\u200D"
# &zwnj; = u"\u200C"
# &#8236; = u"\u8236"
# &#65279; = u"\U00065279"
print(htmlchars)
# &zwj; = zero-width joiner 200D
# &zwnj; = zero-width non-joiner 200C
# &#8236; = POP DIRECTIONAL FORMATTING  8236
# &#65279; = not a char FEFF


# lengths = []
# for x in range(1, 888):
#     lengths.append(x)

# print(cipher)
# print(lengths)

# for length in lengths:
#     newcipher = ''
#     lengthcounter = 0
#     for char in cipher:
#         if lengthcounter+1 == length:
#             newcipher += char+'\n'
#         else:
#             newcipher += char
#         lengthcounter += 1
#     print(newcipher)
