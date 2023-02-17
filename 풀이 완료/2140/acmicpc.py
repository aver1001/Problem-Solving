import sys
sys.stdin = open('input.txt', "r")


N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

dx = (-1, 0, 1, -1, 1, -1, 0, 1)
dy = (-1, -1, -1, 0, 0, 1, 1, 1)


def check(y, x):

    dontKnow = set()
    isBomb = set()
    isSafe = set()
    for idx in range(8):
        ty = y+dy[idx]
        tx = x+dx[idx]

        if 1 <= ty < N-1 and 1 <= tx < N-1:
            if board[ty][tx] == '#':
                dontKnow.add((ty, tx))
            elif board[ty][tx] == 'O':
                isBomb.add((ty, tx))
            elif board[ty][tx] == 'X':
                isSafe.add((ty, tx))

    # 모르는게 다 폭탄일경우
    if len(dontKnow) == int(board[y][x])-len(isBomb):
        for ty, tx in dontKnow:
            if board[ty][tx] != 'O':
                board[ty][tx] = 'O'
    # 폭탄이 다확인되었을경우 모르는건 다 안전함
    if len(isBomb) == int(board[y][x]):
        for ty, tx in dontKnow:
            if board[ty][tx] != 'X':
                board[ty][tx] = 'X'


def cntResult():
    cnt = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] in ['O', '#']:
                cnt += 1

    return cnt


cnt = 0
for y in range(N):
    for x in range(N):
        # 가쪽이면
        if y == 0 or y == N-1 or x == 0 or x == N-1:
            check(y, x)

print(cntResult())
