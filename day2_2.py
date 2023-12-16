f = open("input\\day2.txt")

gamePowers = []

for i,line in enumerate(f):
    setsString = line.split(":")
    sets = setsString[1].split(";")
    minSet = {}
    
    for set in sets:
        colorCounts = set.split(",")

        for colorCount in colorCounts:
            pairArray = colorCount.lstrip().rstrip().split(" ")
            if not (pairArray[1] in minSet) or (minSet[pairArray[1]] < int(pairArray[0])):
                minSet[pairArray[1]] = int(pairArray[0])

    power = 1       
    for count in list(minSet.values()):
        power *= count
    gamePowers.append(power)

print(gamePowers)
print(sum(gamePowers))

f.close()