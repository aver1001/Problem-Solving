import sys
from collections import deque
sys.stdin = open('input.txt', "r")

V, E = map(int, sys.stdin.readline().rstrip().split())
table ={i:{}for i in range(V)}
for _ in range (E):
    u,v,w = map(int, sys.stdin.readline().rstrip().split())
    u -= 1
    v -= 1
    if v in table[u]:
        table[u][v] = min(table[u][v],w)
    else:
        table[u][v] = w
        
    if v in table[v]:
        table[v][u] = min(table[v][u],w)
    else:
        table[v][u] = w

Mdis = [0]*V
M,x =map(int, sys.stdin.readline().rstrip().split())
mcdonaldsQueue = deque([])
for i in map(int, sys.stdin.readline().rstrip().split()):
    Mdis[i-1] = -1
    mcdonaldsQueue.append((i-1,0)) # idx, cost

while mcdonaldsQueue:
    Loc,cost = mcdonaldsQueue.popleft()
    for nextLoc,nextCost in table[Loc].items():
        #맥세권 최대거리 제한
        if cost + nextCost > x:
            continue
        if Mdis[nextLoc] == 0 or Mdis[nextLoc] > cost+nextCost:
            Mdis[nextLoc] = nextCost+cost
            mcdonaldsQueue.append((nextLoc,cost+nextCost))
   
Sdis = [0]*V 
starBucksQueue = deque([])
S,y =map(int, sys.stdin.readline().rstrip().split())
for i in map(int, sys.stdin.readline().rstrip().split()):
    Sdis[i-1] = -1
    starBucksQueue.append((i-1,0)) # idx, cost
    
    
while starBucksQueue:
    Loc,cost = starBucksQueue.popleft()
    for nextLoc,nextCost in table[Loc].items():
        #스세권 최대거리 제한
        if cost + nextCost > y:
            continue
        if Sdis[nextLoc] == 0 or Sdis[nextLoc] > cost+nextCost:
            Sdis[nextLoc] = nextCost+cost
            starBucksQueue.append((nextLoc,cost+nextCost))
Mins = sys.maxsize
for idx in range (V):
    if Mdis[idx] == 0 or Mdis[idx] == -1 or Sdis[idx] == 0 or Sdis[idx] == -1:
        continue
    Mins = min(Mdis[idx]+Sdis[idx],Mins)
           
if Mins == sys.maxsize:
    print(-1)
else:
    print(Mins)
    
    
    