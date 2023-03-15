import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")


N,M = map(int, sys.stdin.readline().rstrip().split())
DP = [[0]*M for _ in range (N)]
Path = [[0]*M for _ in range (N)]

company = []
for day in range (N):
    company.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])


answer = [0]*(M+1)
for y in range (N):
    for x in range (M):
        if x == 0:
            DP[y][x] = company[y][x]
            Path[y][x] = y+1
            continue
        
        if y == 0:
            if DP[y][x-1] > DP[y][x]:
                DP[y][x] = DP[y][x-1]
            else:
                Path[y][x] = y+1
        
        if company[y][x] < DP[y][x-1]:
            DP[y][x] = DP[y][x-1]
        else:
            DP[y][x] = company[y][x]
            Path[y][x] = y+1
        for money in range (y):
            if DP[y][x] < DP[money][x-1]+company[y-money-1][x]:
                DP[y][x] = DP[money][x-1]+company[y-money-1][x]
                Path[y][x] = y-money

# for c,i in zip(DP, Path):
#     print(c,"  ",i)

# print(DP[-1][-1])

money = N
choose = set()
answer = [0]*M
for y in range (N-1,-1,-1):
    for x in range (M-1,-1,-1):
        if x in choose:
            continue
        if money >= Path[y][x]:
            choose.add(x)
            answer[x] = Path[y][x]
            money -= Path[y][x]
print(DP[-1][-1])
print(*answer)