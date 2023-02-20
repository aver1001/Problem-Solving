import sys
sys.stdin = open('input.txt', "r")

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a >= b:
        root[a] = b
    else:
        root[b] = a
        

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m,k = map(int, sys.stdin.readline().rstrip().split())
friendCost = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
root = [i for i in range (n+1)]
for _ in range (m):
    v,w = map(int, sys.stdin.readline().rstrip().split())
    if find(v) != find(w):
        union(v,w)

check = {}
for idx in range (1,n+1):
    if find(idx) in check:
        check[find(idx)] = min(check[find(idx)], friendCost[idx])
    else:
        check[find(idx)] = friendCost[idx]
        
answer = sum(check.values())
if answer > k:
    print('Oh no')
else:
    print(answer)