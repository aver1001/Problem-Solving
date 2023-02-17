import sys
sys.stdin = open('input.txt', "r")
'''
턴 한번은 1번부터 K번 말까지 순서대로 이동시킨다.
이동시 말 위에 올려져 있는 것들은 같이 움직인다.

흰색칸
    그칸으로 이동, 이동하려는 칸에 말이 이미 있는 경우 가장 위에 올림.
빨간색칸
    이동한 후에 순서를 뒤집은뒤 올려놓는다.
파란색칸
    이동방향을 반대로하고 한칸 이동한다. 바꾼 방향도 파란색일경우 움직이지 않는다.
체스판을 벗어날경우 파란색과 같은 경우로 생각한다.
'''
direct = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

drectArrow = {
    1: '→',
    2: '←',
    3: '↑',
    4: '↓'
}

directChagne = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


def printBoard():
    for i in board:
        print(i)
    print()


def colorCheck(y, x):
    if 0 <= y < N and 0 <= x < N:
        if color[y][x] == 0:
            return 0
        elif color[y][x] == 1:
            return 1
        else:
            return 2
    else:
        return 2


def Red(y, x, d, idx):

    temp = popUpper(y, x, idx)

    # 이동할 좌표를 구해준다.
    ty = y + direct[d][0]
    tx = x + direct[d][1]
    for idx, d in temp:
        # 말 위치 확인용 업데이트 해주고
        horseLoc[idx] = (ty, tx, d)
        # 그 보드칸위로 역순대로 쌓아준다.
        board[ty][tx].append([idx, d])
    if len(board[ty][tx]) >= 4:
        return True


def White(y, x, d, idx):
    # 원래 좌표에서 뺼거 뺴준다.
    temp = popUpper(y, x, idx)

    # 이동할 좌표를 구해준다.
    ty = y + direct[d][0]
    tx = x + direct[d][1]
    for idx, d in temp[::-1]:
        # 말 위치 확인용 업데이트 해주고
        horseLoc[idx] = (ty, tx, d)
        # 그 보드칸위로 순서대로 쌓아준다.
        board[ty][tx].append([idx, d])

    if len(board[ty][tx]) >= 4:
        return True


def Blue(y, x, d, idx):
    # 일단 방향을 바꿔주자.
    d = directChagne[d]
    # 움직이는 방향 수정
    ty = y + direct[d][0]
    tx = x + direct[d][1]

    state = False

    nextColor = colorCheck(ty, tx)
    if nextColor == 0:
        state = White(y, x, d, idx)
    elif nextColor == 1:
        state = Red(y, x, d, idx)
    # 찾아가서 방향만 바꿔주자
    horseLoc[idx] = (horseLoc[idx][0], horseLoc[idx]
                     [1], directChagne[horseLoc[idx][2]])

    y, x, d = horseLoc[idx]
    for h in range(len(board[y][x])):
        if board[y][x][h][0] == idx:
            board[y][x][h][1] = directChagne[board[y][x][h][1]]
            break

    return state


def popUpper(y, x, idx):
    temp = []
    temp.append(board[y][x].pop())
    while temp[-1][0] != idx:
        temp.append(board[y][x].pop())

    return temp


def oneTurn():

    for idx in range(1, K+1):
        # 일단 1번부터 위치,방향을 가져온다.
        y, x, d = horseLoc[idx]
        # 이 위치의 idx번보다 위에 있는것들을 temp로 옮겨준다.
        nextColor = colorCheck(y+direct[d][0], x+direct[d][1])
        if nextColor == 0:
            # 흰색
            state = White(y, x, d, idx)
        elif nextColor == 1:
            # 빨간색
            state = Red(y, x, d, idx)
        else:
            state = Blue(y, x, d, idx)

        if state == True:
            return True
    return False


N, K = map(int, sys.stdin.readline().rstrip().split(' '))
color = []
for _ in range(N):
    color.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
board = [[[]for _ in range(N)] for _ in range(N)]
horseLoc = {}

for idx in range(1, K+1):
    y, x, d = map(int, sys.stdin.readline().rstrip().split(' '))
    horseLoc[idx] = (y-1, x-1, d)
    board[y-1][x-1].append([idx, d])


# 처음 체크
for y in range(N):
    for x in range(N):
        if len(board[y][x]) >= 4:
            print(1)
            exit()

cnt = 0
while cnt < 1000:
    cnt += 1
    if oneTurn():
        break

if cnt == 1000:
    print(-1)
else:
    print(cnt)
