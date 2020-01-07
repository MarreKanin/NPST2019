import requests
import os
from bs4 import BeautifulSoup


def main():

    url = 'https://kalender.npst.no/'
    spst = 'https://spst.no/'
    urlliste = []
    for x in range(1, 10):
        urlnew = url+'0'+str(x)
        urlliste.append(urlnew)
    for x in range(10, 25):
        urlnew = url+str(x)
        urlliste.append(urlnew)

    for url in urlliste:
        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'html.parser')
        getWords(bs, spst)


def getWords(bs, spst):
    taglist = []
    with open('htmltags.txt', 'r') as tags:
        for tag in tags:
            tag = tag.replace('\n', '').replace('\r', '')
            taglist.append(tag)
    wordList = []

    for tag in taglist:
        try:
            datas = bs.find_all(tag)
            for data in datas:
                for word in data.getText().split(' '):
                    word = word.replace(' ', '').replace('\t', '').replace('\n', '')
                    if word == ' ' or word == '\n' or word == '*' or word == '+' or word == '/':
                        pass
                    elif word not in wordList and len(word) < 14 and word != '' and word != ' ' and len(word) >= 2:
                        word = word.replace(':', '').replace(',', '').replace(' ', '').replace('.', '').replace('+', '').lower().strip()
                        if word[-1:] == '-' or word[0:] == '-':
                            word = word.replace('-', '')
                        if word == '':
                            pass
                        if len(word) >= 2:
                            wordList.append(word)
                            # print(word)
        except:
            pass
    total = len(wordList)
    listcount = 0
    for word in wordList:
        r = requests.get(url=spst+word)
        print(r.status_code, str(listcount) + ' av '+str(total))
        if r.status_code == 200:
            print(word)
            break
        listcount += 1


if __name__ == "__main__":
    main()
