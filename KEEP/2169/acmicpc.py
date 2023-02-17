import sys
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def printBoard(board):
    for i in board:
        print(i)
    print()


DP = [[[0]*X for _ in range(Y)] for _ in range(3)]

# DP[0] 메인, DP[1] 왼=>오, DP[2] 오 => 왼

for y in range(Y):
    if y == 0:
        for x in range(X):
            if x == 0:
                DP[0][y][x] = board[y][x]
            else:
                DP[0][y][x] = DP[0][y][x-1] + board[y][x]
        continue

    # 왼 => 오
    for x in range(X):
        if x == 0:
            DP[1][y][x] = DP[0][y-1][x]+board[y][x]
        else:
            DP[1][y][x] = max(DP[0][y-1][x]+board[y][x],
                              DP[1][y][x-1]+board[y][x])

    # 오 => 왼
    for x in range(X-1, -1, -1):
        if X-1 == x:
            DP[2][y][x] = DP[0][y-1][x] + board[y][x]
        else:
            DP[2][y][x] = max(DP[0][y-1][x] + board[y][x],
                              DP[2][y][x+1]+board[y][x])

    # 최대값 갱신
    for x in range(X):
        DP[0][y][x] = max(DP[1][y][x], DP[2][y][x])

    # printBoard(DP[0])
print(DP[0][-1][-1])
