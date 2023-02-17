import sys
from collections import deque
sys.stdin = open('input.txt', "r")

board = []

for _ in range(3):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

check = set()
answer = 9999
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def isAnswer():
    cnt = 1
    temp = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == 0:
                temp.append((board[y][x]))
                continue

            if board[y][x] == cnt:
                cnt += 1
            temp.append((board[y][x]))
    temp = tuple(temp)

    if cnt == 9:
        return True, temp
    else:
        return False, temp


queue = deque([[0]])

while queue:
    y, x, cnt = queue.popleft()
