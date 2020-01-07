import os

with open('text.txt', 'r') as textfile:
    for line in textfile:
        line = line.replace('\n', '').replace(',', '')
        if line == '':
            pass
        else:
            wordlist = [i for i in line.split(' ')]
            for x in wordlist:
                with open('wordlist.txt', 'a') as outfile:
                    outfile.write(x+"\n")

            print(wordlist)
