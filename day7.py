import re

f = open("input\\day7.txt")
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
result = 0
hands = []
rank = []

fiveKinds = []
for c in cards:
    rank.append(c+c+c+c+c)

fourKinds = []
for c in cards:
    for i in reversed(range(0, 5)):
        for cc in cards:
            if cc != c:
                fk = c+c+c+c
                start = fk[:i] 
                end = fk[i:]
                rank.append(start + cc + end)

threeKinds = []
for c in cards:

    if c == 'A':
        for i in reversed(range(0, 4)):
            for cc in cards:

                if cc != c:               
                    for j in reversed(range(i+1,5)):
                        for ccc in cards:

                            if ccc != c:
                                tk = c+c+c
                                tk = tk[:i] + cc + tk[i:]
                                rank.append(tk[:j] + ccc + tk[j:])

twoKinds = []
for c in cards:
    if c == 'A':
        for i in reversed(range(0, 3)):
            for cc in cards:
                if cc != c:               
                    for j in reversed(range(i+1,4)):
                        for ccc in cards:
                            if ccc != c:
                                for k in reversed(range(i+2,5)):
                                    for cccc in cards:
                                        if cccc != c:
                                            h = c+c
                                            h = h[:i] + cc + h[i:]
                                            h = h[:j] + ccc + h[j:]
                                            h = h[:k] + cccc + h[k:]
                                            rank.append(h)

oneKind = []
for c in cards:
    for i in reversed(range(0,2)):
        for cc in cards:
            if cc != c:               
                    for j in reversed(range(i+1,3)):
                        for ccc in cards:
                            if ccc != c:
                                for k in reversed(range(i+2,4)):
                                    for cccc in cards:
                                        if cccc != c:
                                            for x in reversed(range(i+3,5)):
                                                for ccccc in cards:
                                                    if ccccc != c:
                                                        h = c+c
                                                        h = h[:i] + cc + h[i:]
                                                        h = h[:j] + ccc + h[j:]
                                                        h = h[:k] + cccc + h[k:]
                                                        h = h[:x] + ccccc + h[x:]
                                                        rank.append(h)
                                                        
for l in f:
    hands.append((l.split(" ")[0], int(l.split(" ")[1].replace("\n","") )))

for h in hands:
    print(rank.index(h[0]))

# print(twoKinds)
# print(hands)
# print(result)
f.close()