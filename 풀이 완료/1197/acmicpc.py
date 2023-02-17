import sys
import heapq

sys.stdin = open('input.txt', "r")

V,M = map(int, sys.stdin.readline().rstrip().split())
table = {i:{} for i in range (1,V+1)}
for _ in range (M):
    #A,B가 가중치 C로 연결되어 있음.
    A,B,C = map(int, sys.stdin.readline().rstrip().split())
    table[A][B] = C
    table[B][A] = C
    
isVisited = [False]*(V+1)
heap = [(0,1)]
answer = 0
while heap:
    cost, Loc = heapq.heappop(heap)
    
    if isVisited[Loc] == True:
        continue
    isVisited[Loc] = True

    answer += cost
    
    for nextLoc, nextCost in table[Loc].items():
        #방문한 노드일경우 패스
        if isVisited[nextLoc] == True:
            continue
        #최소힙에 넣어준다
        heapq.heappush(heap,(nextCost,nextLoc))

    
print(answer)