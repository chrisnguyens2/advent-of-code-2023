f = open("input\\day3.txt")
gears = {}
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

            if col == len(schematic[0]) - 1:
                numLocs.append((num, locs))
                num = 0
                locs = set()
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
                if s == "*":
                    if sloc in gears:
                        gears[sloc].append(num)
                    else:
                        gears[sloc] = [num]
                nums.append((num))
                isPart = True
                break
        if isPart == True:
            isPart = False
            break

sum = 0
for num in nums:
    sum += num

sumGearRatios = 0
for nums in gears.values():
    if len(nums) == 2:
        sumGearRatios += nums[0]*nums[1]

print(sum)
print(sumGearRatios)
f.close()