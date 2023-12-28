F = open("input\\day9.txt").read().strip()
I = F.split('\n')
ans = 0
history = []
history2 = []

for l in I:
    G = [[int(x) for x in l.split(" ")]]
    nextSeq = []

    while not (len(set(nextSeq)) == 1):
        nextSeq = []
        for i, num in enumerate(G[len(G) - 1]):
            if i != len(G[len(G) - 1]) - 1:
                nextSeq.append(G[len(G) - 1][i+1] - num)
        G.append(nextSeq) 

    historyValue = 0
    for i in reversed(range(len(G))):
       historyValue += G[i - 1][-1]
    history.append(historyValue)

    historyValue2 = G[len(G) - 1][0]
    for i in reversed(range(1,len(G))):
        historyValue2 = G[i - 1][0] - historyValue2
    history2.append(historyValue2)

print(sum(history))
print(sum(history2))
