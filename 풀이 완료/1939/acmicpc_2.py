import sys
import heapq
sys.stdin = open('input.txt', "r")
input = sys.stdin

INF = -1000000000
n, m = map(int, sys.stdin.readline().rstrip().split())
link = [[] for _ in range(n+1)]
visited = [-INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    link[a].append((b, -c))
    link[b].append((a, -c))
start, end = map(int, sys.stdin.readline().rstrip().split())

hq = [(INF, start)]
while hq:
    print(hq)
    max_w, v = heapq.heappop(hq)
    if v == end:
        print(-max_w)
        break
    for toNode, weight in link[v]:
        if visited[toNode] <= weight:
            continue
        visited[toNode] = weight
        heapq.heappush(hq, (max(max_w, weight), toNode))
