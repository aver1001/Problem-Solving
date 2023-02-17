import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))


def findLoc(str):
    for y in range(Y):
        for x in range(X):
            if board[y][x] == str:
                return (y, x)


def MoveGlass(ry, rx, by, bx, direction):

    if direction == 'L':
        # blue 먼져 움직이기
        if rx >= bx:
            while True:
                if board[by][bx-1] == '.':
                    bx -= 1
                elif board[by][bx-1] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break

            while True:
                if board[ry][rx-1] == '.':
                    rx -= 1
                elif board[ry][rx-1] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break

        # red 먼져 움직이기
        else:
            while True:
                if board[ry][rx-1] == '.':
                    rx -= 1
                elif board[ry][rx-1] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
            while True:

                if board[by][bx-1] == '.':
                    bx -= 1
                elif board[by][bx-1] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
            print(bx)
    elif direction == 'R':
        # red 먼져 움직이기
        if rx >= bx:
            while True:
                if board[ry][rx+1] == '.':
                    rx += 1
                elif board[ry][rx+1] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
            while True:
                if board[by][bx+1] == '.':
                    bx += 1
                elif board[by][bx+1] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
        # blue 먼져 움직이기
        else:
            while True:
                if board[by][bx+1] == '.':
                    bx += 1
                elif board[by][bx+1] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
            while True:
                if board[ry][rx+1] == '.':
                    rx += 1
                elif board[ry][rx+1] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
    elif direction == 'U':
        # blue 먼져 움직이기
        if ry >= by:
            while True:
                if board[by-1][bx] == '.':
                    by -= 1
                elif board[by-1][bx] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
            while True:
                if board[ry-1][rx] == '.':
                    ry -= 1
                elif board[ry-1][rx] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
        # red 먼저 움직이기
        else:
            while True:
                if board[ry-1][rx] == '.':
                    ry -= 1
                elif board[ry-1][rx] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
            while True:
                if board[by-1][bx] == '.':
                    by -= 1
                elif board[by-1][bx] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
    elif direction == 'D':
        # RED 먼저 움직이기
        if ry >= by:
            while True:
                if board[ry+1][rx] == '.':
                    ry += 1
                elif board[ry+1][rx] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break
            while True:
                if board[by+1][bx] == '.':
                    by += 1
                elif board[by+1][bx] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
        # blue 먼저 움직이기
        else:
            while True:
                if board[by+1][bx] == '.':
                    by += 1
                elif board[by+1][bx] == 'O':
                    by, bx = -1, -1
                    break
                else:
                    board[by][bx] = 'B'
                    break
            while True:
                if board[ry+1][rx] == '.':
                    ry += 1
                elif board[ry+1][rx] == 'O':
                    ry, rx = -1, -1
                    break
                else:
                    board[ry][rx] = 'R'
                    break

    return ry, rx, by, bx


check = set()
redPoint = findLoc('R')
bluePoint = findLoc('B')
board[redPoint[0]][redPoint[1]] = '.'
board[bluePoint[0]][bluePoint[1]] = '.'
queue = deque([(*redPoint, *bluePoint, 0)])
# table = {(y1,x1,y2,x2):cnt1}
while queue:
    ry, rx, by, bx, cnt = queue.popleft()

    for direct in ['L', 'R', 'U', 'D']:
        board[ry][rx] = '.'
        board[by][bx] = '.'

        t_ry, t_rx, t_by, t_bx = MoveGlass(ry, rx, by, bx, direct)
        if t_by == -1:
            continue

        if t_ry == -1:
            print(direct, t_ry, t_rx, t_by, t_bx)
            # 빨간구슬만 탈출 성공
            print(cnt+1)
            exit()

        if (t_ry, t_rx, t_by, t_bx) in check:
            continue
        else:
            check.add((t_ry, t_rx, t_by, t_bx))
            queue.append((t_ry, t_rx, t_by, t_bx, cnt+1))


print(-1)
