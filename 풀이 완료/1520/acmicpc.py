import sys
import heapq
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

heap = [[-board[0][0], 0, 0]]
visited = [[0]*X for _ in range(Y)]
visited[0][0] = 1
while heap:
    cost, y, x = heapq.heappop(heap)
    cost = -cost

    for i in range(4):
        ty = y+dy[i]
        tx = x+dx[i]

        if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] < board[y][x]:
            if visited[ty][tx] == 0:
                visited[ty][tx] += visited[y][x]
                heapq.heappush(heap, [-board[ty][tx], ty, tx])
            else:
                visited[ty][tx] += visited[y][x]


print(visited[-1][-1])
