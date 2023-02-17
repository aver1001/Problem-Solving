from inspect import isroutine
import sys
from collections import deque
sys.stdin = open('input.txt', "r")

X, Y, H = map(int, sys.stdin.readline().rstrip().split())


board = []
queue = deque([])
for h in range(H):
    temp = []
    for y in range(Y):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
        for x in range(X):
            if temp[y][x] == 1:
                queue.append((h, y, x))
    board.append(temp)

dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dh = (0, 0, 0, 0, -1, 1)

Flag = False
while queue:
    Flag = True
    h, y, x = queue.popleft()
    for idx in range(6):
        th = h+dh[idx]
        ty = y+dy[idx]
        tx = x+dx[idx]

        if 0 <= th < H and 0 <= ty < Y and 0 <= tx < X and board[th][ty][tx] == 0:
            board[th][ty][tx] = board[h][y][x] + 1
            queue.append((th, ty, tx))

answer = 0
for h in range(H):
    for y in range(Y):
        for x in range(X):
            if board[h][y][x] == 0:
                print(-1)
                exit()
            else:
                if board[h][y][x] > answer:
                    answer = board[h][y][x]

print(answer - 1)
