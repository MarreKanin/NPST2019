# IV      19 16
# VII     6 20
# VII     20 23
import random


# chars = ['19', '16', '6', '20', '20', '23']

# randomListe = []

# for elemtent in range(9000):
#     newlist = []
#     random.shuffle(chars)
#     newlist = [[chars[0], chars[1]], [chars[2], chars[3]], [chars[4], chars[5]]]
#     if newlist not in randomListe:
#         randomListe.append(newlist)

# count = 0
# randomListe.sort()
# for x in randomListe:
#     for y in x:
#         print(y)
#     print(str(count)+'-------------------------')
#     count += 1
# print(len(randomListe))


char1 = ['16', '19']
char2 = ['20', '6']
char3 = ['20', '23']


newStuff = []

for x in range(2000):
    theRange = [char1, char2, char3]
    random.shuffle(theRange)
    if theRange not in newStuff:
        newStuff.append(theRange)

for x in newStuff:
    for y in x:
        print(y)
    print('--------------')
