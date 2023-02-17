import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

# 테이블 초기화
table = {i: {} for i in range(N+1)}

# 버스정보 넣어줌
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split(' '))

    if b in table[a]:
        table[a][b] = min(table[a][b], cost)
    else:
        table[a][b] = cost

start, end = map(int, sys.stdin.readline().rstrip().split(' '))

heap = [[0, start]]
cost = [sys.maxsize]*(N+1)
isVisited = [False]*(N+1)
cost[start] = 0
isVisited[start] = True

while heap:
    nowCost, nowLoc = heapq.heappop(heap)

    for nextLoc, nextCost in table[nowLoc].items():
        if cost[nextLoc] > nextCost+nowCost and isVisited[nextLoc] == False:
            cost[nextLoc] = nextCost+nowCost

            heapq.heappush(heap, [nextCost+nowCost, nextLoc])

print(cost[end])
