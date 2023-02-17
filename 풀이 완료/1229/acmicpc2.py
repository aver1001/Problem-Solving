import sys
import time
sys.stdin = open('input.txt', "r")
INF = 10 ** 9

d = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [INF] * 1_000_000


def get_hex(limit):  # limit 이하의 육각수 구하기
    n = 1
    current = 0
    ans = []
    while current <= limit:
        current = n * (2 * n - 1)
        ans.append(current)
        n += 1
    return ans[:-1]


def solution():
    n = int(sys.stdin.readline().rstrip())
    if n < 13:
        print(d[n])
        return

    hex = get_hex(n)
    for i in range(13, n + 1):
        min_val = INF
        for h in hex:
            if h > i: break
            min_val = min(min_val, d[i - h])
        d[i] = min_val + 1
    print(d[n])


start = time.time()
solution()
print(time.time()-start)