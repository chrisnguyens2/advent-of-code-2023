f = open("input\\day17.txt")

A = []
for line in f:
    r = []
    for c in list(line.strip().strip('\n')):
        r.append(int(c))
    A.append(r)


def min_neighbor_indices(prev, curr, n_rows, m_cols, exclude = None):
    x,y = curr
    neighbors = [[x+1,y], [x,y+1], [x-1,y], [x,y-1]] #Define neighbors
    neighbors = [[i,j] for i, j in neighbors if (i>=0) & (i<n_rows) & (j>=0) & (j<m_cols) & ([i,j]!=exclude)] #Filter neighbors
    #Search
    min_val = min([A[i][j] for i,j in neighbors])
    for i,j in neighbors:
        if A[i][j] == min_val:
            print(min_val)
            return [i,j]

# Test
print(min_neighbor_indices(prev = [1,0], curr=[1,1], n_rows = len(A), m_cols = len(A[0]))) #[2,1]
print(min_neighbor_indices(prev = [0,0], curr=[0,0], n_rows = len(A), m_cols = len(A[0]))) #[1,0]
print(min_neighbor_indices(prev = [0,0], curr=[0,0], n_rows = len(A), m_cols = len(A[0]), exclude = [1,0])) #[0,1]
print(min_neighbor_indices(prev = [2,0], curr=[2,1], n_rows = len(A), m_cols = len(A[0]), exclude = [1,0])) #[2,2]
def is_same_direction(prev, curr, next):
    print("Direction",prev, curr, next)
    if (prev[0] == curr[0]) & (curr[0]==next[0]):
        return True
    elif (prev[1] == curr[1]) & (curr[1]==next[1]):
        return True
    else:
        return False
    
print(is_same_direction(prev = [1,0], curr = [2,0], next=[3,0])) #True
print(is_same_direction(prev = [1,0], curr = [2,0], next=[2,1])) #False

n_rows, m_cols = len(A), len(A[0])
print(n_rows, m_cols)
n_rows, m_cols = 5,5 #Test
count = 0 # 3 move restriction
total = 0 # Result
curr, prev = [0,0], [0,0] #Starting point
n,m = 0,0
visited = [curr]
while  n < n_rows:
    while m < m_cols:
        total += A[n][m]
        next  = min_neighbor_indices(prev, curr, n_rows, m_cols)
        #Case 1: Loop (and reverse direction)
        if next in visited:
            # print("Next's in a loop")
            next = min_neighbor_indices(prev, curr, n_rows, m_cols, exclude = next)
        #Case 2: Three in the same direction 
        if is_same_direction(prev, curr, next):
            count+=1    
        if count == 2:
            # print("3 in a row")
            next =  min_neighbor_indices(prev, curr, n_rows, m_cols, exclude = next)
            count = 0
        #Update
        print(prev, curr, next)
        prev = curr
        curr = next 
        visited.append(curr)
        n,m = curr #Increment

print(visited)
print(total)