from audioop import findmax
from gettext import find
import sys
sys.stdin = open('input.txt', "r")

board = []
for _ in range(10):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def updateCheck():
    check = [[0]*10 for _ in range(10)]
    for y in range(10):
        for x in range(10):
            if board[y][x] == 1:
                check[y][x] = min(check[y-1][x], check[y]
                                  [x-1], check[y-1][x-1])+1
    return check


def findMaxLoc():
    Max = 0
    loc = [-1, -1]
    for y in range(10):
        for x in range(10):
            if check[y][x] > Max:
                Max = check[y][x]
                loc[0] = y
                loc[1] = x
                if Max == 5:
                    return True, loc

    if loc[0] == -1:
        return False, loc
    else:
        return True, loc


def patchPaper(loc):
    y, x = loc[0], loc[1]
    size = check[y][x]

    if paper[size] > 0:
        paper[size] -= 1

        for ty in range(y, y-size, -1):
            for tx in range(x, x-size, -1):
                check[ty][tx] = 0
                board[ty][tx] = 0

        return True
    else:
        return False


def prinrCheck():
    for i in check:
        print(i)
    print()


paper = [0, 5, 5, 5, 5, 5]
answer = 0
while True:
    check = updateCheck()

    state, loc = findMaxLoc()
    # 더이상 붙일게 없다면 그만
    if state == False:
        break

    if patchPaper(loc):
        answer += 1
    else:
        print(-1)
        exit()

print(answer)
