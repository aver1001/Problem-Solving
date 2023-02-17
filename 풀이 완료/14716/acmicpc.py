import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
check = []
    
for y in range (Y):
    for x in range (X):
        if board[y][x] == 1:
            answer += 1
            queue = deque([(y,x)])
            board[y][x] = 0
            while queue:
                y,x = queue.popleft()
                
                
                for dy,dx in d:
                    ty = dy + y
                    tx = dx + x
                    
                    if 0<= ty < Y and 0<= tx < X and board[ty][tx] == 1:
                        queue.append((ty,tx))
                        board[ty][tx] = 0
print(answer)
