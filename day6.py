f = open("input\\day6.txt")
file = f.readlines()
T=[]
D=[]
result = []
product=1
print(file)
l1 = file[0].split(":")[1].split(" ")
for x in l1:    
    if x != "":        
        T.append(int(x.replace("\n","")))

l2 = file[1].split(":")[1].split(" ")
for x in l2:    
    if x != "":        
        D.append(int(x.replace("\n","")))

for i,t in enumerate(T):
    countWin = 0
    for tt in range(1, t - 1):
        if (t - tt) * tt > D[i]:
            #print(f'{(t-tt)*tt} > {D[i]}')
            countWin += 1
    result.append(countWin)
    product *= countWin

print(result)
print(product)
f.close()