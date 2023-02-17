import sys
from collections import deque
sys.stdin = open('input.txt', "r")

K = int(sys.stdin.readline().rstrip())
X, Y = map(int, sys.stdin.readline().rstrip().split(' '))

board = []

for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


visited = [[[9999999]*(K+1) for _ in range(X)]for _ in range(Y)]
# 왼쪽은

# y,x,cnt,말횟수
queue = deque([[0, 0, 0, 0]])
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
hy = (-1, 1, -2, 2, -2, 2, -1, 1)
hx = (-2, -2, -1, -1, 1, 1, 2, 2)

while queue:
    y, x, cnt, horse = queue.popleft()
    # 그냥 평범한 움직임
    if y == Y-1 and x == X-1:
        print(cnt)
        exit()
    for i in range(4):
        ty = dy[i] + y
        tx = dx[i] + x
        # 범위체크
        if 0 <= tx < X and 0 <= ty < Y and board[ty][tx] != 1:
            if horse == 0:
                if visited[ty][tx][0] == 0:
                    visited[ty][tx][0] = cnt+1
                    queue.append([ty, tx, cnt+1, horse])
            else:
                if visited[ty][tx][horse] >= cnt+1:
                    visited[ty][tx][horse] = cnt+1
                    queue.append([ty, tx, cnt+1, horse])

    # 말의 움직임이 가능하다면
    if horse < K:
        for i in range(8):
            ty = hy[i] + y
            tx = hx[i] + x

            if 0 <= tx < X and 0 <= ty < Y and board[ty][tx] != 1:
                if visited[ty][tx][horse+1] == 0:
                    visited[ty][tx][horse+1] = cnt+1
                    queue.append([ty, tx, cnt+1, horse+1])


print(-1)
