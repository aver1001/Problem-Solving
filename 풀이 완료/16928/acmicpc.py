import sys
from collections import deque

sys.stdin = open('input.txt', "r")

N,M= map(int, sys.stdin.readline().rstrip().split())
table={}
for _ in range (N):
    FROM,TO= map(int, sys.stdin.readline().rstrip().split())
    table[FROM] = TO
    
for _ in range (M):
    FROM,TO= map(int, sys.stdin.readline().rstrip().split())
    table[FROM] = TO
    
queue = deque([(1,0)]) #loc, cnt

isVisited = [False]*101

while queue:
    loc, cnt = queue.popleft()
    #print(loc)
    if loc == 100:
        print(cnt)
        exit(0)
    for i in range (1,7):
        nextLoc = loc + i
        if nextLoc in table:
            nextLoc = table[nextLoc]
        if nextLoc <= 100 and isVisited[nextLoc] == False:
            isVisited[nextLoc] = True
            queue.append((nextLoc,cnt+1))