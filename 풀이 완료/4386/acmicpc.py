import sys
import math
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

def calDistance(a,b):
    x1,y1 = a
    x2,y2 = b
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def find(x):
    if Root[x] != x:
        Root[x] = find(Root[x])
    return Root[x]
        

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        Root[a] = b
    else:
        Root[b] = a

point = []
for idx in range (N):
    X, Y = map(float, sys.stdin.readline().rstrip().split())
    point.append((X,Y))

costs = []
for i in range(N-1):
    for j in range (i+1,N):
        costs.append((calDistance(point[i],point[j]),i,j))
costs.sort()

Root = [i for i in range (N+1)]

answer = 0
for cost, a,b in costs:
    
    if find(a) != find(b):
        union(a,b)
        answer += cost
        
        
print(round(answer, 2))