import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개
# (빨강 초록 파랑)
# (빨강-초록 파랑)


def findNomarlArea():
    check = [[0]*N for _ in range(N)]
    # 정상인 기준
    cnt = 1
    for y in range(N):
        for x in range(N):
            # 확인이 안된 구역일경우
            if check[y][x] == 0:
                queue = deque([[y, x]])
                check[y][x] = cnt
                while queue:
                    fy, fx = queue.popleft()

                    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ty = dy+fy
                        tx = dx+fx
                        # 범위안에 들어가고 방문안했고, 같은 색일경우
                        if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0 and board[ty][tx] == board[y][x]:
                            check[ty][tx] = cnt
                            queue.append([ty, tx])
                cnt += 1
                for i in check:
                    print(i)
                print()

    return cnt-1


def findSicklArea():
    check = [[0]*N for _ in range(N)]
    # 정상인 기준
    cnt = 1
    for y in range(N):
        for x in range(N):
            # 확인이 안된 구역일경우
            if check[y][x] == 0:
                queue = deque([[y, x]])
                check[y][x] = cnt
                while queue:
                    fy, fx = queue.popleft()

                    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ty = dy+fy
                        tx = dx+fx
                        # 범위안에 들어가고 방문안했고, 같은 색일경우
                        if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0:
                            if board[y][x] == 'R' or board[y][x] == 'G':
                                if board[ty][tx] != 'B':
                                    check[ty][tx] = cnt
                                    queue.append([ty, tx])

                            else:
                                if board[y][x] == board[ty][tx]:
                                    check[ty][tx] = cnt
                                    queue.append([ty, tx])
                cnt += 1

    for i in check:
        print(i)
    print()
    return cnt-1


print(findNomarlArea(), findSicklArea(), sep=' ')
