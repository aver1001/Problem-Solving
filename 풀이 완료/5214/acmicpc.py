import sys
from collections import deque
sys.stdin = open('input.txt', "r")

#역의 수 N, 한 하이퍼튜브가 연결하는 역의 개수 K, 하이퍼 튜브의 개수 M
N,K,M = map(int, sys.stdin.readline().rstrip().split())
targetHyperTube = {i:[] for i in range (1,N+1)}
hyperTube = []

for idx in range (M):
    temp = set(map(int, sys.stdin.readline().rstrip().split()))
    for t in temp:
        targetHyperTube[t].append(idx)
    hyperTube.append(temp)

isVisited = [False]*(N+1)
isVisited[1] = True
queue = deque([[1,1]])
if N == 1:
    print(1)
    exit(0)

while queue:
    loc,cnt = queue.popleft()
    
    for Ht in targetHyperTube[loc]:
        for nextLoc in hyperTube[Ht]:
                
            if nextLoc == N:
                print(cnt+1)
                exit(0)
            
            if isVisited[nextLoc] == False:
                isVisited[nextLoc] = True
                queue.append([nextLoc,cnt+1])
print(-1)