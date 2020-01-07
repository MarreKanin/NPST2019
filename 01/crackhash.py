import hashlib
import os
with open('passwords.txt', 'r') as passfile:
    for line in passfile:
        line = line.replace('\n', '')
        m = hashlib.sha1(line.encode('utf-8')).hexdigest()
        # m.update(line)
        hash = '42f82ae6e57626768c5f525f03085decfdc5c6fe'
        #print(hash, m, line)
        if hash == m:
            #print(line, m.hexdigest())
            print("Found match:")
            print(m, line)
            break

            # print(line)
            # 'eda58b412d6e55a2eebb5b5f731330bd'
