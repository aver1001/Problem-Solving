import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(N):
    board.append(
        list(map(int, list(sys.stdin.readline().rstrip().split(' ')))))

S, Y, X = map(int, sys.stdin.readline().rstrip().split(' '))
Y -= 1
X -= 1

table = {}
for y in range(N):
    for x in range(N):
        if board[y][x] == 0:
            continue

        if board[y][x] in table:
            table[board[y][x]].add((y, x))
        else:
            table[board[y][x]] = {(y, x)}


def pboard():
    for i in board:
        print(i)
    print()


def spread(y, x):
    global temp

    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ty = dy+y
        tx = dx+x

        if 0 <= ty < N and 0 <= tx < N and board[ty][tx] == 0:
            board[ty][tx] = board[y][x]
            temp.add((ty, tx))


if board[Y][X] != 0:
    print(board[Y][X])
    exit()

for _ in range(S):
    global temp

    for virus in range(1, K+1):
        temp = set()
        if table.get(virus):
            for y, x in table[virus]:
                spread(y, x)
            table[virus].update(temp)
        else:
            continue

    if board[Y][X] != 0:
        print(board[Y][X])
        exit()

print(0)
