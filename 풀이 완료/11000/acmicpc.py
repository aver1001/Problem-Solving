import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
lessons = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lessons = sorted(lessons, key=lambda x: x[0])

q = []
for lesson in lessons:

    if q and q[0] <= lesson[0]:
        #
        heapq.heappop(q)
    heapq.heappush(q, lesson[1])


print(len(q))
