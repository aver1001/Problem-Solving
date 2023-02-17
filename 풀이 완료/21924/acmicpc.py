import sys
import heapq
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split())

table = {i:{} for i in range (1,N+1)}
total = 0
for _ in range (M):
    a,b,cost= map(int, sys.stdin.readline().rstrip().split())
    total += cost
    table[a][b] = cost
    table[b][a] = cost

heap = [(0,1)]
answer = 0
cnt = 0
isVisited = [False]*(N+1)
isVisited[0] = True
while heap:
    #print(heap)
    cost,Loc = heapq.heappop(heap)
    
    if isVisited[Loc] == True:
        continue
    if cnt == N:
        break
    #print(Loc)
    isVisited[Loc] = True
    answer += cost
    cnt += 1
    
    
    
    for nextLoc,nextCost in table[Loc].items():
        if isVisited[nextLoc] == False:
            heapq.heappush(heap,(nextCost,nextLoc))

if all(num for num in isVisited):
    print(total-answer)
else:
    print(-1)