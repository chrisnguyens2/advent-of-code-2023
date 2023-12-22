import re

f = open("input\\day7.txt")
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
result = 0
hands = []

fiveKinds = []
for c in cards:
    fiveKinds.append(c+c+c+c+c)

fourKinds = []
for c in cards:
    for i in range(0, 4):
        for cc in cards:
            if cc != c:
                fk = c+c+c+c
                fourKinds.append(fk[:i] + cc + fk[i:])

threeKinds = []
for c in cards:
    for i in range(0, 4):
        for cc in cards:
            tk = c+c+c
            fourKinds.append(fk[:i] + cc + fk[i:])

for l in f:
    hands.append((l.split(" ")[0], int(l.split(" ")[1].replace("\n","") )))

for h in hands:
    print(re.findall("QQQ",h[0]))

print(hands)
print(result)
f.close()