import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N, L, R = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def createUnion():
    check = [[0 for _ in range(N)] for _ in range(N)]
    hap = {}
    cnt = 0
    for y in range(N):
        for x in range(N):
            if check[y][x] == 0:
                queue = deque([])
                queue.append([y, x])
                cnt += 1
                hap[cnt] = [board[y][x]]
                check[y][x] = cnt
                while queue:
                    ay, ax = queue.popleft()

                    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ty = dy + ay
                        tx = dx + ax

                        if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0:
                            if L <= abs(board[ay][ax] - board[ty][tx]) <= R:
                                check[ty][tx] = cnt
                                queue.append([ty, tx])
                                hap[cnt].append(board[ty][tx])

    for key, value in hap.items():
        hap[key] = int(sum(value) / len(value))
    for y in range(N):
        for x in range(N):
            board[y][x] = hap[check[y][x]]
    if cnt == N*N:
        return False
    else:
        return True


def printBoard():
    for i in board:
        print(i)
    print()


answer = 0
while True:
    if createUnion():
        answer += 1
    else:
        break
print(answer)
