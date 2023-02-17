import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())


def printBoard():
    for i in board:
        print(i)
    print()


def fireSpread(fireLoc):

    temp = set()
    for y, x in fireLoc:

        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ty = dy+y
            tx = dx+x

            if 0 <= ty < Y and 0 <= tx < X and (board[ty][tx] == '.' or type(board[ty][tx]) == int):
                temp.add((ty, tx))

    for y, x in temp:
        board[y][x] = '*'

    return temp


def move():
    global loc

    isMove = False
    temp = set()
    for y, x, cost in loc:
        if board[y][x] == '@':
            board[y][x] = 0

        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ty = dy+y
            tx = dx+x

            if tx == -1 or ty == -1 or tx == X or ty == Y:
                print(cost+1)
                return False

            if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] == '.':

                board[ty][tx] = cost+1
                temp.add((ty, tx, cost+1))
                isMove = True

    if isMove == False:
        print('IMPOSSIBLE')
        return False

    loc = temp

    return True


for _ in range(N):
    X, Y = map(int, sys.stdin.readline().rstrip().split())
    board = []
    for _ in range(Y):
        board.append(list(sys.stdin.readline().rstrip()))
    global loc
    fire = set()
    loc = set()

    for y in range(Y):
        for x in range(X):
            if board[y][x] == '*':
                fire.add((y, x))
            elif board[y][x] == '@':
                loc.add((y, x, 0))
    state = True
    while state:
        fire = fireSpread(fire)
        state = move()
