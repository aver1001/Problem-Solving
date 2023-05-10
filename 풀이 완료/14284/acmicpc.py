import sys
import heapq
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
table ={i:{} for i in range (1,N+1)}

for _ in range (M):
    a,b,cost = map(int, sys.stdin.readline().rstrip().split())
    table[a][b] = cost
    table[b][a] = cost

distance = [sys.maxsize]*(N+1)
start,end = map(int, sys.stdin.readline().rstrip().split())

heap = []

heapq.heappush(heap,(0,start))
distance[start] = 0

while heap:
    
    cost,loc = heapq.heappop(heap)
    
    if distance[loc] < cost:
        continue
    
    for nextLoc, nextCost in table[loc].items():
        hapCost = nextCost + cost
        if hapCost < distance[nextLoc]:
            distance[nextLoc] = hapCost
            heapq.heappush(heap,[hapCost, nextLoc])
print(distance[end])