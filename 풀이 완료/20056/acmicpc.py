import sys
import math
sys.stdin = open('input.txt', "r")

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))
'''
1. 모든 파이어볼은 자신의 방향 d로 속력 s칸만큼 이동한다

2. 이동이 모두 끝난뒤 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일들이 발생한다
    - 같은 칸에 있는 파이어볼은 모두 합쳐진다.
    - 파이어볼은 4개로 나누어진다
    - 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        - 질량 == 합쳐진 파이어볼의 질량의 합 / 5
        - 속력 == 합쳐진 파이어볼의 속력의 합 / 합쳐진 파이어볼의 개수
        - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 0,2,4,6
            아니라면 1,3,5,7
        - 질량이 0인 파이어볼은 소멸되어 사라진다
'''

direction = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1)}

board = [[[] for _ in range(N)]for _ in range(N)]
for _ in range(M):
    # y,x   => 파이어볼의 위치
    # m     => 파이어볼의 질량
    # s     => 파이어볼의 속력
    # d     => 파이어볼의 방향

    y, x, m, s, d = map(int, sys.stdin.readline().rstrip().split(' '))
    y -= 1
    x -= 1
    board[y][x].append([m, s, d])


def moveFireBall():

    afterFireBall = []
    # 모든 칸을 확인하면서
    for y in range(N):
        for x in range(N):
            # 칸에 파이어볼이 있을경우
            if board[y][x]:
                # 파이어볼을 순회하며
                for m, s, d in board[y][x]:

                    dy, dx = direction[d]
                    # 다음 도착할 위치를 구해준다
                    ty = (y+dy*s) % N
                    tx = (x+dx*s) % N

                    # print(y, x, m, s, d)
                    # print(ty, tx, m, s, d)
                    # print()
                    # 후에 추가해줘야 오류가 없기떄문에 정보를 따로 저장해둔다
                    afterFireBall.append([ty, tx, m, s, d])
                board[y][x] = []
    for y, x, m, s, d in afterFireBall:
        board[y][x].append([m, s, d])


def mixFireBall():
    for y in range(N):
        for x in range(N):
            lenFireball = len(board[y][x])
            # 파이어볼이 2개 이상 있다면
            if lenFireball >= 2:
                hapM = 0
                hapS = 0
                calD = 0
                # 합들과 방향을 구해준뒤
                for m, s, d in board[y][x]:
                    hapM += m
                    hapS += s
                    calD += d % 2
                # 비어주고
                board[y][x] = []
                if hapS == 0:
                    continue
                # 분해해서 넣어준다
                if calD == 0 or calD == lenFireball:
                    for i in [0, 2, 4, 6]:
                        board[y][x].append(
                            [math.floor(hapM/5), math.floor(hapS/lenFireball), i])
                else:
                    for i in [1, 3, 5, 7]:
                        board[y][x].append(
                            [math.floor(hapM/5), math.floor(hapS/lenFireball), i])


def allFireBallWeight():
    answer = 0
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                for m, s, d in board[y][x]:
                    answer += m
    print(answer)


def printBoard():
    for i in board:
        print(i)
    print()


for _ in range(K):
    moveFireBall()
    printBoard()
    mixFireBall()
    printBoard()
allFireBallWeight()
