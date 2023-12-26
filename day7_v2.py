f = open("input\\day7.txt")
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] #0 - 12
handPairs = []


def identifyHandType(hand):
    cardCount = {}
    for card in cards:
        for c in hand:
            if card == c:
                if cards.index(c) in cardCount:
                    cardCount[cards.index(c)] += 1
                else:
                    cardCount[cards.index(c)] = 1
    
    highestCard = [12, 1] #cardIndex, cardCount

    for cc in cardCount:
        if cardCount[cc] > highestCard[1] or (cardCount[cc] == highestCard[1] and cc < highestCard[0]):
            highestCard[0] = cc
            highestCard[1] = cardCount[cc]

    return highestCard

def compareNonMatches(hand1,hand2):
    for i in range(4):
        if hand1[i] != hand2[i]:
            if cards.index(hand1[i]) > cards.index(hand2[i]):
                return True
            else:
                return False
    return False

for l in f:
    hand = l.split(" ")[0]
    bid = int(l.split(" ")[1].replace("\n",""))
    handType = identifyHandType(hand)

    handPairs.append((hand, bid, handType))

result = 0
n = len(handPairs)

for i in range(n-1):
    for j in range(0, n-i-1):
        count1 = handPairs[j][2][1]
        count2 = handPairs[j+1][2][1]
        if (count1 < count2
            or (count1 == count2 and handPairs[j][2][0] > handPairs[j+1][2][0])):
                handPairs[j], handPairs[j + 1] = handPairs[j + 1], handPairs[j]

for i in range(n-1):
    for j in range(0, n-i-1):
        if handPairs[j][2] == handPairs[j+1][2] and compareNonMatches(handPairs[j][0], handPairs[j+1][0]):
                handPairs[j], handPairs[j + 1] = handPairs[j + 1], handPairs[j]

for i,handPair in enumerate(handPairs):
    result += (i+1)*handPair[1]

print(handPairs[999])
# print(hands) 248114233
print(result)
f.close()