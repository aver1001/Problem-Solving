import sys
from collections import deque

sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

DP = [sys.maxsize]*(N+1)
DP[N] = 0
queue = deque([(N, 0)])

while queue:
    now, cnt = queue.popleft()
    if now == 1:
        DP[now] = cnt
        break

    if now % 3 == 0 and DP[now//3] >= cnt+1:
        DP[now//3] = cnt+1
        queue.append((now//3, cnt+1))
    if now % 2 == 0 and DP[now//2] >= cnt+1:
        DP[now//2] = cnt+1
        queue.append((now//2, cnt+1))
    if DP[now-1] >= cnt+1:
        DP[now-1] = cnt+1
        queue.append((now-1, cnt+1))

# 역추적

now = 1
answer = []
while True:
    answer.append(now)
    if now == N:
        break

    if now*3 <= N and DP[now*3] == DP[now]-1:
        now = now*3
    elif now*2 <= N and DP[now*2] == DP[now]-1:
        now = now*2
    elif now+1 <= N and DP[now+1] == DP[now]-1:
        now = now+1
    else:
        break

print(cnt)
print(*reversed(answer))
