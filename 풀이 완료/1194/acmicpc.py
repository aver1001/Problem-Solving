import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []


def printBoard():
    for i in board:
        print(i)
    print()


for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))

for y in range(Y):
    for x in range(X):
        if board[y][x] == '0':
            startPoint = (y, x)
            board[y][x] = '.'
            break

'''
열쇠 가능한 경우 'a', 'b', 'c', 'd', 'e', 'f'
'''

keys = {'a': 1,
        'b': 1 << 1,
        'c': 1 << 2,
        'd': 1 << 3,
        'e': 1 << 4,
        'f': 1 << 5}

table = {}

for i in range(1 << 6):
    table[i] = [[10000]*X for _ in range(Y)]
queue = deque([(*startPoint, 0, 0)])

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while queue:
    y, x, cnt, key = queue.popleft()
    for idx in range(4):
        ty = y+dy[idx]
        tx = x+dx[idx]

        if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] != '#':

            if board[ty][tx] == '1':
                print(cnt+1)
                exit()

            if board[ty][tx] == '.':
                if table[key][ty][tx] > cnt+1:
                    table[key][ty][tx] = cnt + 1
                    queue.append((ty, tx, cnt+1, key))
                continue

            #대문자일경우 == 문
            if board[ty][tx].isupper():
                if key & keys[board[ty][tx].lower()]:
                    if table[key][ty][tx] > cnt + 1:
                        table[key][ty][tx] = cnt + 1
                        queue.append((ty, tx, cnt+1, key))
                # 열쇠일 경우
            else:
                tempKey = key | keys[board[ty][tx]]
                if table[tempKey][ty][tx] > cnt + 1:
                    table[tempKey][ty][tx] = cnt + 1
                    queue.append((ty, tx, cnt+1, tempKey))

print(-1)
