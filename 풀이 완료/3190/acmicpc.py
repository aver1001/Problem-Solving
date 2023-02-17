from collections import deque


n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
dx, dy = (0, 1, 0, -1),  (1, 0, -1, 0)
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

l = int(input())
turns = dict()
for _ in range(l):
    s, d = input().split()
    turns[int(s)] = 1 if d == "D" else -1

sec = 0
x, y, d = 0, 0, 0
snake = deque([(0, 0)])
graph[0][0] = 1

while True:
    sec += 1
    x, y = x + dx[d], y + dy[d]

    if not 0 <= x < n or not 0 <= y < n or graph[x][y] == 1:
        break

    if graph[x][y] == 0:
        snake.append((x, y))
        graph[x][y] = 1
        a, b = snake.popleft()
        graph[a][b] = 0
    elif graph[x][y] == 2:
        snake.append((x, y))
        graph[x][y] = 1

    if sec in turns:
        d = (d + turns[sec]) % 4

print(sec)
