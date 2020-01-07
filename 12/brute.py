import requests


url = '''https://api.spst.no/eval?eval=decrypt(%22passord-'''
url2 = '''1%22,%22NaHSO4%22,%22e5a8aadb885cd0db6c98140745daa3acf2d06edc17b08f1aff6daaca93017db9dc8d7ce7579214a92ca103129d0efcdd%22)'''

for x in range(0, 100):
    r = requests.get(url=url+str(x)+url2)
    print(r.text, x)


# PST{24e592de8b20fe09938916d79b08854e}
# https://api.spst.no/eval?eval=decrypt(%22passord-61%22,%22NaHSO4%22,%22e5a8aadb885cd0db6c98140745daa3acf2d06edc17b08f1aff6daaca93017db9dc8d7ce7579214a92ca103129d0efcdd%22)
