from collections import deque
import sys
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

'''
검은색 -1, 무지개 0, 일반 = M가지 색상

블록 그룹은 연결된 블록의 집합.
1. 일반블록이 적어도 하나 있고, 모두 같은 색이여야함.
2. 검은색 블록은 포함되면 안됨.
3. 무지개 블록은 몇개가 있던 상관 없음.
4. 그룹의 블록 개수는 2개 이상여야 함
5. 모두 연결되어야 함
6. 그룹의 기준은 무지개 블록이 아닌 블록 중 1. 행이가장작고 2. 열이 가장작은것

오토플레이
    블록그룹이 존재하는 한 계속 반복
1. 가장 큰 블록 그룹을 찾음
    1. 무지개가 가장 많은것
    2. 기준 블록의 행이 가장 큰 것
    3. 열이 가장 큰 것
2. 1에서 찾은 블록 그룹의 모든 블록을 제거하고 B^2 점을 얻음
3. 격자에 중력이 작용
4. 격자가 90도 반시계로 회전
5. 다시 격자에 중력이 작용

중력 작용시 검은색 블록은 움직이지 않음.

'''
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def printBoard():
    for i in board:
        print(i)
    print()


def findBigGroup():
    # 1. 가장 큰 블록 그룹을 찾음.
    check = [[False]*N for _ in range(N)]
    candidate = []

    for y in range(N):
        for x in range(N):
            # 일반블록일경우, 방문하지 않았을경우
            # 그룹의 크기, 무지개의 수, 기준블록 행, 기준블록 열

            if board[y][x] >= 1 and check[y][x] == False:
                print(y, x)
                blockNum = board[y][x]
                queue = deque([(y, x)])
                Group = set()
                cntRainbow = 0
                basis = [N, N]
                Loc = []
                while queue:
                    y, x = queue.popleft()
                    check[y][x] = True
                    if (y, x) in Group:
                        continue
                    else:
                        Group.add((y, x))

                    if board[y][x] == 0:
                        cntRainbow += 1
                        Loc.append((y, x))
                    elif board[y][x] == blockNum:
                        if y <= basis[0]:

                            if basis[0] == y:
                                if x <= basis[1]:
                                    basis = [y, x]
                            else:
                                basis = [y, x]
                        check[y][x] = True
                        Loc.append((y, x))
                    else:
                        continue

                    for idx in range(4):
                        ty = y+dy[idx]
                        tx = x+dx[idx]

                        if 0 <= ty < N and 0 <= tx < N and (ty, tx) not in Group and (board[ty][tx] == blockNum or board[ty][tx] == 0) and board[ty][tx] != -2:
                            queue.append((ty, tx))
                print(Loc)
                if len(Loc) <= 1:
                    continue
                candidate.append(
                    [len(Group), cntRainbow, basis[0], basis[1], Group])
    candidate.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    print(candidate)
    if len(candidate) != 0:
        return True, candidate[0][-1]
    else:
        return False, (0, 0)


def addScore(targetGroup):

    for y, x in targetGroup:
        board[y][x] = -2
    return len(targetGroup)**2


def gravity():
    for x in range(N):
        for _ in range(N+1):
            for y in range(N-1):

                # 밑에 칸이 빈칸이고, 나는 검은색 블록이 아닐경우
                if board[y+1][x] == -2 and board[y][x] != -1:
                    board[y+1][x], board[y][x] = board[y][x], board[y+1][x]


def rotate90():
    after = [[0]*N for _ in range(N)]
    for y in range(N-1, -1, -1):
        for x in range(N):
            #print(y, x, '||', N-1-y, x)
            after[N-1-y][x] = board[x][y]
    return after


score = 0
while True:
    state, targetGroup = findBigGroup()
    if state == False:
        break
    score += addScore(targetGroup)
    print('삭제', score)
    printBoard()
    print('중력')
    gravity()
    printBoard()
    board = rotate90()
    print('반시계')
    printBoard()
    print('중력')
    gravity()
    printBoard()

    print('=============')
print(score)
