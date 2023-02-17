import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())


temp = [[]for _ in range(N+1)]
for _ in range(N):
    deadLine, cupRamen = map(int, sys.stdin.readline().rstrip().split(' '))
    temp[deadLine].append([cupRamen, deadLine])

heap = []
answer = 0
for idx in range(N, 0, -1):

    for cupRamen, _ in temp[idx]:
        heapq.heappush(heap, -cupRamen)

    if heap:
        answer += -heapq.heappop(heap)
print(answer)
