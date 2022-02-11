import random

matches = {}

matches_num = 40
count = 10000
Matches1 = Matches2 = matches_num
for i in range(count):
    while Matches1 > 0 and Matches2 > 0:
        if random.random() > 0.5:
            Matches1 -= 1
        else:
            Matches2 -= 1
    mtch = Matches1 + Matches2
    if mtch in matches:
        matches[mtch] += 1
    else:
        matches[mtch] = 1
    
print(sorted(list(matches.items())))
for key in matches:
    print(key, matches[key]/count)


print(Matches1)
print(Matches2)
    