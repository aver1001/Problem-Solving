import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

info = []
heap = []
for _ in range (N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    info.append((min(start,end),max(start,end)))
info.sort(key=lambda x:x[1])

answer = 0


D = int(sys.stdin.readline().rstrip())
for start,end in info:
    heapq.heappush(heap,start)
    while len(heap) != 0:
        temp = heapq.heappop(heap)
        if end-D > temp:
            continue
        else:
            heapq.heappush(heap,temp)
            break
    answer = max(answer,len(heap))
print(answer)