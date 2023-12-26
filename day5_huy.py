# PART 1
f = open("input\\day5.txt")
f = [line.strip().strip("/") for line in f]

def map_extraction(map_range):
    res = []
    for i in range(map_range[0], map_range[1]):
        a, b, c = f[i].split(" ")
        res.append([int(b), int(a), int(c)])
    return res

seeds = [int(i) for i in f[0].strip("seeds:").strip().split(" ")]
seed_soil_map = map_extraction([3,31])
soil_fertilizer_map = map_extraction([33, 43])
fertilizer_water_map = map_extraction([45,54])
water_light_map =map_extraction( [56, 79])
light_temp_map = map_extraction([81, 113])
temp_humidity_map = map_extraction([115, 160])
humidity_location = map_extraction([162, 211])

map_list = [seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, 
            light_temp_map, temp_humidity_map, humidity_location]
final_location = []
for seed in seeds:
    for map in map_list:
        for source, target, range_ in map:
            if (seed >= source) & (seed <= source + range_-1):
                seed = target + seed - source 
                break            
    final_location.append(seed)
print("Solution part 1: ", min(final_location))

#Part 2:
def find_intersect(x1, y1, x2, y2):
    #Case 1:
    if (x1 <= x2) & (y1 <= y2) & (y1 >= x2):
        return [x2, y1]
    elif (x2 <= x1) & (y2 <= y1) & (y2 >= x1):
        return [x1, y2]
    elif (x1 <= x2) & (y2 <= y1):
        return [x2, y2]
    elif (x2 <= x1) & (y1 <= y2):
        return [x1, y1]
    return []

seed_pair = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
final_location = []
for start_seed, seed_range in seed_pair:
    for map in map_list:
        for source, target, source_range in map:
            #Find intersection
            intersect = find_intersect(start_seed, start_seed + seed_range-1, source, source + source_range-1)
            if len(intersect) != 0:
                start_seed = intersect[0]
                seed_range = intersect[1] - intersect[0] 
    final_location.append(start_seed)

print(final_location)
print("Solution part 2: ", min(final_location))



