import sys
sys.stdin = open('input.txt', "r")


def printBoard():
    for i in board:
        print(i)
    print()


dricet = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}


def blizard(dirtect, distance):
    y, x = N//2, N//2
    addy, addx = dricet[dirtect]
    for _ in range(distance):
        y += addy
        x += addx
        board[y][x] = 0


def visit():
    y, x = N//2, N//2
    mid = N//2

    limit = 1
    d = {
        1: (0, -1),
        2: (1, 0),
        3: (0, 1),
        4: (-1, 0)
    }

    loc = []

    while limit <= N//2:
        direct = 1
        for _ in range(4):
            while True:
                # 범위안에 들어올경우
                if mid-limit <= y+d[direct][0] <= mid+limit and mid-limit <= x+d[direct][1] <= mid+limit:
                    y += d[direct][0]
                    x += d[direct][1]
                    loc.append((y, x))
                else:
                    break
            direct += 1
        limit += 1
    while x != 0:
        x -= 1
        loc.append((y, x))
    return loc


def glassMove():

    for start in range(len(loc)-1):
        for idx in range(start, len(loc)-1):
            ay, ax = loc[idx+1]
            by, bx = loc[idx]

            if board[by][bx] == 0:
                board[by][bx], board[ay][ax] = board[ay][ax], board[by][bx]


def glassBomb():

    isBomb = False

    before = -1
    temp = []
    for y, x in loc:
        # 이전거랑 다르다면
        if board[y][x] == 0:
            continue
        if board[y][x] != before:
            # 누적이 4개가 넘는다면
            if len(temp) >= 4:
                # 파괴
                isBomb = True
                for ty, tx in temp:
                    board[ty][tx] = 0
            temp = [(y, x)]
            before = board[y][x]
        # 이전거랑 같다면
        else:
            temp.append((y, x))
    return isBomb


N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
skill = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
for _ in range(M):
    D, S = map(int, sys.stdin.readline().rstrip().split())
    skill.append((D, S))


loc = visit()
printBoard()
blizard(2, 2)
printBoard()
glassMove()
printBoard()
glassBomb()
printBoard()
glassMove()
printBoard()
'''
만들어야 하는 함수
1. 블리자드
    1,2,3,4 => 상하좌우
    방향, 거리 이용해서 구슬 파괴
2. 구슬 빈칸없이 옮기기
3. 구슬 폭파
    4개이상 연속하는 구슬이 있을때 그 구슬을 파괴
4. 구슬 변화
    연속되는 구슬을 그룹으로 잡고
    구슬을 (그룹의 구슬의 개수, 그룹을 이루고 있는 구슬의 번호) 로 변경해준다.
'''
