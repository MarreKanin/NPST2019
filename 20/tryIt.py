import requests
import json
import hashlib


def main():
    s = requests.Session()
    cookies = dict(session='d47b77ab-9c8b-47a9-817e-5dbeae5e334e', __cfduid='d46f52fdb5684e5fa2380fd5b62be50f31576923023')
    url = 'https://intranett.npst.no/api/v1/challenges/attempt'
    # string = '''&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'=".<(+|!$*); ,%_>?'''
    x = '&'
    line = 'IBM 029+IBM1'+x+'60'
    m = hashlib.md5(line.encode('utf-8')).hexdigest()
    data = {"challenge_id": 26, "submission": "PST{" + m + "}"}

    response = s.post(url=url, cookies=cookies, data=data)

    print(response.text, response.status_code)


if __name__ == "__main__":
    main()
