import re
import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

table = []
for _ in range(Y):
    table.append(list(sys.stdin.readline().rstrip().split(' ')))

canBulidList = []
virus = []

# 바이러스, 빈곳 저장
for y in range(Y):
    for x in range(X):
        if table[y][x] == '0':
            canBulidList.append((y, x))
        elif table[y][x] == '2':
            virus.append((y, x))


def printTable():
    for i in table:
        print(i)
    print()


def buildWall(canBuildList):
    Max = 0
    for build in combinations(canBuildList, 3):
        # 벽 3개 지어주고
        for y, x in build:
            table[y][x] = '1'
        # 바이러스 퍼져나간뒤 안전지대크기 업데이트
        Max = max(Max, spreadVirus())
        # 벽 3개 원래대로
        for y, x in build:
            table[y][x] = '0'

    return Max


def spreadVirus():
    nowVirus = virus.copy()
    sVirus = set()
    while nowVirus:

        y, x = nowVirus.pop()

        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ty = y+dy
            tx = x+dx
            if 0 <= ty < Y and 0 <= tx < X and table[ty][tx] == '0' and (ty, tx) not in sVirus:
                sVirus.add((ty, tx))
                nowVirus.append((ty, tx))

    # 빈곳 - 지을수 있는 벽(3) - 새로 퍼진 바이러스 = 안전지대
    return len(canBulidList) - 3 - len(sVirus)


print(buildWall(canBulidList))
