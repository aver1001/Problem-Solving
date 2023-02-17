import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X, T = map(int, sys.stdin.readline().rstrip().split(' '))
board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

dust = set()
airPurifier = []

for y in range(Y):
    for x in range(X):
        # -1일경우 공기청정기 위치를 넣어준다.
        # Y증가하는 순서이기때문에 공기청정기 [위에위치,아래위치] 저장될것임
        if board[y][x] == -1:
            airPurifier.append([y, x])
        elif board == 0:
            continue
        else:
            dust.add((y, x))

# T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력해주세요

# 미세먼지 체크 후 한번에 더해줘야 정확한 값을 알 수 있음.
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def spread():
    # 추가된 미세먼지는 마지막에 다 더해줄것이기 때문에
    # 배열하나 선언해놓기
    addList = []
    # 먼지가 있는곳을 순회하면서
    for y, x in dust:
        temp = []
        # 상하좌우 미세먼지 확산이 가능한지 확인해본다
        for idx in range(4):
            tx = x+dx[idx]
            ty = y+dy[idx]
            if isMove(ty, tx):
                temp.append((ty, tx))

        # 확산되는 먼지의 양
        spreadDust = board[y][x]//5
        # 퍼지는 만큼 자신의 먼지량을 줄여주고
        board[y][x] -= spreadDust * len(temp)
        for ty, tx in temp:
            # [yPos xPos 먼지의 양]으로 더해줌
            addList.append((ty, tx, spreadDust))
            # 먼지들 위치 업데이트
            dust.add((y, x))

    # 다 확인이 끝났으므로 더해줄 먼지들을 더해주자
    for y, x, spreadDust in addList:
        board[y][x] += spreadDust


def isMove(y, x):

    # 범위안에 들어가고, 공기청정기의 위치가 아닐경우
    if 0 <= y < Y and 0 <= x < X and board[y][x] != -1:
        # 움직이기 가능
        return True
    else:
        # 움직이기 불가능
        return False


def returnAnswer():
    answer = 0
    for i in board:
        for a in i:
            if a != -1:
                answer += a
    return answer


def upClean():
    up_step = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    direct = 0

    y, x = airPurifier[0]
    x += 1
    prev = 0
    while True:
        ty, tx = y + up_step[direct][0], x + up_step[direct][1]

        if [y, x] == airPurifier[0]:
            break
        if 0 <= ty < Y and 0 <= tx < X:
            board[y][x], prev = prev, board[y][x]
            y, x = ty, tx
        else:
            direct += 1
    return


def downClean():
    up_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direct = 0

    y, x = airPurifier[1]
    x += 1
    prev = 0
    while True:
        ty, tx = y + up_step[direct][0], x + up_step[direct][1]

        if [y, x] == airPurifier[1]:
            break
        if 0 <= ty < Y and 0 <= tx < X:
            board[y][x], prev = prev, board[y][x]
            y, x = ty, tx
        else:
            direct += 1
    return


for _ in range(T):
    spread()
    upClean()
    downClean()

print(returnAnswer())
