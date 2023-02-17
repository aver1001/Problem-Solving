import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))


board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))

direct = [[1, 0], [-1, 0], [0, -1], [0, 1]]

start = (0, 0)
end = (Y-1, X-1)
visited = [[[False]*2 for _ in range(X)]for _ in range(Y)]
answer = 1000000

queue = deque([])
queue.append([start, 0, 0])

while queue:
    (y, x), cnt, broke = queue.popleft()

    print(y, x, '##', cnt)

    if (y, x) == end:
        answer = cnt+1
        break

    for addy, addx in direct:
        if 0 <= y+addy < Y and 0 <= x+addx < X:

            # 길이 막혀있다면
            if board[y+addy][x+addx] == '1':
                # 아무것도 안부셨을때만 고고
                if broke == 0:
                    if visited[y+addy][x+addx][1] == True:
                        continue
                    visited[y+addy][x+addx][1] = True
                    queue.append([(y+addy, x+addx), cnt+1, broke+1])
                    continue
            else:
                if broke == 0:
                    if visited[y+addy][x+addx][0] == True:
                        continue
                    visited[y+addy][x+addx][0] = True
                    queue.append([(y+addy, x+addx), cnt+1, broke])
                else:
                    if visited[y+addy][x+addx][1] == True:
                        continue
                    visited[y+addy][x+addx][1] = True
                    queue.append([(y+addy, x+addx), cnt+1, broke])


if answer == 1000000:
    print(-1)
else:
    print(answer)
