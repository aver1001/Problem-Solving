import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))

'''
. 비어있는곳
* 물이 차있는곳
X 돌
D 비버의 굴
S 고슴도치의 위치

매분마다 고슴도치는 4방향으로이동
물은 매분 4방향으로 퍼짐 빈칸으로만 이동
물과 고슴도치는 돌을 통과할 수 없음
고슴도치는 물이 차있는 구역으로 이동할 수 없음
물은 비버의 소굴로 이동할 수 없음

고슴도치는 물이 찰 예정인 칸으로 이동할 수없다 => 물 먼져 이동시키면 됨
'''

# 보드 관리하기 힘드니 DFS로 시작함
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
global answer
answer = sys.maxsize


def waterMove():
    waterSpred = set()
    for y in range(Y):
        for x in range(X):
            if board[y][x] == '*':
                for idx in range(4):
                    ty = y+dy[idx]
                    tx = x+dx[idx]
                    # 범위안에 들어가고, 비어있는 곳 일경우
                    if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] == '.':
                        waterSpred.add((ty, tx))

    for y, x in waterSpred:
        board[y][x] = '*'


def printBoard():
    for i in board:
        print(i)
    print()


def BFS(y, x):
    check = [[False]*X for _ in range(Y)]
    queue = deque([[y, x, 0]])
    cnt = 0
    waterMove()
    while queue:
        y, x, tempcnt = queue.popleft()
        if cnt != tempcnt:
            waterMove()
        cnt = tempcnt

        for idx in range(4):
            tx = x + dx[idx]
            ty = y + dy[idx]

            if 0 <= ty < Y and 0 <= tx < X:
                if board[ty][tx] == '.':
                    if check[ty][tx] == False:
                        check[ty][tx] = True
                        queue.append([ty, tx, cnt+1])
                elif board[ty][tx] == 'D':
                    print(cnt+1)
                    exit()
    print('KAKTUS')
    exit()


def findDochi():
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 'S':
                return y, x


BFS(*findDochi())
