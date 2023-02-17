import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")
'''
4X4 크기의 공간이 있음.
한 칸에는 물고기 한마리가 존재하고, 각 물고기는 번호(1~16)와 방향(8가지)을 가지고있음.

청소년 상어가 이 공간에 들어가 물고기를 먹으력 함.
청소년 상어는 0,0 에 있는 물고기를 먹고, 0,0에 들어간다. 상어의 방향은 0,0 에 있던 물고기의 방향과 같다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다.
물고기는 한칸을 이동할 수 있음
이동할 수 있는 칸 == 빈칸, 다른물고기가 있는 칸
이동할 수 없는 칸 == 상어가 있거나 공간의 경계를 넘는 칸.

각 물고기는 방향이 이동할 수 있는 칸을 향할때까지 45도씩 반시계방향으로 회전함.
이동할 수 없으면 이동 안함.

물고기가 다른 물고기가 있는 방향으로 이동하는 경우 서로의 위치를 바꾸는 방식으로 이동함.

물고기의 이동이 모두 끝나면 상어가 이동.
상어는 방향에 있는 칸으로 이동할 수 있는대 한번에 여러칸을 이동할 수 있음.
상어가 물고기가 있는 방향으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 갖게 됨.
이동하는중에 지나가는ㄴ 칸에 잇는 물고기는 먹지 않음.
물고기가 없는 칸으로 이동할 수 없음.
상어가 이동할 수 있는 칸이 없다면 집으로 감.
상어 이동후 물고기가 이동함.

'''


def printBoard():
    # board 확인용 함수
    for i in board:
        print(i)
    print()


direction = {
    # y,x
    0: (-1, 0, '↑'),
    1: (-1, -1, '↖'),
    2: (0, -1, '←'),
    3: (1, -1, '↙'),
    4: (1, 0, '↓'),
    5: (1, 1, '↘'),
    6: (0, 1, '→'),
    7: (-1, 1, '↗'),
}


def sharkEat(y, x, hap, board):
    print(hap, '에서', board[y][x][0], '먹은뒤', hap + board[y][x][0])
    shark = [y, x, hap + board[y][x][0], board[y][x][1]]  # y,x,번호의 합,방향
    board[y][x] = [-1, 0]

    return shark


def rangeCheck(y, x):
    if 0 <= y < 4 and 0 <= x < 4:
        return True
    return False


def findFish(num):
    for y in range(4):
        for x in range(4):
            if board[y][x][0] == num:
                return y, x

    return -1, -1


def moveFish(board, shark):
    sy, sx = shark[0], shark[1]

    for idx in range(1, 17):
        # 1번 물고기부터 위치 가져옴
        y, x = findFish(idx)
        # 물고기가 없을경우 다음물고기 고고
        if y == -1:
            continue

        fishDirect = board[y][x][1]

        # 반시계로 돌면서 가능한지 파악.
        for add in range(8):
            tidx = (fishDirect + add) % 8
            # print(direction[tidx][2])
            ty = y + direction[tidx][0]
            tx = x + direction[tidx][1]

            if rangeCheck(ty, tx) and (board[ty][tx][0] != -1):
                if ty != sy or tx != sx:
                    continue
                # 위치 변경
                board[ty][tx], board[y][x] = board[y][x], board[ty][tx]
                break
        # printBoard()


def moveShark(shark, board, cnt):
    '''
    상어는 방향에 있는 칸으로 이동할 수 있는대 한번에 여러칸을 이동할 수 있음.
    상어가 물고기가 있는 방향으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 갖게 됨.
    이동하는중에 지나가는ㄴ 칸에 잇는 물고기는 먹지 않음.
    물고기가 없는 칸으로 이동할 수 없음.
    상어가 이동할 수 있는 칸이 없다면 집으로 감.
    상어 이동후 물고기가 이동함.
    '''

    hapList = [shark[2]]
    y, x, hap, d = shark[0], shark[1], shark[2], shark[3]

    # 이동가능 거리는 1~3이기 떄문에 다 움직여 봐야함.
    for i in range(1, 4):
        ty = y + direction[d][0]*i
        tx = x + direction[d][1]*i

        #  범위 안에 들어가고, 물고기가 있을경우
        if rangeCheck(ty, tx) and board[ty][tx][0] > 0:
            # 물고기를 먹고 물고기의 방향을 갖게 됨. 재귀적으로 다시 고고
            nextBoard = deepcopy(board)
            nextShark = sharkEat(ty, tx, hap, nextBoard)
            moveFish(nextBoard, nextShark)

            hapList.append(moveShark(nextShark, deepcopy(nextBoard), cnt+1))

    return max(hapList)


answer = 0
fish = {i: () for i in range(1, 17)}
board = []

for y in range(4):
    ttemp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    temp = []
    for idx in range(0, 8, 2):
        temp.append([ttemp[idx], ttemp[idx+1]-1])
        fish[ttemp[idx]] = (y, idx//2)
    board.append(temp)

shark = sharkEat(0, 0, 0, board)
moveFish(board, shark)
print(shark[:2], shark[2], direction[shark[3]][2])
print(moveShark(shark, board, 0))
