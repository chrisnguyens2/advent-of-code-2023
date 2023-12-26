f = open("input\\day7.txt")
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] #0 - 12
handPairs = []
fiveKind = []
fourKind = []
fullHouse = []
threeKind = []
twoPair = []
onePair = []
highCard = []

def identifyHandType(hand):
    cardCount = {}
    for c in hand:
        if cards.index(c) in cardCount:
            cardCount[cards.index(c)] += 1
        else:
            cardCount[cards.index(c)] = 1
            
    counts = list(cardCount.values())
    counts.sort(reverse=True)

    return counts

def isHand1GreaterThanHand2(hand1,hand2):
    for i in range(4):
        if hand1[i] != hand2[i]:
            if cards.index(hand1[i]) < cards.index(hand2[i]):
                return True
            else:
                return False
    return False

def sortHands(hands):
    n = len(hands)
    for i in range(n-1):
        for j in range(0, n-i-1):       
            if (isHand1GreaterThanHand2(hands[j][0], hands[j+1][0])):
                hands[j], hands[j + 1] = hands[j + 1], hands[j]

for l in f:
    hand = l.split(" ")[0]
    bid = int(l.split(" ")[1].replace("\n",""))
    handType = identifyHandType(hand)
    handPair = (hand, bid)
    
    if handType == [5]:
        fiveKind.append(handPair)
    elif handType == [4,1]:
        fourKind.append(handPair)
    elif handType == [3,2]:
        fullHouse.append(handPair)
    elif handType == [3,1,1]:
        threeKind.append(handPair)
    elif handType == [2,2,1]:
        twoPair.append(handPair)
    elif handType == [2,1,1,1]:
        onePair.append(handPair)
    elif handType == [1,1,1,1,1]:
        highCard.append(handPair)
    else:
        raise Exception("Unknown hand type: " + hand + str(handType))

sortHands(fiveKind)
sortHands(fourKind)
sortHands(fullHouse)
sortHands(threeKind)
sortHands(twoPair)
sortHands(onePair)
sortHands(highCard)

handPairs.extend(highCard)
handPairs.extend(onePair)
handPairs.extend(twoPair)
handPairs.extend(threeKind)
handPairs.extend(fullHouse)
handPairs.extend(fourKind)
handPairs.extend(fiveKind)

result = 0
for i,(h,b) in enumerate(handPairs, 1):
    result += i*b

# print(len(fiveKind) +
#         len(fourKind) +
#         len(fullHouse) +
#         len(threeKind) +
#         len(twoPair) +
#         len(onePair) +
#         len(highCard))
# print(len(handPairs))
print(fourKind)
print(handPairs[998])
# print(hands) 253911981
print(result)
f.close()