# -*- coding: utf-8 -*-
import random
from itertools import permutations

# løsningen er å ceasarshifte først med alfabet, så med tall - i 2 runder.
encoded = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'.decode(
    'utf-8')
decoded = 'PST krø55p8r7n179 b98daeb8ca67fea0e6c7fd1e1438ef5f krø55p8r7n179 95u11'.decode(
    'utf-8')
print(encoded)
newencode = ''
print(decoded)

for bokstav in decoded:

    if bokstav == '8':
        bokstav = '4'
    if bokstav == '7':
        bokstav = '3'
    if bokstav == '9':
        bokstav = '@'
    if bokstav == '1':
        bokstav = '7'
    if bokstav == '5':
        bokstav = '1'
    if bokstav == '@':
        bokstav = '5'
    newencode += bokstav
print(newencode)

result = ''
for bokstav in newencode:

    if bokstav == '4':
        bokstav = 'a'
    if bokstav == '3':
        bokstav = 'e'
    if bokstav == '1':
        bokstav = 'l'
    if bokstav == '5':
        bokstav = 's'
    if bokstav == '7':
        bokstav = 't'
    result += bokstav

print(result)

# 13457
# least

# z = '1'
# x = '3'
# c = '4'
# v = '5'
# b = '7'
# n = 'l'
# m = 'e'
# w = 'a'
# e = 's'
# r = 't'
# lol2 = [z, x, c, v, b]
# lol = [n, m, w, e, r]
# tries = []
# for x in range(10000):
#     string = ''
#     stuff = random.choice(lol)+random.choice(lol)+random.choice(lol)+random.choice(lol)+random.choice(
#         lol)+random.choice(lol)+random.choice(lol)+random.choice(lol)+random.choice(lol)+random.choice(lol)
#     stufforder = ''
#     post = None
#     for x in stuff:
#         if x not in stufforder:
#             post = True
#         # if x in stufforder:
#         #     post = False
#         if stufforder.find(x) == -1:
#             post = False
#         stufforder += x
#     if post == False:
#         pass
#     if post == True:
#         tries.append(stuff)


# perm = permutations(lol)

# lists = []
# for x in perm:
#     thing = ''
#     for y in x:
#         thing += y
#     print(thing)
