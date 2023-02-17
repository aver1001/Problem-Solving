import sys
import heapq
sys.stdin = open('input.txt', "r")

N,M,X = map(int, sys.stdin.readline().rstrip().split())

route = [[0]*(N+1) for _ in range (N+1)]

for _ in range(M):
    A,B,C = map(int, sys.stdin.readline().rstrip().split())
    route[A][B] = C
    
def dj(start):
    cost = [100*M]*(N+1)
    cost[start] = 0
    heap =[(start,0)]
    
    while heap:
        nowLoc, nowCost = heapq.heappop(heap) 
        
        for nextLoc in range (1,N+1):
            if route[nowLoc][nextLoc] != 0 and cost[nextLoc] > route[nowLoc][nextLoc]+nowCost:
                cost[nextLoc] = route[nowLoc][nextLoc]+nowCost
                heapq.heappush(heap,(nextLoc,route[nowLoc][nextLoc]+nowCost))
     
    
    return(cost[1:])
        
        
def reverseDJ(start):
    cost = [100*M]*(N+1)
    cost[start] = 0
    heap =[(start,0)]
    
    while heap:
        nowLoc, nowCost = heapq.heappop(heap) 
        
        for nextLoc in range (1,N+1):
            if route[nextLoc][nowLoc] != 0 and cost[nextLoc] > route[nextLoc][nowLoc]+nowCost:
                cost[nextLoc] = route[nextLoc][nowLoc]+nowCost
                heapq.heappush(heap,(nextLoc,route[nextLoc][nowLoc]+nowCost))
     
    
    return(cost[1:])

answer = 0
for a,b in zip(dj(X),reverseDJ(X)):
    if a+b > answer:
        answer = a+b
print(answer)