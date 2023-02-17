import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split())
caffaine = list(map(int, sys.stdin.readline().rstrip().split(' ')))

caffaine.sort()
table = [[101]*(K+1) for _ in range(N)]

for i in range(N):
    if K < caffaine[i]:
        continue
    table[i][caffaine[i]] = 1


for y in range(1, N):
    for x in range(K+1):
        if x < caffaine[y]:
            table[y][x] = table[y-1][x]
        elif x == caffaine[y]:
            table[y][x] = 1
        else:
            # 전에 도착했던 카페인
            table[y][x] = min(table[y-1][x], table[y-1][x-caffaine[y]]+1)

for i in table:
    print(i)


if table[-1][K] == 101:
    print(-1)
else:
    print(table[-1][K])
