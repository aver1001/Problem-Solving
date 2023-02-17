import sys
import heapq
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

route = [[] for _ in range(N+1)]
check = [sys.maxsize]*(N+1)
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split(' '))

    route[A].append((B, -C))
    route[B].append((A, -C))

start, end = map(int, sys.stdin.readline().rstrip().split(' '))

heap = [[-sys.maxsize, start]]


while heap:
    max_w, v = heapq.heappop(heap)
    if v == end:
        print(-max_w)
        break

    for toNode, weight in route[v]:
        if check[toNode] <= weight:
            continue

        check[toNode] = weight
        heapq.heappush(heap, [max(max_w, weight), toNode])
