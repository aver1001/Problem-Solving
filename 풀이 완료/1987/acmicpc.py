import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))

direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def BFS():
    queue = deque()
    check = set()
    check.add(board[0][0])
    queue.append([(0, 0), 1, check])

    while queue:
        pos, cnt, check = queue.popleft()
        y, x = pos
        for addy, addx in direct:
            if 0 <= y+addy < Y and 0 <= x+addx < X and board[y+addy][x+addx] not in check:
                temp = check.copy()
                temp.add(board[y+addy][x+addx])
                queue.append([(y+addy, x+addx), cnt+1, temp])

    return cnt


def DFS(pos, check, cnt, d):
    global answer
    y, x = pos
    if cnt > answer:
        answer = cnt
    for addy, addx in direct:
        if 0 <= y+addy < Y and 0 <= x+addx < X and board[y+addy][x+addx] not in check:

            check.add(board[y+addy][x+addx])
            DFS((y+addy, x+addx), check, cnt+1, d+board[y+addy][x+addx])
            check.remove(board[y+addy][x+addx])


print(BFS())
