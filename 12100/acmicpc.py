import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

# DOWN


def down(board):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

# LEFT


def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer] = tmp
    return board

# RIGHT


def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board


def printBoard():
    for i in board:
        print(i)
    print()


def findMax(board):
    answer = 0
    for y in range(n):
        for x in range(n):
            answer = max(board[y][x], answer)

    return answer


def DFS(cnt, board):
    global answer
    # 초기 cnt = 0
    if cnt == 5:
        answer = max(answer, findMax(board))
    else:
        DFS(cnt + 1, up(deepcopy(board)))
        DFS(cnt + 1, down(deepcopy(board)))
        DFS(cnt + 1, left(deepcopy(board)))
        DFS(cnt + 1, right(deepcopy(board)))


global answer
answer = 0

DFS(0, board)
print(answer)
