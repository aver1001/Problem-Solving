import sys
from bisect import bisect_left, bisect_right
sys.stdin = open('input.txt', "r")

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

m = N//2
n = N - m

first = [0] * (1 << n)

for i in range(1 << n):
    for k in range(n):
        if (i & (1 << k)) > 0:
            first[i] += numbers[k]

second = [0]*(1 << m)
for i in range(1 << m):
    for k in range(m):
        if (i & (1 << k)) > 0:
            second[i] += numbers[k+n]

second.sort()

answer = 0
for f in first:
    answer += bisect_right(second, S-f) - bisect_left(second, S-f)

if S == 0:
    answer -= 1
print(answer)
