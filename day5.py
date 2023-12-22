f = open("input\\day5.txt")

seeds = []
almanac = {}

isNewSection = False
currentSection = ""
for line in f:
    l = line.strip()
    if l.startswith("seeds: "):
        seedStrings = l.split("seeds: ")[1].split(" ")
        seeds = [eval(i) for i in seedStrings]

    elif l == '':
        isNewSection = True
    elif isNewSection:
        almanac[l] = {}
        isNewSection = False
        currentSection = l
    else:
        # input = destination range start, the source range start, and the range length
        # map = source : dest
        nums = l.strip().split(" ")
        for x in range(int(nums[2])):
            almanac[currentSection][int(nums[1]) + x] = int(nums[0]) + x

source = -1
locations = []

for seed in seeds:
    source = seed
    for map in almanac:
        if source in almanac[map]:          
            if map == list(almanac)[-1]:
                  locations.append(almanac[map][source])
            else:
                source = almanac[map][source]
        else:
            if map == list(almanac)[-1]:
                locations.append(source)       
        
print(seeds)
#print(almanac)
print(min(locations))
f.close()