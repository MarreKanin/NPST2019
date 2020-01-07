import hashlib
import os
with open('../../Tools/xato10m.txt', 'r') as passfile:
    for line in passfile:
        line = line.replace('\n', '')
        m = hashlib.md5()
        m.update(line)
        # m.digest()
        # print(m.hexdigest())
        hash = 'bsadaebacabefeaOebcefdtetaeaeflf'
        # its more common to show hashes as a hex string
        # print(m.hexdigest())
        guesshash = m.hexdigest()
        points = 0
        for x in range(32):
            # print(x)
            if guesshash[x] == hash[x]:
                points += 1
        #print(line, guesshash, points)
        if points > 10:
            print(line, guesshash)
            # if hash == m.hexdigest():
            #     print(line, m.hexdigest())
            #     break

            # print(line)
            # 'eda58b412d6e55a2eebb5b5f731330bd'
