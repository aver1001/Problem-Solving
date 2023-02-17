import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt', "r")

N, L = map(int, sys.stdin.readline().rstrip().split(' '))
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

Pqueue = []
# 가장 처음 범위를 구해준뒤
# 다 힙에 넣어주고
# 계속반복

# 반복
for i in range(N):
    lt = i - L + 1

    while Pqueue and Pqueue[0][1] < lt:
        heappop(Pqueue)

    heappush(Pqueue, (commend[i], i))

    print(Pqueue[0][0], end=' ')
