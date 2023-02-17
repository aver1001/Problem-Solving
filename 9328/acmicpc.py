import sys
from collections import deque
sys.stdin = open('input.txt', "r")


def printBoard():
    for i in check:
        print(i)
    print()


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

    board = []
    for _ in range(Y):
        board.append(list(sys.stdin.readline().rstrip()))

    check = [[0]*X for _ in range(Y)]

    key = set(sys.stdin.readline().rstrip())

    if '0' in key:
        key = set()
    queue = deque([])

    answer = 0

    for y in range(Y):
        for x in range(X):
            if (y == 0 or y == Y-1 or x == 0 or x == X-1) and (board[y][x] != '*'):

                if board[y][x].islower():
                    key.add(board[y][x])
                    queue.append((y, x))
                elif board[y][x].isupper():
                    queue.append((y, x))

                elif board[y][x] == '$':
                    board[y][x] = '.'
                    check[y][x] = 3
                    answer += 1
                    queue.append((y, x))
                else:
                    queue.append((y, x))

    while True:
        isPorsess = False
        wait = deque([])
        while queue:
            y, x = queue.popleft()

            if board[y][x].isupper():
                if board[y][x].lower() not in key:
                    wait.append((y, x))
                    continue

            for idx in range(4):
                ty = y+dy[idx]
                tx = x+dx[idx]

                if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] != '*' and check[ty][tx] == 0:

                    #대문자 == 문일경우
                    if board[ty][tx].isupper():
                        # 열쇠가 있어서 들어갈 수 있을 경우
                        if board[ty][tx].lower() in key:
                            isPorsess = True
                            check[ty][tx] = 1
                            queue.append((ty, tx))
                        # 열쇠가 없어서 지금은 들어갈 수 없을 경우
                        else:
                            wait.append((ty, tx))
                    # 소문자 == 열쇠일 경우
                    elif board[ty][tx].islower():
                        isPorsess = True
                        key.add(board[ty][tx])
                        check[ty][tx] = 1
                        queue.append((ty, tx))
                    # 문서일 경우
                    elif board[ty][tx] == '$':
                        answer += 1
                        check[ty][tx] = 3
                        board[ty][tx] == '.'
                        queue.append((ty, tx))

                    else:
                        isPorsess = True
                        check[ty][tx] = 1
                        queue.append((ty, tx))

        if isPorsess == False:
            break
        else:
            queue = wait

    print(answer)

'''
1. 갈 수 있는 곳 다 탐사.
2. 열쇠로 열 수 없는 경우 따로 넣어놓고 얻은 열쇠로 다시 1번 시작
'''
