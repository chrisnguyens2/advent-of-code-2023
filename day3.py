f = open("input\\day3.txt")
nums = []
schematic = []

def checkCharacter(c, nums, num):
    if (not c.isdigit()) and c != ".":
        nums.append(num)

for line in f:
    schematic.append(line.replace('\n', ""))

numLocs = []
for row,line in enumerate(schematic):
    num = []
    for col,c in enumerate(line):
        if c.isdigit():
            num.append(c)
        elif len(num) > 0:
            numLocs.append(("".join([str(item) for item in num]), row, col - 1))
            num = []

for num,row,col in numLocs:
    if row == 0 and col - (len(num) - 1) == 0:
        for c in schematic[row + 1][0:len(num) + 1]:
            checkCharacter(c, nums, num)
        checkCharacter(schematic[row][len(num) + 1], nums, num)

print(schematic)
print(numLocs)
print(nums)
f.close()