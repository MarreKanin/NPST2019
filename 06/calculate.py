# -*- coding: iso-8859-1
firsttask = 'KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo'.decode(
    'utf-8')
task = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1038åa5a fmw55k8m7i179 95p11'.decode(
    'utf-8')
tast = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'.decode(
    'utf-8')


print(firsttask + ' <- First Cipher')
print(task + ' <- Original Cipher WRONG')
print(tast + ' <- Original Cipher')


# print(letters)

with open('decoded.txt', 'r') as infile:
    for line in infile:
        line = line.replace('\n', '')
        newline = ''
        #linz = 'PST krø55p8r7n179 b98daeb8ca67fea0e6c7fd1e1038ef5f krø55p8r7n179 95u11'
        #line = 'PST krø55p8r7n179 b98daeb8ca67fea0e6c7fd1e1438ef5f krø55p8r7n179 95u11'

        print(line.decode('utf-8') + ' <- Etter ceasar shift')
        for x in line:
            x = '@' if x == '5' else x
            x = '4' if x == '8' else x
            x = '3' if x == '7' else x
            x = '7' if x == '1' else x
            x = '5' if x == '9' else x
            x = '1' if x == '@' else x

            newline += x
    print(newline.decode('utf-8') + ' <- Første replacment'.decode('utf-8'))
newnewline = ''
for x in newline.decode('utf-8'):
    x = 'l' if x == '1' else x
    x = 'a' if x == '4' else x
    x = 'e' if x == '3' else x
    x = 't' if x == '7' else x
    x = 's' if x == '5' else x
    x = 'O' if x == '0' else x
    x = 'Z' if x == '2' else x
    x = 'b' if x == '6' else x
    x = 'b' if x == '8' else x
    x = 'g' if x == '9' else x

# 0 = O or D or space
# 1 = I or L
# 2 = Z or e
# 3 = E or R
# 4 = h or A
# 5 = S
# 6 = b or G
# 7 = T or j
# 8 = B or X
# 9 = g or J

    newnewline += x


print(newnewline + ' <- Resultat men FEIL')


letters = [i for i in range(ord("a"), ord("z"))]
letters.append(ord('æ'.decode('utf-8')))
letters.append(ord('ø'.decode('utf-8')))
letters.append(ord('å'.decode('utf-8')))
for i in range(0, 10):
    letters.append(ord(chr(i)))

# for letternumber in letters:
#     newciphershift = ''
#     for letter in task:
#         print(letternumber)
