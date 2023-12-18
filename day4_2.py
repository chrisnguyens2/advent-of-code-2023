import math

f = open("input\\day4.txt")

cardPointDict = {}
cardOriginalCount = {}
p1 = 0

for i,line in enumerate(f):
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
        cardPointDict[i] = (countMatches, pts)

        j = i
        while j <= countMatches:
            if j in cardOriginalCount:
                cardOriginalCount[j] += 1
            else:
                cardOriginalCount[j] = 1
            j += 1

print(p1)
print(cardPointDict)
print(cardOriginalCount)

f.close()