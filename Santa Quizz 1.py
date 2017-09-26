#!/usr/bin/python
def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in list(string):
        if i in vowels:
            count += 1
    return True if count >= 3 else False
def double(string):
    val = list(string)
    for i in range(len(val) - 1):
        if val[i] == val[i + 1]:
            return True
    return False
def banned(string):
    val = list(string)
    bad_couples = {'a' : 'b', 'c' : 'd', 'p' : 'q', 'x' : 'y'} 
    for i in range(len(val) - 1):
        if val[i] in bad_couples.keys() and val[i + 1] == bad_couples[val[i]]:
            return False
    return True

nice = list()
nice_count = 0
naughty = list()
naughty_count = 0
candidates = list()
with open('input') as f:
    candidates = f.readlines()
    candidates = [x.strip() for x in candidates]
for candidate in candidates:
    if vowels(candidate) and double(candidate) and banned(candidate):
        nice.append(candidate)
        nice_count += 1
    else:
        naughty.append(candidate)
        naughty_count +=1
print 'There are ' + str(nice_count) + ' nice strings and ' + str(naughty_count) + ' naughty ones'
