F = open("input\\day8.txt").read().strip()
I = F.split('\n')
ans = 0

steps, instructions = F.split('\n\n')

instrDict = {}
nodes = []
for i in instructions.split('\n'):
    key, value = i.split('=')
    if key[2] == 'A':
        nodes.append(key.strip())
    instrDict[key.strip()] = (value[2:5], value[7:10])

def isNodesNotEndingZ(nodeKeys):
    for n in nodeKeys:
        if n[2] != 'Z':
            return True
    return False


while isNodesNotEndingZ(nodes):
    for step in steps:
        for i,node in enumerate(nodes):
            if step == 'L':
                nodes[i] = instrDict[node][0]             
            elif step == 'R':
                nodes[i] = instrDict[node][1]
        ans += 1
        print(ans)

