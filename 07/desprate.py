import random

a = '04ec672b'

b = '2c3ecc69'

c = '5416b9d9ff1775fe'

list = [a, b, c]

stuff = []
for x in range(220):
    the_hash = random.choice(list) + random.choice(list)+random.choice(list)
    if "PST{"+the_hash+"}" not in stuff and len(the_hash) == 32:
        stuff.append(("PST{"+the_hash+"}"))
count = 0
for x in stuff:
    print(str(count) + " " + x)
    count += 1
