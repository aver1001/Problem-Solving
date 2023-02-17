import sys
sys.stdin = open('input.txt', "r")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] and a[k][j]:
                a[i][j] = 1

    

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if a[x-1][y-1] == 1:
        print(-1)
    elif a[y-1][x-1] == 1:
        print(1)
    elif a[x-1][y-1] == 0:
        print(0)