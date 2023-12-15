f = open(".\input\day1_input.txt")

def replaceFirstStringNum(line: str):
    numDict = {"one": 1
               , "two" : 2
               , "three" : 3
               , "four" : 4
               , "five" : 5
               , "six" : 6
               , "seven" : 7
               , "eight" : 8
               , "nine" : 9}
    
    numCleanUpDict = {"oneight" : "oneeight"
                      , "twone": "twoone"
                      , "threeight": "threeeight"
                      , "fiveight": "fiveeight"
                      , "sevenine": "sevennine"
                      , "eightwo": "eighttwo"
                      , "eighthree": "eightthree"
                      , "nineight": "nineeight"}

    for key,value in numCleanUpDict.items():
        line = line.replace(key, value)
    
    for key,value in numDict.items():
        line = line.replace(key, str(value))

    return line

def getResultFromLine(l):
    filteredString = ''.join(c for c in l if c.isdigit())
    lineNum = filteredString[0] + filteredString[-1]
    return int(lineNum)

result = 0

for line in f:
    updatedLine = replaceFirstStringNum(line)
    result += getResultFromLine(updatedLine)

print(result)
f.close()