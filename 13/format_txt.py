import os

list = []
with open('pass.txt', 'r') as textfile:
    for line in textfile:
        line = line.replace('\n', '').replace(',', '').replace('\r', '  ')
        if line == '':
            pass
        else:
            wordlist = [i for i in line.split(' ')]
            for x in wordlist:
                if x == '':
                    pass
                else:
                    with open('wordlist.txt', 'a') as outfile:
                        outfile.write(x+"\n")

            print(wordlist)
