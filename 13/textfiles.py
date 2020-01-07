
import operator


files = ['2019-12-07.access.log', '2019-12-08.access.log',
         '2019-12-09.access.log', '2019-12-10.access.log']

data = []

for file in files:
    with open(file, 'rb') as logfile:
        for line in logfile:
            line = line.replace('\n', '')
            data.append(line)

hashes = {}
ips = {}
for line in data:
    if '/lister/slemme.php?id=gwyn' in line:
        print(line)
        break
    # print(line)
    hashindex = line.find('jw_token=')
    ipindex = line.find(' - - ')
    agentindex = line.find('"-" "')
    agent = line[agentindex+5:].replace('"', '')
    dateindex = line.find(' [')
    datecloseindex = line.find('] ')
    date = line[dateindex+2:datecloseindex]
    methodindexs = line.find('] "')
    methodindexst = line.find(' /')

    method = line[methodindexs+3:methodindexst]
    ip = line[0:ipindex]
    hash = line[hashindex+9:hashindex+41]
    if '- ' in hash:
        hash = ''
    if hash != '':
        url = line[methodindexst+1:hashindex]
    if hash == '':
        urlstart = line.find(' /')+1
        urlstop = line.find(' HTTP/1')
        #print(urlstart, urlstop)
        url = line[urlstart:urlstop]

    #print(date, url, hash, ip, agent, method)
    # with open('outfile.txt', 'a') as outfile:
    #     outfile.write(date + '\t' + url+'\t' + hash+'\t' +
    #                   ip+'\t' + agent+'\t' + method+'\n')
    if hash not in hashes and '- ' not in hash:
        hashes[hash] = 1
    if hash in hashes and '- ' not in hash:
        hashes[hash] = (hashes[hash]+1)
    if ip not in ips:
        ips[ip] = 1
    if ip in ips:
        ips[ip] = (ips[ip]+1)


hashes = sorted(hashes.items(), key=operator.itemgetter(1))
ips = sorted(ips.items(), key=operator.itemgetter(1))

for x in hashes:
    pass  # print(x)

for x in ips:
    #print(x, ips[x[1]])
    if x[1] > 10:
        pass  # print(x)

print(len(hashes))
