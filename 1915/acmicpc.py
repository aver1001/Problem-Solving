import sys
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())

board = []
answer = 0
for _ in range(Y):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

for x in range(X):
    for y in range(Y):
        if y > 0 and x > 0 and board[y][x] == 1:
            board[y][x] += min(board[y-1][x-1], board[y-1][x], board[y][x-1])
        answer = max(board[y][x], answer)

print(answer*answer)
