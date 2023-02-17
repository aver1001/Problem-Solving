from calendar import c
import heapq
import sys
sys.stdin = open('input.txt', "r")
INF = sys.maxsize
V, E = map(int, sys.stdin.readline().rstrip().split(' '))
start = int(sys.stdin.readline())

table = {}
for i in range(1, V+1):
    table[i] = {}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(' '))
    table[u][v] = w

heap = [[0, start]]
cost = [INF]*(V+1)
cost[start] = 0

while heap:
    nowcost, nowloc = heapq.heappop(heap)

    for nextloc, nextcost in table[nowloc].items():
        if cost[nextloc] > nowcost+nextcost:
            cost[nextloc] = nowcost+nextcost

            heapq.heappush(heap, [cost[nextloc], nextcost])

for i in range(1, V+1):
    print("INF" if cost[i] == INF else cost[i])
