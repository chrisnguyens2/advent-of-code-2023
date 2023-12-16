f = open("input\\day2.txt")

bag = {"red": 12, "green": 13, "blue": 14}
validGames = []

for i,line in enumerate(f):
    setsString = line.split(":")
    sets = setsString[1].split(";")
    validGame = True
    
    for set in sets:
        colorCounts = set.split(",")

        for colorCount in colorCounts:
            pairArray = colorCount.lstrip().rstrip().split(" ")
            if int(pairArray[0]) <= bag[pairArray[1]]:
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