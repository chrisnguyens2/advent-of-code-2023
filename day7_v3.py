from functools import cmp_to_key
import functools

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

def compare(hand1,hand2):
    for i in range(4):
        if hand1[0][i] != hand2[0][i]:
            return  - cards.index(hand2[0][i]) - cards.index(hand1[0][i])
    return 0

compare_key = cmp_to_key(compare)

# def sortHands(hands):
#     n = len(hands)
#     for i in range(n-1):
#         for j in range(0, n-i-1):       
#             if (isHand1GreaterThanHand2(hands[j][0], hands[j+1][0])):
#                 hands[j], hands[j + 1] = hands[j + 1], hands[j]

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

fiveKind.sort(key=functools.cmp_to_key(compare))
fourKind.sort(key=functools.cmp_to_key(compare))
fullHouse.sort(key=functools.cmp_to_key(compare))
threeKind.sort(key=functools.cmp_to_key(compare))
twoPair.sort(key=functools.cmp_to_key(compare))
onePair.sort(key=functools.cmp_to_key(compare))
highCard.sort(key=functools.cmp_to_key(compare))

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
# print(fourKind)
# 253911981 253218030
# 253910319
print(result)
f.close()