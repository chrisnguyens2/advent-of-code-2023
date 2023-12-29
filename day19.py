F = open("input\\day19.txt").read().strip()
ans = 0
W,P = F.split('\n\n')
W = W.split('\n')
workflows = {}
for w in W:
    ruleName = w.split("{")[0]
    conditions = [x.split(":") for x in w.replace("}","").split("{")[1].split(",")]
    workflows[ruleName] = conditions 

P = [y.split(",") for y in [x.replace("{","").replace("}","") for x in P.split('\n')]]

for part in P:
    x = int(part[0][2:])
    m = int(part[1][2:])
    a = int(part[2][2:])
    s = int(part[3][2:])

    result = 'in'
    metRule = False
    while True:
        for rule in workflows[result]:
            if len(rule) != 1:
                metRule = eval(rule[0])
                if metRule:
                    result = rule[1]
                    break
            else:
                result = rule[0]
        if result == 'R':
            break
        elif result == 'A':
            ans += (x + m + a + s)
            break

print(ans)

