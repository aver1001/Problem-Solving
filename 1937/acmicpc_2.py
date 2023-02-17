from collections import deque

import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
answer = 0

visited = [[0]*N for _ in range(N)]


def DFS(y, x):
    # 방문한적이 있다면
    if visited[y][x] != 0:
        return visited[y][x]

    visited[y][x] = 1
    for idx in range(4):
        ty = y+dy[idx]
        tx = x+dx[idx]
        # 좌표 넘어가는거 체크
        if 0 <= ty < N and 0 <= tx < N:
            if board[ty][tx] > board[y][x]:

                visited[y][x] = max(visited[y][x], DFS(ty, tx)+1)

    return visited[y][x]


for y in range(N):
    for x in range(N):
        DFS(y, x)

answer = 0
for v in visited:
    for i in v:
        answer = max(answer, i)

print(answer)
