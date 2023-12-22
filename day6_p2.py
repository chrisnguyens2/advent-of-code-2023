f = open("input\\day6.txt")
file = f.readlines()
T=[]
D=[]

T = int(file[0].split(":")[1].replace(" ", "").replace("\n", ""))
D = int(file[1].split(":")[1].replace(" ", ""))

countWin = 0
for tt in range(1, T - 1):
    if (T - tt) * tt > D:
        countWin += 1

print(T)
print(D)
print(countWin)
f.close()