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
        almanac[l] = []
        isNewSection = False
        currentSection = l
    else:
        nums = l.strip().split(" ")
        almanac[currentSection].append((int(nums[0]), int(nums[1]), int(nums[2]))) # (dest, src, range)

source = -1
locations = []

for seed in seeds:
    source = seed
    for map in almanac:
        for dest,src,range in almanac[map]:
            if src <= source <= src + range:
                if map == list(almanac)[-1]:
                  locations.append((source - src) + dest)
                else:
                    source = (source - src) + dest
                break
            else:
                if map == list(almanac)[-1] and (dest,src,range) == almanac[map][-1]:
                    locations.append(source)    
        
print(seeds)
print(almanac)
print(min(locations))
f.close()