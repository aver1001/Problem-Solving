import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
빙산의 높이정보가 저장됨
0은 바다
'''
Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

# 무식하게 구현해보자
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def meltIce():
    melt = set()
    for y in range(Y):
        for x in range(X):
            # 만약 얼음이라면
            if board[y][x] != 0:

                cnt = 0
                # 4방향 확인해주며
                for idx in range(4):
                    ty = y+dy[idx]
                    tx = x+dx[idx]
                    # 범위확인 + 바다인지 확인해주고
                    if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] == 0:
                        # 바다라면 카운팅
                        cnt += 1
                # 얼음이 녹았을지 판단후 녹았다면
                if board[y][x] <= cnt:
                    # 녹은얼음에 추가
                    melt.add((y, x))
                # 녹지는 않았다면
                else:
                    # 얼음양 줄여줌
                    board[y][x] -= cnt

    # 다 순회한뒤 녹은 얼음 보드에 업데이트해줌

    for y, x in melt:
        board[y][x] = 0


def printBoard():
    for i in board:
        print(i)
    print()


def countArea():
    check = [[0]*X for _ in range(Y)]
    cnt = 1
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 0:
                continue
            if check[y][x] == 0:
                check[y][x] = cnt
                queue = deque([[y, x]])
                while queue:
                    y, x = queue.pop()
                    for idx in range(4):
                        ty = y+dy[idx]
                        tx = x+dx[idx]
                        # 범위확인 + 바다아닌거 확인
                        if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] != 0 and check[ty][tx] == 0:
                            check[ty][tx] = cnt
                            queue.append([ty, tx])

                cnt += 1
    return(cnt-1)


answer = 0
while True:
    meltIce()
    answer += 1

    island = countArea()
    if island >= 2:
        print(answer)
        exit()

    elif island == 0:
        print(0)
        exit()
