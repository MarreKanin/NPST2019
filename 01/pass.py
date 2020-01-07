import random
chars = ['*', '@', '!', '#', '%', '&', '(', ')', '^', '~', '{', '}']
newchars = [ord(i) for i in chars]
nums = [i for i in range(ord('0'), ord('9')+1)]
caps = [i for i in range(ord('A'), ord('Z')+1)]
smalls = [i for i in range(ord('a'), ord('z')+1)]
passcombinations = []
for x in range(1000000):
    numbers = []
    numbers.append(random.choice(nums))
    numbers.append(random.choice(newchars))
    numbers.append(random.choice(caps))
    numbers.append(random.choice(smalls))
    summz = 0
    numbers.sort()
    for x in numbers:
        summz += int(x)
    if summz % 128 == 24:
        stringz = ''
        for x in numbers:
            stringz += chr(x)
        if stringz not in passcombinations:
            passcombinations.append(stringz)
        # print(stringz)
passcombinations.sort()
with open('passwords.txt', 'w+') as outfile:
    for x in passcombinations:
        print(x)
        outfile.write(x+'\n')
