f = open("input\\day1.txt")
result = 0

for l in f:
    filteredString = ''.join(c for c in l if c.isdigit())
    lineSum = int(filteredString[0] + filteredString[-1])
    result += lineSum
    # print(result)

print(result)
f.close()