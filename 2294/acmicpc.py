import sys
from collections import deque
sys.stdin = open('input.txt', "r")

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = set()
for _ in range(n):
    coins.add(int(sys.stdin.readline().rstrip()))

DP = [0]*100001

# [위치,횟수]
queue = deque([[0, 0]])
while queue:

    now, cnt = queue.popleft()

    for c in coins:
        if now+c < 10001 and DP[c+now] == 0:
            if now+c == k:
                print(cnt+1)
                exit()
            DP[c+now] = cnt+1
            queue.append([c+now, cnt+1])
