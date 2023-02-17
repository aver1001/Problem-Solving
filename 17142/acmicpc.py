import queue
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

virus = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            board[y][x] = '-'

        if board[y][x] == 2:
            virus.append((y, x))
            board[y][x] = '*'


'''
0 빈칸
1 벽
2 바이러스를 놓을 수 있는 위치
'''
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def BFS(virusList):
    check = deepcopy(board)
    queue = deque([])
    answer = 0
    for y, x in virusList:
        queue.append([y, x, 1])
        check[y][x] = 1

    while queue:
        y, x, cnt = queue.popleft()

        for idx in range(4):
            ty = dy[idx]+y
            tx = dx[idx]+x

            if 0 <= ty < N and 0 <= tx < N:
                if check[ty][tx] == 0:
                    check[ty][tx] = cnt+1
                    queue.append([ty, tx, cnt+1])
                    answer = cnt + 1
                elif check[ty][tx] == '*':
                    check[ty][tx] = cnt+1
                    queue.append([ty, tx, cnt+1])

    for y in range(N):
        for x in range(N):
            if check[y][x] == 0:
                return 9999999

    return answer-1


answer = 9999999
for vList in combinations(virus, M):
    answer = min(answer, BFS(vList))

if answer == 9999999:
    print(-1)
else:
    print(answer)
