import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
board = []
sitBoard = [[0]*N for _ in range(N)]
favoriteTable = {}


def bestSit():
    sitArray = []
    for y in range(N):
        for x in range(N):
            if sitBoard[y][x] != 0:
                continue
            friendCnt = 0
            zeroCnt = 0
            # 상하좌우 친구들 확인
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ty = y + dy
                tx = x + dx
                # 범위체크

                if 0 <= ty < N and 0 <= tx < N:
                    # 좋아하는 친구 몇 있는지 확인
                    if sitBoard[ty][tx] in favorite:
                        friendCnt += 1
                    if sitBoard[ty][tx] == 0:
                        zeroCnt += 1
            # 자리의 대한 정보를 정리해서 넣어둔다. 후에 정렬을위해 순서 맞춰서 넣어줬음.
            sitArray.append([friendCnt, zeroCnt, y, x])

    # 문제 조건에 맞게 정렬해주고
    sitArray.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # 가장 best 자리의 앉혀줌
    sitBoard[sitArray[0][2]][sitArray[0][3]] = me


def calScore():
    score = 0
    for y in range(N):
        for x in range(N):
            cnt = 0
            for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                ty = dy + y
                tx = dx + x

                if 0 <= ty < N and 0 <= tx < N and sitBoard[ty][tx] in favoriteTable[sitBoard[y][x]]:
                    cnt += 1

            if cnt == 0:
                score += 0
            elif cnt == 1:
                score += 1
            elif cnt == 2:
                score += 10
            elif cnt == 3:
                score += 100
            elif cnt == 4:
                score += 1000
    print(score)


def printBoard():
    for i in sitBoard:
        print(i)
    print()


for _ in range(N**2):
    me, a, b, c, d = map(int, sys.stdin.readline().rstrip().split(' '))
    favorite = {a, b, c, d}
    favoriteTable[me] = {a, b, c, d}
    bestSit()

calScore()
