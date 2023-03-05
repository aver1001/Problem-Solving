import sys
from collections import deque
import heapq
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
isVisiable = list(map(int, sys.stdin.readline().rstrip().split()))
isVisiable[-1] = 0
MAXT  = N * 100000
table ={i : set() for i in range (N)}
for _ in range (M):
    a,b,t = map(int, sys.stdin.readline().rstrip().split())
    if isVisiable[a] == 1 or isVisiable[b] == 1:
        continue
    table[a].add((b,t))
    table[b].add((a,t))


cost = [MAXT]*N
cost[0] = 0
heap = [(0,0)]


while heap:
    nowCost,nowLoc = heapq.heappop(heap)
    
    if cost[nowLoc] < nowCost:
        continue
    
    for nextLoc,nextCost in table[nowLoc]:
        if nextCost+nowCost < cost[nextLoc]:
            cost[nextLoc] = nextCost+nowCost
            heapq.heappush(heap,(nextCost+nowCost,nextLoc))
        

if cost[-1] == MAXT:
    print(-1)
else:
    print(cost[-1])