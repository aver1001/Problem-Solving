import sys
from collections import deque
sys.stdin = open('input.txt', "r")

X, Y = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(Y):
    board.append(sys.stdin.readline().rstrip().split(' '))

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

Rotten = deque()
check = set()
for y in range(Y):
    for x in range(X):
        if board[y][x] == '1':
            Rotten.append((y, x, 0))

while Rotten:
    y, x, cnt = Rotten.popleft()
    check.add((y, x))
    for addy, addx in direction:
        if 0 <= y+addy < Y and 0 <= x+addx < X and board[y+addy][x+addx] == '0' and (y+addy, x+addx) not in check:
            board[y+addy][x+addx] = '1'
            Rotten.append((y+addy, x+addx, cnt+1))

for y in range(Y):
    if cnt == -1:
        break
    for x in range(X):
        if board[y][x] == '0':
            cnt = -1
            break

print(cnt)
