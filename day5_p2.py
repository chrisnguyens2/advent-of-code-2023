f = open("input\\day5.txt")

seedRanges = []
seeds = []
almanac = {}

isNewSection = False
currentSection = ""
for line in f:
    l = line.strip()
    if l.startswith("seeds: "):
        seedStrings = l.split("seeds: ")[1].split(" ")
        seeds = [eval(i) for i in seedStrings]

        for i in range(0, len(seeds), 2):
            seedRanges.append((seeds[i], seeds[i+1] - 1))

    elif l == '':
        isNewSection = True
    elif isNewSection:
        almanac[l] = []
        isNewSection = False
        currentSection = l
    else:
        nums = l.strip().split(" ")
        almanac[currentSection].append((int(nums[0]), int(nums[1]), int(nums[2]) - 1)) # (dest, src, range)

currentSourceRanges = []
newSourceRanges = []
locations = []

for seed in seedRanges:
    currentSourceRanges.append(seed)
    for sourceRange in currentSourceRanges:
        for map in almanac:
            for dest,src,r in almanac[map]: 
                srcMin = sourceRange[0]
                srcMax = sourceRange[0] + sourceRange[1]
                mapSrcMin = src
                mapSrcMax = src + r
                if srcMin <= mapSrcMax and srcMax >= mapSrcMin: #overlap exists
                    overlap = (max(srcMin, mapSrcMin), min(srcMax, mapSrcMax)) #overlap
                    if map == list(almanac)[-1]:
                        locations.append((overlap[0] - mapSrcMin) + dest)
                        print(map)
                        print((overlap[0] - mapSrcMin) + dest)
                    else:                    
                        minOverlap = ((overlap[0] - mapSrcMin) + dest, overlap[1] - overlap[0])
                        newSourceRanges.append(minOverlap)
                        if overlap[0] > mapSrcMin:
                            newSourceRanges.append(mapSrcMin, overlap[0] - mapSrcMin)
                        if overlap[1] < mapSrcMax:
                            newSourceRanges.append(overlap[1], mapSrcMax - overlap[1])
                        print(map)
                        print(minOverlap)
                else:
                    if map == list(almanac)[-1] and (dest,src,r) == almanac[map][-1]:
                        locations.append(srcMin)
                        print(map)
                        print(srcMin)
                    else:
                        newSourceRanges.append((src,r))

            # if src <= source <= src + r:
            #     if map == list(almanac)[-1]:
            #       locations.append((source - mapSrc) + dest)
            #     else:
            #         source = (source - mapSrc) + dest
            #     break
            # else:
            #     if map == list(almanac)[-1] and (dest,src,r) == almanac[map][-1]:
            #         locations.append(source)    
        
#print(seeds)
print(seedRanges)
print(min(locations))
f.close()