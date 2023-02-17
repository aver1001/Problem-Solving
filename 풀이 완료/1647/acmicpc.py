import sys
import heapq 
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())

table = [[]for _ in range (N+1)]
isVisited = [False]*(N+1)
for _ in range (M):
    A,B,C = map(int, sys.stdin.readline().rstrip().split())
    table[A].append((C,B))
    table[B].append((C,A))
    
heap = [(0,1)]
answer = []
while heap:

    cost,Loc = heapq.heappop(heap)
    if isVisited[Loc] == True:
        continue
    
    isVisited[Loc] = True
    answer.append(cost)
    
    for nextCost, nextLoc in table[Loc]:
        #방문 안했을경우만
        if isVisited[nextLoc] == False:
            #힙에 넣어준다.
            heapq.heappush(heap,(nextCost,nextLoc))
print(sum(answer)-max(answer))
