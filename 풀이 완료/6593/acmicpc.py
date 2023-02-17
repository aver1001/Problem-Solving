import sys
from collections import deque
sys.stdin = open('input.txt', "r")


while True:
    L, Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

    if L == 0:
        break
    board = []
    for _ in range(L):
        temp = []
        for _ in range(Y):
            temp.append(
                list(sys.stdin.readline().rstrip()))
        board.append(temp)
        sys.stdin.readline().rstrip()
    # floor, y, x

    for f in range(L):
        for y in range(Y):
            for x in range(X):
                if board[f][y][x] == 'S':
                    start = [f, y, x, 0]
                    break

    queue = deque([start])
    flag = False
    while queue:
        f, y, x, cnt = queue.popleft()
        if flag:
            break

        for df, dy, dx in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            tf = df + f
            ty = dy + y
            tx = dx + x

            if 0 <= tf < L and 0 <= ty < Y and 0 <= tx < X:
                if board[tf][ty][tx] == '.':
                    board[tf][ty][tx] = cnt+1
                    queue.append([tf, ty, tx, cnt+1])
                elif board[tf][ty][tx] == 'E':
                    print('Escaped in '+str(cnt+1)+' minute(s).')
                    flag = True
                    break
    if flag == False:
        print('Trapped!')
