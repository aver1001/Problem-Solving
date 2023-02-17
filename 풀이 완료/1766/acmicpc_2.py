import sys
from collections import deque
import heapq
sys.stdin = open('input.txt', "r")
'''
문제는 난이도 순서로 출제되어 있다.
1이 쉬운거 N이 어려운거

문제간의 관계가 있는 경우가 있다.

1. N개의 문제는 모두 풀어야 한다.
2. 먼저 푸는 것이 좋은 문제가 잇는 문제는, 반드시 먼져 풀어야한다.
3. 가능하다면 쉬운문제부터 풀어야 한다.

'''
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
check = [0] * (N+1)
table = [[] for _ in range(N+1)]
for _ in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split(' '))
    # 문제 : 선수문제
    table[first].append(second)
    check[second] += 1

for idx in range(1, N+1):
    table[idx].sort()

heap = []
for idx in range(1, N+1):
    if check[idx] == 0:
        heapq.heappush(heap, idx)

answer = []
while heap:
    Next = heapq.heappop(heap)
    answer.append(Next)

    for n in table[Next]:
        check[n] -= 1
        if check[n] == 0:
            heapq.heappush(heap, n)

print(*answer)
