import sys
import heapq
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())

table = {i:{} for i in range (1,N+1)}
for _ in range (M):
    a,b,t = map(int, sys.stdin.readline().rstrip().split())
    
    if b in table[a]:
        table[a][b] = min(table[a][b],t)
    else:
        table[a][b] = t
    
    if a in table[b]:
        table[b][a] = min(table[b][a],t)
    else:
        table[b][a] = t

def dj(start,end):
    dis = [sys.maxsize]*(N+1)
    
    dis[1] = 0
    heap = []
    heapq.heappush(heap,[0,1])
    while heap:
        distance, loc = heapq.heappop(heap)
        for nextLoc,nextDistance in table[loc].items():
            hapDistance = nextDistance + distance
            if start==loc and end==nextLoc or start==nextLoc and end==start: continue
            if dis[nextLoc] > hapDistance:
                dis[nextLoc] = hapDistance
                pre[nextLoc] = loc
                heapq.heappush(heap,[hapDistance,nextLoc])
    return dis[N]
pre=[0]*(N+1)

result = dj(1,0)
ans = -1
e = N

while pre[e]!=0:
    s = pre[e]
    output = dj(s, e)
    if output != sys.maxsize:
        diff = output-result
        ans = max(ans, diff)
    else:
        ans = -1
        break
    e = s
print(ans)