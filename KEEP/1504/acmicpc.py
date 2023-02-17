import sys
import heapq
sys.stdin = open('input.txt', "r")

N,E = map(int, sys.stdin.readline().rstrip().split())

route = {i:{} for i in range (1,N+1)}
for _ in range (E):
    A,B,cost = map(int, sys.stdin.readline().rstrip().split())
    route[A][B] = cost
    route[B][A] = cost

A,B = map(int, sys.stdin.readline().rstrip().split())

def dj(start):
    #거리 최대값 초기화
    cost = [sys.maxsize]*(N+1)
    cost[start] = 0
    
    heap = [(0,start)]
    
    while heap:
        nowCost,nowLoc = heapq.heappop(heap)
        
        for nextLoc,nextCost in route[nowLoc].items():
            if nowCost + nextCost < cost[nextLoc]:
                cost[nextLoc] = nowCost + nextCost
                heapq.heappush(heap,(nowCost+nextCost,nextLoc))
    return cost
    
    

one = dj(1)
two = dj(A)
three = dj(B)

# 1 => A => B => N
result = min(one[A] +two[B] + three[N], one[B]+three[A]+two[N])
if result >= sys.maxsize:
    print(-1)
else:
    print(result)