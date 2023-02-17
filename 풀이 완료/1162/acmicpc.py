import sys
import heapq
import time
start = time.time()
sys.stdin = open('input.txt', "r")

N,M,K = map(int, sys.stdin.readline().rstrip().split())
table= [[] for _ in range (N)]

for _ in range (M):
    A,B,cost = map(int, sys.stdin.readline().rstrip().split())
    A -= 1
    B -= 1
    table[A].append((B,cost))
    table[B].append((A,cost))

heap = [(0,0,1)]
DP = [[sys.maxsize]*(N) for _ in range (K+1)]

for i in range (K+1):
    DP[i][0] = 0
cnt = 0
while heap:
    Loc,cost,k = heapq.heappop(heap)
    
    if DP[k][Loc] < cost:
        continue
    if k+1 <= K :
        for nextLoc,nextCost in table[Loc]:
            #도로 포장할경우
            if DP[k+1][nextLoc] > cost:
                DP[k+1][nextLoc] = cost
                heapq.heappush(heap,(nextLoc,cost,k+1))
                
    #도로포장 안할경우
    for (nextLoc,nextCost) in table[Loc]:
        
        if DP[k][nextLoc] > cost+nextCost:
            DP[k][nextLoc] = cost+nextCost
            heapq.heappush(heap,(nextLoc,cost+nextCost,k))
            cnt += 1
for i in DP:
    print(i)
print(min(DP[-1])) 