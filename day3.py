f = open("input\\day3.txt")
nums = []
schematic = []

for line in f:
    schematic.append(line.replace('\n', ""))

numLocs = []
symbolLocs = []
for row,line in enumerate(schematic):
    num = 0
    locs = set()
    for col,c in enumerate(line):
        if c.isdigit():
            num = num*10+int(c)
            locs.add((row, col - 1))
            locs.add((row, col + 1))
            locs.add((row - 1, col + 1))
            locs.add((row - 1, col ))
            locs.add((row - 1, col - 1))
            locs.add((row + 1, col + 1))
            locs.add((row + 1, col ))
            locs.add((row + 1, col - 1))
        else:
            if num > 0:
                numLocs.append((num, locs))
                num = 0
                locs = set()
            if (not c.isdigit()) and c != ".":
                symbolLocs.append((c, (row, col)))        

for num,nlocs in numLocs:
    isPart = False
    for nloc in nlocs:        
        for s,sloc in symbolLocs:
            if nloc == sloc:
                #numLocs.remove((num,nlocs))
                nums.append((num))
                isPart = True
                break
        if isPart == True:
            isPart = False
            break


#print(schematic)
#print(numLocs)
#print(symbolLocs)
#print(nums)

sum = 0
for num in nums:
    sum += num

# print(nums)
print(sum)
f.close()