from collections import deque

import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
answer = 0
for y in range(N):
    for x in range(N):

        queue = deque([[y, x, 1]])
        while queue:
            y, x, cnt = queue.popleft()
            if cnt > answer:
                answer = cnt

            for idx in range(4):
                ty = y+dy[idx]
                tx = x+dx[idx]

                # 좌표 넘어가는거 체크
                if 0 <= ty < N and 0 <= tx < N:
                    # 이전 좌표보다 더 많은 대나무 개수 확인
                    if board[ty][tx] > board[y][x]:
                        queue.append([ty, tx, cnt+1])


print(answer)
