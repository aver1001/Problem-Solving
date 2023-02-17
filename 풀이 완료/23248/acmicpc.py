import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

m, n, k = map(int, sys.stdin.readline().rstrip().split(' '))
data = [tuple(map(int, input().split())) for _ in range(k)]
data.sort()
data = [i[1] for i in data]
data.reverse()
dp = []
for i in range(len(data)):
    idx = bisect_left(dp, data[i])
    if idx == len(dp):
        dp.append(data[i])
    else:
        dp[idx] = data[i]
print(len(dp))
