from itertools import combinations, permutations
from collections import deque
import sys
sys.stdin = open('input.txt', "r")
board = []


def printBoard():
    for i in board:
        print(i)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def isPossible(pos):

    check = [[0]*5 for _ in range(5)]

    queue = deque([pos[0]])

    cnt = 0
    while queue:
        y, x = queue.popleft()

        for idx in range(4):
            ty = y+dy[idx]
            tx = x+dx[idx]

            if (ty, tx) in pos and check[ty][tx] == 0:
                cnt += 1
                check[ty][tx] = 1
                queue.append((ty, tx))
    if cnt == len(pos):
        return True
    else:
        return False


starPoint = []

for _ in range(5):
    board.append(list(sys.stdin.readline().rstrip()))

for y in range(5):
    for x in range(5):
        if board[y][x] == '*':
            starPoint.append([y, x])

N = len(starPoint)

temp = []
for y in range(5):
    for x in range(5):
        temp.append((y, x))

comb = list(combinations(temp, N))
per = list(permutations(range(N), N))
answer = 100
for c in comb:

    if isPossible(c):

        temp = 100
        for p in per:
            hap = 0
            for idx in range(N):
                hap += abs(c[p[idx]][0] - starPoint[idx][0]) + \
                    abs(c[p[idx]][1] - starPoint[idx][1])
            temp = min(temp, hap)

        answer = min(answer, temp)

if answer == 100:
    print(0)
else:
    print(answer)
