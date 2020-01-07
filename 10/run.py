import os
import re

datastring = ''
with open('bestmove.txt', 'rb') as movefile:
    for line in movefile:
        data = re.findall("Best move was ......", line)
        for x in data:
            datastring += (x.replace('Best move was', '').replace(
                '}', '').replace(' ', '').replace('.', ''))

print(datastring)

white = ''
black = ''
both = ''
with open('moves.txt', 'rb') as moves:
    for line in moves:
        line = line.replace('\n', '').replace('\r', '')
        #print("LINE: "+line)
        try:
            print(line.split(' ')[1])
            print(line.split(' ')[2])
            white += line.split(' ')[1]
            black += line.split(' ')[2]
            both += line.split(' ')[1] + line.split(' ')[2]
        except:
            pass


print(white)
print(black)
print(both)
