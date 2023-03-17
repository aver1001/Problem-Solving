import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', "r")

def calDistanceHap(A:int,B:int):
    isVisited = [False]*(N+1)
    queue = deque([(A,0),(B,0)])
    answer = 0
    
    while queue:
        loc,cost = queue.popleft()
        if isVisited[loc] == False:
            isVisited[loc] = True
        else:
            continue
        answer += cost*2
        
        for nextLoc in table[loc]:
            if isVisited[nextLoc] == False:
                queue.append((nextLoc,cost+1))


    return answer

N,M = map(int, sys.stdin.readline().rstrip().split())
table = {i : set() for i in range (1,N+1)}
for _ in range (M):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    table[A].add(B)
    table[B].add(A)

minDis = sys.maxsize
for A,B in combinations(range (1,N+1),2):
    Dis = calDistanceHap(A,B)
    if Dis < minDis:
        minDis = Dis
        answer = (A,B)
        
print(*answer,minDis)