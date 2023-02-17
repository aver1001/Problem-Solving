import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    time = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    table = {i: [] for i in range(N)}
    for _ in range(K):
        before, after = map(int, sys.stdin.readline().rstrip().split(' '))
        before -= 1
        after -= 1
        table[after].append(before)

    last = int(sys.stdin.readline().rstrip())-1
    queue = deque([[last, time[last]]])
    check = [0]*N
    while queue:
        now, cost = queue.popleft()
        # 이미 방문한곳인데 내가 지금 코스트보다 적으면 break
        if check[now] >= cost:
            continue
        check[now] = cost

        for next in table[now]:
            if next in table:
                queue.append([next, cost+time[next]])

    print(max(check))
