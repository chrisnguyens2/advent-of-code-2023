F = open("input\\day8.txt").read().strip()
I = F.split('\n')
ans = 0

steps, instructions = F.split('\n\n')

instrDict = {}
for i in instructions.split('\n'):
    key, value = i.split('=')
    instrDict[key.strip()] = (value[2:5], value[7:10])

node = 'AAA'
while node != 'ZZZ':
    for step in steps:
        if node == 'ZZZ':
            break
        if step == 'L':
            node = instrDict[node][0]
            ans += 1
        elif step == 'R':
            node = instrDict[node][1]
            ans += 1

print(ans)