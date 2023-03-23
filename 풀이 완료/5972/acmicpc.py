import sys
import heapq
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split())
table = {i : {} for i in range (1,N+1)}

# 농부 현서는 헛간 1에 있고
# 농부 찬홍이는 헛간 N에 있습니다.
for _ in range (M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    if b in table[a]:
        table[a][b] = min(table[a][b],cost)
    else:
        table[a][b] = {}
        table[a][b] = cost
        
    if a in table[b]:
        table[b][a] = min(table[b][a],cost)
    else:
        table[b][a] = {}
        table[b][a] = cost
#print(table)

dis = [sys.maxsize]*(N+1)
heap= [[1,0]]
while heap:
    Loc,cost = heapq.heappop(heap)
    
    if dis[Loc] < cost:
        continue
    
    for nextLoc, nextCost in table[Loc].items():
        if dis[nextLoc] > nextCost + cost:
            dis[nextLoc] = nextCost + cost
            heapq.heappush(heap,[nextLoc,nextCost+cost])
print(dis[-1])