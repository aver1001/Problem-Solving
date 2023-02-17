import sys
from collections import deque

sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


answer = 0
for y in range(Y):

    x = 0
    isClean = False

    while True:
        for i in range(x, X):
            if board[y][i] == 1:
                board[y][i] = 0
                isClean = True
                x = i
                continue
        else:
            y += 1

        if y == Y:
            break

    if isClean:
        answer += 1
print(answer)
