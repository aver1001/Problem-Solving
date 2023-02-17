import sys, heapq
import time

start = time.time()

sys.stdin = open('input.txt', "r")
# 입력부
n,m,k = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
    
# inf : 임의의 무한대값
inf = 98765432109876543210

# d : 2차원 다익스트라 배열. 현재 정점 i에서 포장을 j개 했을 때 드는 최소거리
d = [[inf] * (k + 1) for _ in range(n + 1)]
q = []
for i in range(k + 1):
    d[1][i] = 0
heapq.heappush(q, (0,1,0))

cnt = 0
# 다익스트라 
while q:
    now_dist, now, p = heapq.heappop(q)
    if d[now][p] < now_dist:
        continue
    # 현재 정점에서 포장이 가능한 경우
    if p + 1 <= k:
        for (next, next_dist) in adj[now]:
            if d[next][p + 1] > now_dist:
                d[next][p + 1] = now_dist
                heapq.heappush(q, (now_dist, next, p + 1))
                
                
    # 기본적으로 포장을 하지 않는 경우
    for (next, next_dist) in adj[now]:
        if d[next][p] > now_dist + next_dist:
            d[next][p] = now_dist + next_dist
            heapq.heappush(q, (now_dist + next_dist, next, p))
            cnt += 1
            
# 정답 출력
ans = inf
for i in range(k + 1):
    ans = min(ans, d[n][i])

for i in d:
    print(i)
print() 

print(cnt)