import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt', "r")


def printBoard(num):
    for i in board[num]:
        print(i)
    print()


def rotate90(board):
    return list(zip(*board[::-1]))


dy = (-1, 0, 1, 0, 0, 0)
dx = (0, 1, 0, -1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)


def BFS(board):
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    queue = deque([[0, 0, 0, 0]])
    while queue:
        z, y, x, cnt = queue.popleft()

        for idx in range(6):
            ty = y+dy[idx]
            tx = x+dx[idx]
            tz = z+dz[idx]
            if 0 <= ty < 5 and 0 <= tx < 5 and 0 <= tz < 5 and board[tz][ty][tx] == 1 and visited[tz][ty][tx] == False:

                if tz == 4 and ty == 4 and tx == 4:
                    # 도착
                    return cnt+1
                visited[tz][ty][tx] = True
                queue.append((tz, ty, tx, cnt+1))
    return 3125


def DFS(per):
    temp = 3125
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        board = [rotateBoard[per[0]][a], rotateBoard[per[1]][b],
                                 rotateBoard[per[2]][c], rotateBoard[per[3]][d], rotateBoard[per[4]][e]]

                        if board[0][0][0] == 1 and board[4][4][4] == 1:
                            temp = min(BFS(board), temp)
    return temp


board = []
rotateBoard = [[] for _ in range(5)]
for idx in range(5):
    temp = []
    for _ in range(5):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

    for _ in range(4):
        temp = rotate90(temp)
        rotateBoard[idx].append(temp)

answer = 3125
for per in list(permutations([0, 1, 2, 3, 4], 5)):

    answer = min(DFS(per), answer)
if answer == 3125:
    print(-1)
else:
    print(answer)
