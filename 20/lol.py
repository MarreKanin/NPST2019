import requests
import os
import hashlib


def main():
    sendt_hashes = []
    with open('tried.txt', 'r') as hashes:

        for line in hashes:
            line = line.replace('\n', '')
            line = line.split(':')[0]
            sendt_hashes.append(line)
    string = '''&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@ =".<(+|!$*),%_>?'''
    # string = ''
    # for y in range(9):
    #     string += str(y)
    for x in string:
        status = "False"

        line = 'IBM 029+IBM196'+x
        m = hashlib.md5(line.encode('utf-8')).hexdigest()
        for x in sendt_hashes:
            if m == x:
                status = "True"
                break
        if status == "True":
            pass
        else:
            print(m, line, status)
    # with open('codes.txt', 'r') as codes:
    #     for code in codes:
    #         code = code.replace('\n', '')
    #         c1, c2 = code[0:2], code[2:4]
    #         decode = int(c1) + int(c2)
    #         decode2 = hex(int(decode))

    #         print(code, hex(int(code)), hex(int(decode)), decode2)


if __name__ == "__main__":
    main()
