f = open("input\day2.txt")

games = []

for line in f:
    setsString = line.split(":")
    sets = setsString[1].split(";")
    setArray = []
    games.append(setArray)

    for set in sets:
        colorCounts = set.split(",")
        countDict = {}            
        setArray.append(countDict)

        for colorCount in colorCounts:
            pairArray = colorCount.lstrip().rstrip().split(" ")
            countDict[pairArray[1]] = int(pairArray[0])

#print(games)

bag = {"red": 12, "green": 13, "blue": 14}
validGames = []

for i in range(len(games)):
    validGame = True

    for set in games[i]:
        for color, count in set.items():
            if set[color] <= bag[color]:
                validGame = True
            else:
                validGame = False
                break
        
        if validGame == False:
            break

    if validGame:
        validGames.append(i + 1)

print(validGames)
print(sum(validGames))

f.close()