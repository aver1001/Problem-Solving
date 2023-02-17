import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))

check = [[[sys.maxsize, sys.maxsize]for _ in range(X)] for _ in range(Y)]


def find(str):
    for y in range(Y):
        for x in range(X):
            if board[y][x] == str:
                return (y, x)


startPoint = find('S')
endPoint = find('F')
queue = deque([(*startPoint, 0, 0)])

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
check[startPoint[0]][startPoint[1]] = [0, 0]

while queue:
    y, x, garbage, aroundGarbage = queue.popleft()

    for idx in range(4):
        ty = dy[idx] + y
        tx = dx[idx] + x
        tempGarbage = garbage
        tempAroundGarabage = aroundGarbage

        if 0 <= ty < Y and 0 <= tx < X:

            # 자신 위치 쓰래기 확인
            if board[ty][tx] == 'g':
                tempGarbage += 1
            # 주변 쓰래기 확인
            elif board[ty][tx] == 'F':
                pass
            elif board[ty][tx] == 'S':
                pass
            else:
                for idx2 in range(4):
                    tty = dy[idx2] + ty
                    ttx = dx[idx2] + tx

                    if 0 <= tty < Y and 0 <= ttx < X:
                        if board[tty][ttx] == 'g':
                            tempAroundGarabage += 1

            # 쓰래기 수가 적을경우
            if check[ty][tx][0] > tempGarbage:
                check[ty][tx][0] = tempGarbage
                check[ty][tx][1] = tempAroundGarabage
                queue.append((ty, tx, tempGarbage, tempAroundGarabage))
            # 쓰래기 수는 같은데 주변이 작을경우
            elif check[ty][tx][0] == tempGarbage and check[ty][tx][1] > tempAroundGarabage:
                check[ty][tx][0] = tempGarbage
                check[ty][tx][1] = tempAroundGarabage
                queue.append((ty, tx, tempGarbage, tempAroundGarabage))


print(*check[endPoint[0]][endPoint[1]])
