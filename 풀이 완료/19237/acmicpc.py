from re import L
import sys
sys.stdin = open('input.txt', "r")
'''
1~M 번호의 상어가 존재
1이 가장 강함.
N*N 크기에 상어가 한마리씩 들어가 있음.

모든상어가 자신의 위치의 자신의 냄새를 뿌림.

1초마다
모든상어가 이동
자신의 냄새를 뿌림
냄새는 K번 이동하면 사라짐.

상어의 이동방향은
1. 인접한칸중 아무 냄새가 없는 칸으로 방향을 잡음.
2. 자신의 냄새가 있는 칸으로 방향을 잡음.
3. 가능한 칸이 여러개일 경우 특정한 우선순위를 따름.
4. 우선순위는 상어마다 다름

모든상어가 이동한 후 한칸에 여러마리 상어가 남아 있으면
가장적은 번호를 갖은 상어를 제외하고 모두 격자밖으로 쫒겨남.

1번 상어만 남게 되기까지 몇 초가 걸리는지 구하는 프로그램을 작성하라.
'''
N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

sharkNowDirect = {}
for idx, direct in enumerate(list(map(int, sys.stdin.readline().rstrip().split(' '))), start=1):
    sharkNowDirect[idx] = direct

sharkPriorityDirect = {}
for idx in range(1, M+1):
    sharkPriorityDirect[idx] = {}
    for j in range(1, 5):
        sharkPriorityDirect[idx][j] = list(
            map(int, sys.stdin.readline().rstrip().split(' ')))

direct = {
    1: (-1, 0, '↑'),
    2: (1, 0, '↓'),
    3: (0, -1, '←'),
    4: (0, 1, '→')
}

sharkNowLoc = {}
for y in range(N):
    for x in range(N):
        if board[y][x] != 0:
            sharkNowLoc[board[y][x]] = (y, x)
            board[y][x] = [board[y][x], K]
        else:
            board[y][x] = [0, 0]


def printBoard():
    for i in board:
        print(i)
    print()


def rangeCheck(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    else:
        return False


def allSharkMove():
    for idx in range(M+1):
        if idx in sharkNowDirect:
            oneSharkMove(idx)


def oneSharkMove(num):

    smell = []
    noSmell = []
    mySmell = []

    # 우선순위대로 4방향을 이동시킨다.
    for idx in sharkPriorityDirect[num][sharkNowDirect[num]]:
        dy, dx, _ = direct[idx]
        ty = sharkNowLoc[num][0] + dy
        tx = sharkNowLoc[num][1] + dx
        # 범위체크
        if rangeCheck(ty, tx):
            # 만약 냄새가 없다면
            if board[ty][tx][0] == 0:
                # 노냄새에 넣어줌
                noSmell.append((ty, tx, idx))
            # 내 냄새라면
            elif board[ty][tx][0] == num:
                mySmell.append((ty, tx, idx))

            # 나머지
            else:
                # 냄새에 넣어줌
                smell.append((ty, tx, idx))

    # 만약 냄새 없는곳이 있다면
    if len(noSmell) != 0:
        # 그곳으로 이동
        ty, tx, d = noSmell[0]
        sharkNowDirect[num] = d
        sharkNowLoc[num] = (ty, tx)
    elif len(mySmell) != 0:
        ty, tx, d = mySmell[0]
        sharkNowDirect[num] = d
        sharkNowLoc[num] = (ty, tx)
    # 없다면
    else:
        # 나머지 우선순위중 1등 이동
        ty, tx, d = smell[0]
        sharkNowDirect[num] = d
        sharkNowLoc[num] = (ty, tx)


def deleteSameLoc(sharkNowLoc):
    newLoc = {}
    for idx in range(1, M+1):

        if idx not in sharkNowLoc:
            continue

        y, x = sharkNowLoc[idx]
        if (y, x) not in newLoc:
            newLoc[(y, x)] = idx
        else:
            del sharkNowDirect[idx]

    # 초기화 해주고
    sharkNowLoc = {}
    for loc, num in newLoc.items():
        sharkNowLoc[num] = loc
    return sharkNowLoc


def subSmell():
    for y in range(N):
        for x in range(N):

            if board[y][x][1] != 0:
                board[y][x][1] -= 1

            if board[y][x][1] == 0:
                board[y][x][0] = 0


def spredSmell():

    for idx in range(1, M+1):
        if idx in sharkNowLoc:
            loc = sharkNowLoc[idx]
            y, x = loc
            board[y][x] = [idx, K]


cnt = 1
while cnt <= 1000:

    allSharkMove()
    subSmell()
    sharkNowLoc = deleteSameLoc(sharkNowLoc)
    spredSmell()

    if len(sharkNowLoc) == 1:
        print(cnt)
        exit()
    cnt += 1

print(-1)
