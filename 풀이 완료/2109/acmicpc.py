import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

info = [[]for _ in range (10001)]
#price, day
for _ in range (N):
    p,d  = map(int, sys.stdin.readline().rstrip().split())
    info[d].append(p)


heap = []
answer = 0
for day in range (10000,0,-1):
    for price in info[day]:
        heapq.heappush(heap,-price)
    if len(heap) > 0:
        temp = -heapq.heappop(heap)
        answer += temp
print(answer)