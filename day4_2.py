import math

f = open("input\\day4.txt")

cards = []

cardCount = {}
p1 = 0
p2 = 0

for i,line in enumerate(f,1):
    cardCount[i] = 1
    cards.append(line.replace('\n', ""))

numCards = len(cards)

for i,line in enumerate(cards,1):
    card = line.replace('\n', "").split(":")
    nums = card[1].split("|")
    winningNums = set(nums[0].strip().split(" "))
    myNums = set(nums[1].strip().split(" "))

    countMatches = 0
    for wNum in winningNums:
        for myNum in myNums:
            if wNum != '' and myNum != '' and wNum == myNum:
                countMatches += 1
    
    if countMatches > 0:
        pts = int(math.pow(2,countMatches - 1))
        p1 += pts

        j = i
        k = 1
        while j < i + countMatches:           
            cardCount[i + k] += cardCount[i]
            p2 += cardCount[i]
            j += 1
            k += 1

print(p1)
print(p2 + numCards)
f.close()