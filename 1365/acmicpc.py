import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

heap = []
for idx, c in enumerate(commend, start=1):
    heapq.heappush(heap, [abs(idx-c), idx, c])

visited = [False]*N
answer = 0
while heap:
    cost, idx, c = heapq.heappop(heap)

    left = min(idx, c)
    right = max(idx, c)

    for idx in range(left-1, right-1):
        if visited[idx] == True:
            answer += 1
            break
    else:
        for idx in range(left-1, right-1):
            visited[idx] = True

print(answer)
# 1~2 = 0
# 1~3 = 0,1
# 2~3 = 1
