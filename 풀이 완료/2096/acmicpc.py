import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
maxBoard = []
for _ in range(N):
    maxBoard.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

minBoard = deepcopy(maxBoard)
for y in range(1, N):
    for x in range(N):
        if x == 0:
            maxBoard[y][x] = max(maxBoard[y-1][x]+maxBoard[y][x],
                                 maxBoard[y-1][x+1]+maxBoard[y][x])

            minBoard[y][x] = min(minBoard[y-1][x]+minBoard[y][x],
                                 minBoard[y-1][x+1]+minBoard[y][x])
        elif x == N-1:
            maxBoard[y][x] = max(maxBoard[y-1][x]+maxBoard[y][x],
                                 maxBoard[y-1][x-1]+maxBoard[y][x])

            minBoard[y][x] = min(minBoard[y-1][x]+minBoard[y][x],
                                 minBoard[y-1][x-1]+minBoard[y][x])
        else:
            maxBoard[y][x] = max(maxBoard[y-1][x]+maxBoard[y][x], maxBoard[y-1]
                                 [x-1]+maxBoard[y][x], maxBoard[y-1][x+1]+maxBoard[y][x])

            minBoard[y][x] = min(minBoard[y-1][x]+minBoard[y][x], minBoard[y-1]
                                 [x-1]+minBoard[y][x], minBoard[y-1][x+1]+minBoard[y][x])


print(max(maxBoard[-1]), min(minBoard[-1]))
