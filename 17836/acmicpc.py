import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
용사는 1,1 에서 시작
0 빈공간
1 마법의 벽
2 전설의 명검 그람
'''
Y, X, T = map(int, sys.stdin.readline().rstrip().split(' '))
board = []
checkOne = [[0]*X for _ in range(Y)]
checkTwo = [[0]*X for _ in range(Y)]
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

queue = deque([[0, 0, 0, False]])
checkOne[0][0] = 1

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while queue:
    y, x, cnt, getSword = queue.popleft()

    for dx, dy in direction:
        ty = dy+y
        tx = dx+x

        # 범위 확인
        if 0 <= ty < Y and 0 <= tx < X:
            if ty == Y-1 and tx == X-1:
                print(cnt+1)
                exit()

            if cnt >= T:
                print('Fail')
                exit()

            # 칼 얻엇을경우
            if getSword and checkTwo[ty][tx] == 0:
                checkTwo[ty][tx] = 1
                queue.append([ty, tx, cnt+1, True])
            # 칼 없을경우
            else:

                if board[ty][tx] == 0 and checkOne[ty][tx] == 0:
                    checkOne[ty][tx] = 1
                    queue.append([ty, tx, cnt+1, False])
                elif board[ty][tx] == 2:
                    checkOne[ty][tx] = 1
                    queue.append([ty, tx, cnt+1, True])

print('Fail')
