#!/usr/bin/python
def couple(string):
    val = list(string)
    val = [''.join(val[i:i+2]) for i in range(len(val) - 1)]
    for i in range(len(val) - 1):
        if val[i] in val[i + 1:]:
            return True
    return False
def double(string):
    val = list(string)
    for i in range(len(val) - 2):
        if val[i] == val[i + 2]:
            return True
    return False

nice = list()
nice_count = 0
naughty = list()
naughty_count = 0
candidates = list()
with open('input') as f:
    candidates = f.readlines()
    candidates = [x.strip() for x in candidates]
for candidate in candidates:
    if couple(candidate) and double(candidate):
        nice.append(candidate)
        nice_count += 1
    else:
        naughty.append(candidate)
        naughty_count +=1
print 'There are ' + str(nice_count) + ' nice strings and ' + str(naughty_count) + ' naughty ones'
