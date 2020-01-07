import os
import operator


x = os.listdir('./files')

# print(x)

nisseliste = {}
for y in x:

    # print(os.stat("./files/"+y)[6])
    if os.stat("./files/"+y)[6] not in nisseliste:
        nisseliste.update({os.stat("./files/"+y)[6]: 1})
    if os.stat("./files/"+y)[6] in nisseliste:
        nisseliste[os.stat("./files/"+y)[6]] += +1
    if 3235 == os.stat("./files/"+y)[6]:
        print(y)
    if 1567 == os.stat("./files/"+y)[6]:
        print(y)
# print(nisseliste

thenewlist = sorted(nisseliste.items(), key=operator.itemgetter(1))
# print(thenewlist)
for key, value in thenewlist:
    print(key, value)
# print(os.stat("./files/"+y)[0], os.stat("./files/"+y)[1])
