import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
commend = sys.stdin.readline().rstrip().split()

route = []

def find(x):
    if root[x] != x:
        root[x] = find(root[x]) 
    return root[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a > b:
        root[a] = b
    else:
        root[b] = a

for _ in range (M):
    u,v,d = map(int, sys.stdin.readline().rstrip().split())
    u -= 1
    v -= 1
    if commend[u] == commend[v]:
        continue
    route.append((d,u,v))
    
route.sort()
root = [i for i in range (N+1)]
answer = 0
cnt = 0

for cost,a,b in route:
    
    if find(a) != find(b):
        union(a,b)
        answer+= cost
        cnt += 1
if cnt != N-1:
    print(-1)
else:
    print(answer)
