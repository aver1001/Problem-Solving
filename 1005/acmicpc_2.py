import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    time = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    table = {i: [] for i in range(N)}
    inCount = {i: 0 for i in range(N)}
    for _ in range(K):
        before, after = map(int, sys.stdin.readline().rstrip().split(' '))
        before -= 1
        after -= 1
        table[before].append(after)
        inCount[after] += 1

    last = int(sys.stdin.readline().rstrip())-1
    check = [0 for _ in range(N)]
    queue = deque([])

    for key, value in inCount.items():
        if value == 0:
            queue.append(key)
            check[key] = time[key]

    while queue:
        now = queue.popleft()

        # 위상정렬
        for next in table[now]:
            inCount[next] -= 1
            check[next] = max(check[next], check[now]+time[next])
            if inCount[next] == 0:
                queue.append(next)

    print(check[last])
